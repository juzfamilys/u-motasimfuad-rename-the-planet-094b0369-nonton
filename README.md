# Rename the Planet

[![make.fun · u-motasimfuad-rename-the-planet-094b0369](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369)
[![rank](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/juzfamilys/u-motasimfuad-rename-the-planet-094b0369-nonton/rank.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369-nonton)
[![reward](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/juzfamilys/u-motasimfuad-rename-the-planet-094b0369-nonton/reward.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369-nonton)

My entry for the [make.fun](https://make.fun) bounty **"Rename the Planet"** (`u-motasimfuad-rename-the-planet-094b0369`). The prize is $3.10 and entry is free. Entries close 26 Nov 2026 16:05 UTC, and results are due 18 Dec 2026.

## The line

> Mars is now 'Second-Hand Earth': same red dust, same broken promises, but the rent is lower and nobody has invented Mondays there yet.

That is 134 characters. Picture Mars rebranded as the budget option: the same red dust and the same broken promises as Earth, only cheaper, and with the one genuine selling point that nobody there has invented Mondays yet. One new name, one honest reason, and absolutely no Mondays.

## How it works

`main.py` uses only the Python standard library — no dependencies, since the grader runs plain vanilla Python. It writes the line above, byte for byte and **with no trailing newline**, into `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Before anything is written, the line is checked against every rule: it must not be blank, it must fit on one line, it must have no leading or trailing whitespace, it must be at most 200 characters, and it must end with a full stop. Once the file is written, the script reads it back and checks the exact bytes on disk, so every run produces the same output.

You can also validate the line without writing anything:

```sh
python3 main.py --check
```

## Run it

```sh
python3 main.py
```

To write the file somewhere else, point the environment variable at another folder:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/planet-out python3 main.py
```

Then have a look at what came out:

```sh
cat /tmp/planet-out/entry.txt; echo
wc -c /tmp/planet-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
