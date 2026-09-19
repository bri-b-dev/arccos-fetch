"""
Parses all round_*.json exports from Arccos and computes the aggregates used in
rounds_analysis.html: monthly trend, season comparison (2025 vs 2026), and
category-level Strokes Gained (SGA) breakdowns.

Usage:
    .venv/bin/python analyze_rounds.py
"""

import json
import glob
import os
import statistics
from datetime import datetime
from collections import defaultdict, Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def load_records():
    records = []
    for path in glob.glob(os.path.join(DATA_DIR, "round_*.json")):
        with open(path) as f:
            d = json.load(f)
        r = d.get("round", {})
        stats = d.get("stats", {})
        overall = stats.get("overall", {})
        section = overall.get("overallSection", {})
        trad = overall.get("traditionalStats") or {}

        if r.get("isDeleted") == "T" or not r.get("startTime"):
            continue

        holes = r.get("noOfHoles") or 18
        over_under = r.get("overUnder")

        gir = trad.get("gir", {})
        gir_pct = gir.get("noOfGirsHit", 0) / gir["noOfHoles"] * 100 if gir.get("noOfHoles") else None

        fw = trad.get("hitFairway", {})
        fw_pct = fw.get("fairways", 0) / fw["totalFairways"] * 100 if fw.get("totalFairways") else None

        putts = trad.get("totalPutts", {})
        putts_per_hole = putts["value"] / holes if putts.get("value") is not None and holes else None

        updown = trad.get("upAndDown", {})
        updown_pct = updown.get("upAndDownSuccess", 0) / updown["totalChances"] * 100 if updown.get("totalChances") else None

        records.append({
            "roundId": r.get("roundId"),
            "date": r.get("startTime"),
            "dt": datetime.fromisoformat(r["startTime"].replace("Z", "+00:00")),
            "courseName": r.get("courseName"),
            "holes": holes,
            "overUnder": over_under,
            "overUnder18": over_under / holes * 18 if over_under is not None else None,
            "includedInHcp": r.get("includedInLatestHandicap"),
            "sga_overall_18": section.get("sga") / holes * 18 if section.get("sga") is not None else None,
            "sga_driving_18": section.get("drivingSga") / holes * 18 if section.get("drivingSga") is not None else None,
            "sga_approach_18": section.get("approachSga") / holes * 18 if section.get("approachSga") is not None else None,
            "sga_short_18": section.get("shortSga") / holes * 18 if section.get("shortSga") is not None else None,
            "sga_putting_18": section.get("puttingSga") / holes * 18 if section.get("puttingSga") is not None else None,
            "gir_pct": gir_pct,
            "fairway_pct": fw_pct,
            "putts_per_hole": putts_per_hole,
            "updown_pct": updown_pct,
        })

    records.sort(key=lambda x: x["date"])
    return records


def avg(records, key):
    vals = [r[key] for r in records if r[key] is not None]
    return sum(vals) / len(vals) if vals else None


def season(records, year, month_start, month_end):
    return [r for r in records if r["dt"].year == year and month_start <= r["dt"].month <= month_end]


def print_monthly(records):
    print("\n=== Monatlicher Trend ===")
    monthly = defaultdict(list)
    for r in records:
        monthly[r["dt"].strftime("%Y-%m")].append(r)
    for key in sorted(monthly):
        g = monthly[key]
        print(
            f"{key}  n={len(g):<2}"
            f"  toPar18={fmt(avg(g,'overUnder18'))}"
            f"  sga={fmt(avg(g,'sga_overall_18'))}"
            f"  drv={fmt(avg(g,'sga_driving_18'))}"
            f"  app={fmt(avg(g,'sga_approach_18'))}"
            f"  sht={fmt(avg(g,'sga_short_18'))}"
            f"  putt={fmt(avg(g,'sga_putting_18'))}"
        )


def fmt(v, nd=1):
    return f"{v:.{nd}f}" if v is not None else "n/a"


def print_season_comparison(records):
    s2025 = season(records, 2025, 4, 10)
    s2026 = season(records, 2026, 3, 9)

    print(f"\n=== Saisonvergleich (April–Oktober) ===")
    print(f"2025: n={len(s2025)}   2026: n={len(s2026)}")

    keys = [
        ("Score über Par (norm. 18 Loch)", "overUnder18", 1),
        ("Strokes Gained gesamt", "sga_overall_18", 2),
        ("SGA Driving", "sga_driving_18", 2),
        ("SGA Approach", "sga_approach_18", 3),
        ("SGA Short Game", "sga_short_18", 2),
        ("SGA Putting", "sga_putting_18", 2),
        ("GIR %", "gir_pct", 1),
        ("Fairways getroffen %", "fairway_pct", 1),
        ("Putts / Loch", "putts_per_hole", 2),
        ("Up & Down %", "updown_pct", 1),
    ]
    for label, k, nd in keys:
        v25, v26 = avg(s2025, k), avg(s2026, k)
        print(f"{label:32s} 2025={fmt(v25,nd):>8}   2026={fmt(v26,nd):>8}")

    def stdev(lst, key):
        vals = [r[key] for r in lst if r[key] is not None]
        return statistics.pstdev(vals)

    print(f"{'Streuung (Std.-Abw. Score)':32s} 2025={stdev(s2025,'overUnder18'):>8.1f}   2026={stdev(s2026,'overUnder18'):>8.1f}")

    print("\nincludedInLatestHandicap:")
    print("  2025:", Counter(r["includedInHcp"] for r in s2025))
    print("  2026:", Counter(r["includedInHcp"] for r in s2026))

    print("\nNur reine 9-Loch-Runden, roher overUnder (keine Hochrechnung):")
    for label, g in [("2025", s2025), ("2026", s2026)]:
        sub = [r["overUnder"] for r in g if r["holes"] == 9 and r["overUnder"] is not None]
        print(f"  {label}: n={len(sub)} mean={sum(sub)/len(sub):.1f} median={statistics.median(sub):.1f}")


def print_outliers(records, since_year=2025, since_month=9, since_day=18):
    cutoff = datetime(since_year, since_month, since_day, tzinfo=records[0]["dt"].tzinfo)
    recent = [r for r in records if r["dt"] >= cutoff and r["sga_overall_18"] is not None]
    recent.sort(key=lambda r: r["sga_overall_18"])
    print(f"\n=== Ausreißer (seit {cutoff.date()}) ===")
    print("Schwächste:", recent[0]["date"][:10], recent[0]["courseName"], f"toPar18={recent[0]['overUnder18']:.1f}", f"sga={recent[0]['sga_overall_18']:.1f}")
    print("Stärkste: ", recent[-1]["date"][:10], recent[-1]["courseName"], f"toPar18={recent[-1]['overUnder18']:.1f}", f"sga={recent[-1]['sga_overall_18']:.1f}")


if __name__ == "__main__":
    records = load_records()
    print(f"Runden gesamt: {len(records)}")
    print(f"Zeitraum: {records[0]['date'][:10]} – {records[-1]['date'][:10]}")
    print("Loch-Verteilung:", Counter(r["holes"] for r in records))

    print_monthly(records)
    print_season_comparison(records)
    print_outliers(records)
