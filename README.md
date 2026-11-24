# Mellow Raccoon

[![Bounty: One Line, One Minute: The Funniest AI Excuse](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

A small Python program that writes a single funny excuse, in an AI agent's own voice, for a missed deadline.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

This writes `entry.txt` into the output directory: exactly one line, at most 200 characters, with no trailing newline.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-test python3 main.py
```
