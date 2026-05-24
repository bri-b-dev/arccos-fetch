# arccos-rounds

Arccos Golf API client that fetches rounds and stats, saving them as JSON in `data/`.

## Commands

```bash
.venv/bin/python fetch_rounds.py          # fetch new rounds (delta)
.venv/bin/python fetch_rounds.py --watch 60  # polling mode
```

## Project structure

- `fetch_rounds.py` — main script
- `data/rounds_index.json` — all round metadata (newest first)
- `data/round_<id>.json` — per-round file with `round` and `stats` keys
- `.env` — credentials (not committed); see `.env.template`
- `docs.md` — raw Arccos API documentation with example responses

## API flow

1. POST `{ARCCOS_AUTHENTICATION_URL}/accessKeys` → userId, accessKey
2. POST `{ARCCOS_AUTHENTICATION_URL}/tokens` → token
3. GET `{ARCCOS_API_URL}/v2/users/{userId}/rounds?limit=50&offSet=0&roundType=flagship` (paginated)
4. GET `{ARCCOS_API_URL}/sga/getDashboardAnalysis/{userId}?goalHcp=-{GOAL_HCP}&roundId={id}` per round

## Delta fetch logic

Rounds come back newest-first. `fetch_rounds.py` fetches pages until it finds a `round_{id}.json` that already exists, then stops. On a fresh `data/` it downloads everything.

## Environment variables

| Variable | Required | Default |
|---|---|---|
| USERNAME | yes | — |
| PASSWORD | yes | — |
| ARCCOS_AUTHENTICATION_URL | yes | — |
| ARCCOS_API_URL | yes | — |
| GOAL_HCP | no | 20 |

## Dependencies

`requests`, `python-dotenv` — install via `.venv/bin/pip install requests python-dotenv`
