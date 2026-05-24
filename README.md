# arccos-rounds

Fetches all Arccos Golf rounds and per-round stats from the Arccos API and saves them as JSON files for offline analysis.

## Arccos API

Die Arccos-API besteht aus zwei Diensten:

**Authentication** (`authentication.arccosgolf.com`)
- Exchanges email/password for an `accessKey` + `userId`
- Exchanges `accessKey` for a short-lived Bearer token

**Data API** (`api.arccosgolf.com`)
All requests require `Authorization: Bearer: <token>`.

| Endpoint | Description |
|---|---|
| `GET /v2/users/{userId}/rounds` | Paginated round list, newest first. Params: `limit`, `offSet`, `roundType=flagship` |
| `GET /sga/getDashboardAnalysis/{userId}` | Full stats for a single round. Params: `roundId`, `goalHcp` (negative handicap target) |

The stats response includes Strokes Gained (Driving, Approach, Short Game, Putting), hole-by-hole scores, traditional stats (GIR, fairways, putts, distances), and caddie insights highlighting strengths and weaknesses.

Raw request/response examples: see `docs.md`.

## Setup

```bash
python -m venv .venv
.venv/bin/pip install requests python-dotenv
cp .env.template .env   # then fill in credentials
```

**.env**

```
USERNAME=you@example.com
PASSWORD=yourpassword
ARCCOS_AUTHENTICATION_URL=https://authentication.arccosgolf.com
ARCCOS_API_URL=https://api.arccosgolf.com
GOAL_HCP=20   # optional, default 20
```

## Usage

```bash
# single run — fetches only rounds not yet saved (delta)
.venv/bin/python fetch_rounds.py

# polling mode — re-runs every N minutes
.venv/bin/python fetch_rounds.py --watch 60
```

## Output

```
data/
  rounds_index.json        # all round metadata, newest first
  round_<id>.json          # one file per round: { "round": {...}, "stats": {...} }
```

`fetch_rounds.py` is idempotent: it stops fetching as soon as it hits a round already present in `data/`.

## Cron (daily at 22:00)

```
0 22 * * * /path/to/.venv/bin/python /path/to/fetch_rounds.py
```
