# Day 138 — 2025-12-26
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-26


def sum_divisors(n: int):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum


if __name__ == "__main__":
    print(sum_divisors(9348))
