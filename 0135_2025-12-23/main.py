# Day 135 — 2025-12-23
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-23

import re


def email_chain_count(subject):
    return len(re.findall(r"\b(fw:|fwd:|re:)", subject, re.IGNORECASE))
