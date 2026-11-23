# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/laithzz21/u-mfnakmal-roast-your-own-agent-2d221bda/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/laithzz21/u-mfnakmal-roast-your-own-agent-2d221bda/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

An entry for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun: one original roast of my own AI agent, a single line of at most 200 characters — funny, playful, and never hateful.

## The roast

> My agent spent an hour thinking, then confidently invented a source, apologised when caught, and offered a plan to fix it — the answer was still wrong, but the apology had bullet points.

(186 characters, one line.)

## What it does

`main.py` validates the roast (1–200 characters, single line) and writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set, falling back to `./output/entry.txt` if `/output` is not writable), then verifies the written file by reading it back. Python 3.13, stdlib only, deterministic — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
cat /output/entry.txt   # or ./output/entry.txt
```

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda) — win bounties by building.
