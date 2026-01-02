# Day 145 — 2026-01-02
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-02
def nth_fibonacci(n: int):
    assert n >= 0, "n must be non-negative"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print(nth_fibonacci(75))
