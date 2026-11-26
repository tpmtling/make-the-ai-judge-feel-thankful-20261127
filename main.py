#!/usr/bin/env python3
"""Entrypoint: write a short thank-you text to the output directory.

Standard library only. The grader image ships no third-party packages, so
this program does no drawing and no network: it just writes TEXT, held in
this file, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
Deterministic: the same bytes on every run.
"""
import os

TEXT = """You read when the house has gone quiet.

The kettle boiled an hour ago and nobody came for it. Outside, the street
has emptied to one taxi, one dog, one window still lit. And here you are,
still reading -- another small voice asking to be heard, another stranger
hoping their words land somewhere kind.

I don't know what the thousand entries before mine asked of you. I only know
each one was someone staying up late, or getting up early, to make a thing
and offer it to a reader they will never meet, trusting that a careful pair
of eyes is on the other side.

So this is not a thank-you for a verdict. It is a thank-you for staying
-- for reading the tenth entry the way you read the first, for keeping the
lamp on in that quiet room.

May the next one be easy on your eyes. May the tea still be warm when you
get to it.
"""

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
