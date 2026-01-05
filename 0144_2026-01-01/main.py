# Day 144 — 2026-01-01
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-01

goal = [10000, 120, 5]


def resolution_streak(days):
    streak = 0
    failed = 0
    for day in days:
        if day[0] >= goal[0] and day[1] <= goal[1] and day[2] >= goal[2]:
            streak += 1
        else:
            failed = days.index(day)
            break
    if failed:
        return f"Resolution failed on day {failed}: {10} day streak."
    else:
        return f"Resolution on track: {10} day streak."


if __name__ == "__main__":
    print(
        resolution_streak(
            [
                [10500, 75, 15],
                [11000, 90, 10],
                [10650, 100, 9],
                [10200, 60, 10],
                [10678, 87, 9],
                [12431, 67, 13],
                [10444, 107, 19],
                [10111, 95, 5],
                [10000, 120, 7],
                [11980, 101, 8],
            ]
        )
    )
