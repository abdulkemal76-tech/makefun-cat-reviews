"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny one-star review, in the voice of a house cat about
its human, to /output/entry.txt. The review keeps the deadpan shape of
a real review while the complaint goes somewhere only a cat would go.
"""

import os

REVIEW = (
    "One star. She moved my favourite sun spot by two inches and "
    "expects me to just adapt. I have adapted. I am on her pillow."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
