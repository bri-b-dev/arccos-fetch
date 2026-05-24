#!/usr/bin/env python3
"""
Fetch all Arccos Golf rounds and per-round stats, saving each as JSON in data/.

Usage:
  python fetch_rounds.py            # single run (ideal for cron)
  python fetch_rounds.py --watch 60 # re-run every 60 minutes

Cron example (daily at 22:00):
  0 22 * * * /path/to/.venv/bin/python /path/to/fetch_rounds.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
AUTH_URL = os.environ["ARCCOS_AUTHENTICATION_URL"].rstrip("/")
API_URL = os.environ["ARCCOS_API_URL"].rstrip("/")
GOAL_HCP = int(os.getenv("GOAL_HCP", "20"))

DATA_DIR = Path(__file__).parent / "data"
ROUNDS_INDEX = DATA_DIR / "rounds_index.json"

HEADERS = {"accept": "application/json", "content-type": "application/json;charset=utf-8"}
PAGE_SIZE = 50


def authenticate() -> tuple[str, str]:
    r = requests.post(
        f"{AUTH_URL}/accessKeys",
        headers=HEADERS,
        json={"email": EMAIL, "password": PASSWORD, "signedInByFacebook": "F"},
    )
    r.raise_for_status()
    keys = r.json()
    user_id = keys["userId"]
    access_key = keys["accessKey"]

    r = requests.post(
        f"{AUTH_URL}/tokens",
        headers=HEADERS,
        json={"accessKey": access_key, "userId": user_id},
    )
    r.raise_for_status()
    token = r.json()["token"]
    return user_id, token


def auth_headers(token: str) -> dict:
    return {**HEADERS, "authorization": f"Bearer: {token}"}


def fetch_new_rounds(user_id: str, token: str) -> list[dict]:
    """Fetch rounds page by page (newest first) and stop at the first already-saved round."""
    new_rounds: list[dict] = []
    offset = 0
    while True:
        r = requests.get(
            f"{API_URL}/v2/users/{user_id}/rounds",
            headers=auth_headers(token),
            params={"limit": PAGE_SIZE, "offSet": offset, "roundType": "flagship"},
        )
        r.raise_for_status()
        data = r.json()
        batch = data["rounds"]
        if not batch:
            break
        for round_meta in batch:
            if (DATA_DIR / f"round_{round_meta['roundId']}.json").exists():
                return new_rounds
            new_rounds.append(round_meta)
        offset += len(batch)
    return new_rounds


def fetch_stats(user_id: str, token: str, round_id: int) -> dict:
    r = requests.get(
        f"{API_URL}/sga/getDashboardAnalysis/{user_id}",
        headers=auth_headers(token),
        params={"goalHcp": -GOAL_HCP, "roundId": round_id},
    )
    r.raise_for_status()
    return r.json()


def run_once() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    print("Authenticating...")
    user_id, token = authenticate()
    print(f"  userId: {user_id}")

    print("Fetching new rounds...")
    rounds = fetch_new_rounds(user_id, token)
    if not rounds:
        print("  No new rounds.")
        return 0
    print(f"  {len(rounds)} new round(s) found")

    new_count = 0
    for i, round_meta in enumerate(rounds, 1):
        round_id = round_meta["roundId"]
        out_path = DATA_DIR / f"round_{round_id}.json"
        date = (round_meta.get("startTime") or "")[:10]
        course = round_meta.get("courseName", "")
        print(f"  [{i}/{len(rounds)}] {date} {course} (id={round_id})")

        try:
            stats = fetch_stats(user_id, token, round_id)
        except requests.HTTPError as e:
            print(f"    Warning: stats fetch failed ({e}) — saving round metadata only")
            stats = {}

        out_path.write_text(
            json.dumps({"round": round_meta, "stats": stats}, indent=2),
            encoding="utf-8",
        )
        new_count += 1

    # Prepend new rounds to the index
    existing = json.loads(ROUNDS_INDEX.read_text()) if ROUNDS_INDEX.exists() else []
    ROUNDS_INDEX.write_text(json.dumps(rounds + existing, indent=2), encoding="utf-8")

    print(f"Done. {new_count} new round(s) saved to {DATA_DIR}/")
    return new_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Arccos rounds to data/")
    parser.add_argument(
        "--watch",
        type=int,
        metavar="MINUTES",
        help="Re-run every N minutes (leave blank to run once)",
    )
    args = parser.parse_args()

    if args.watch:
        print(f"Watch mode: polling every {args.watch} minute(s). Ctrl+C to stop.")
        while True:
            try:
                run_once()
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
            print(f"Sleeping {args.watch}m...")
            time.sleep(args.watch * 60)
    else:
        try:
            run_once()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
