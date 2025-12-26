#!/usr/bin/env python3

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

# Challenge #1 metadata
CHALLENGE_1_DATE = date(2025, 8, 11)


def main():
    parser = argparse.ArgumentParser(
        description="Create a FreeCodeCamp daily challenge scaffold"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--date", help="Challenge date (YYYY-MM-DD)")
    group.add_argument("--number", type=int, help="Challenge number (>= 1)")
    args = parser.parse_args()

    # If no argument, default to today
    if not args.date and not args.number:
        challenge_date = date.today()
        delta = (challenge_date - CHALLENGE_1_DATE).days
        if delta < 0:
            sys.exit("Error: today is before challenge #1")
        challenge_number = delta + 1

    elif args.date:
        try:
            challenge_date = date.fromisoformat(args.date)
        except ValueError:
            sys.exit("Error: invalid date format (use YYYY-MM-DD)")
        delta = (challenge_date - CHALLENGE_1_DATE).days
        if delta < 0:
            sys.exit("Error: date is before challenge #1")
        challenge_number = delta + 1

    else:
        if args.number < 1:
            sys.exit("Error: challenge number must be >= 1")
        challenge_number = args.number
        challenge_date = CHALLENGE_1_DATE + timedelta(days=challenge_number - 1)

    date_str = challenge_date.isoformat()
    num_str = f"{challenge_number:04d}"
    folder_name = f"{num_str}_{date_str}"

    # Script is at repo root
    repo_root = Path(__file__).resolve().parent
    day_path = repo_root / folder_name

    if day_path.exists():
        sys.exit(f"Error: {folder_name} already exists")

    day_path.mkdir()

    challenge_url = (
        f"https://www.freecodecamp.org/learn/daily-coding-challenge/{date_str}"
    )

    # Python file
    (day_path / "main.py").write_text(
        f"# Day {challenge_number} — {date_str}\n"
        f"# {challenge_url}\n\n"
        "def main():\n"
        "    pass\n\n"
        "if __name__ == '__main__':\n"
        "    print(main())\n"
    )

    # JavaScript file
    (day_path / "script.js").write_text(
        f"// Day {challenge_number} — {date_str}\n"
        f"// {challenge_url}\n\n"
        "function main() {\n"
        "\n"
        "}\n\n"
        "console.log(main());\n"
    )

    print(f"Created {folder_name}")


if __name__ == "__main__":
    main()
