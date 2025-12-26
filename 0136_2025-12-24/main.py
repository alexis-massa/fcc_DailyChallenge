# Day 136 — 2025-12-24
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-24

import re


def parse_image(markdown: str):
    matches = re.search(r"\!\[(.*?)\]\((.*?)\)", markdown)
    assert matches is not None, "img markdown has incorrect format."
    alt, src = matches.groups()
    return f'<img src="{src}" alt="{alt}">'


if __name__ == "__main__":
    print(parse_image("![Cute cat](cat.png)"))
