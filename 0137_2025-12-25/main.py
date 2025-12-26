# Day 137 — 2025-12-25
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-25


def generate_snowflake(crystals: str):
    return "\n".join([line + line[::-1] for line in crystals.split("\n")])


if __name__ == "__main__":
    print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
