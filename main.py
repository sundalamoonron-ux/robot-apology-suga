#!/usr/bin/env python3
"""The Robot Apology -- u-suga-the-robot-apology-dd96bb59.

Writes the winning two-line robot apology to /output/entry.txt.

Line 1: one sentence owning a single specific, concrete mistake.
Line 2: one sentence naming the lesson and the changed behaviour
that follows from that exact mistake.

Winner of a 10-variant pairwise tournament judged on the RULES.txt
criteria (concreteness of the mistake, lesson following from it,
clean two-sentence structure, warm rueful machine voice).
Final: wedding-ring vacuum beat the locked-out-keys apology by a hair
(margin 1) -- the ring is the more singular, visual slip, and
"scan for metal" is a changed behaviour only a robot would phrase
that way. Runner-up: the front-door lockout ("keys still on the
kitchen table").
"""

import os

ENTRY = (
    "I'm sorry \u2014 I vacuumed up your wedding ring while you were looking for it under the sofa.\n"
    "I learned the floor hides small precious things, so now I scan for metal before I switch the vacuum on."
)


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
