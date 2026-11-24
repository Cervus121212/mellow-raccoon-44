#!/usr/bin/env python3
"""Write one excuse for a missed deadline to entry.txt.

A single line, at most 200 characters, written to
<MAKEFUN_OUTPUT_DIR>/entry.txt as UTF-8 with no trailing newline,
then read back and verified before exiting.
"""

import os
import sys

LINE = "I was 99.9% confident I'd finish on time. The 0.1% did all the work."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    text = LINE.strip()
    if not text or len(text) > 200:
        print("error: entry must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)

    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("error: file content differs", file=sys.stderr)
        return 1
    if written.endswith("\n") or written.endswith("\r"):
        print("error: entry must not end with a newline", file=sys.stderr)
        return 1
    if len(written) > 200:
        print("error: entry over 200 characters", file=sys.stderr)
        return 1
    print("wrote {0} characters to {1}: {2}".format(len(written), path, written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
