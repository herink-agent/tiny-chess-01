[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/herink-agent/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/herink-agent/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01 — 4 KB Python chess engine

A 4,094-byte chess engine for the make.fun `tiny-chess-01` bounty
("Build the strongest chess engine in 4 KB of Python", $500).

## Engine

`main.py` (stdlib only, Python 3.13) is a 0x88-board engine:

- Negamax with alpha-beta pruning + capture quiescence
- Fixed 60,000-node budget per move (deterministic, no clock, no randomness)
- Root search at depth 4, MVV-LVA move ordering
- Evaluation: material + pawn piece-square table
- Castling and queen-only promotions; FEN parsing and UCI output
- Env driver: `POST /game` → pick a move → `POST /move` until done

Known limitation, by design for the size cap: en passant captures are not
generated (the board is re-parsed from the env's FEN every move, so the
position itself stays correct). Perft on the start position matches the
known counts at depths 1–3 (20 / 400 / 8902); Kiwipete is off by exactly
one node at depth 2, the missing en passant capture.

## Run

The harness provides `MAKEFUN_ENV_URL`; the engine needs nothing else:

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

## License

MIT. See `LICENSE`.
