#!/usr/bin/env python3

import sys
import subprocess
import re
from pathlib import Path
from datetime import date, timedelta

CHALLENGE_1_DATE = date(2025, 8, 11)


def main():
    assert len(sys.argv) == 2, sys.exit(
        "Usage: python3 auto_commit.py <challenge_number>"
    )

    try:
        number = int(sys.argv[1])
        if number < 1:
            raise ValueError
    except ValueError:
        sys.exit("Challenge number must be a positive integer")

    challenge_date = CHALLENGE_1_DATE + timedelta(days=number - 1)
    date_str = challenge_date.isoformat()
    num_str = f"{number:04d}"
    folder_name = f"{num_str}_{date_str}"

    day_dir = Path(folder_name)
    assert day_dir.exists(), sys.exit(f"Folder not found: {folder_name}")

    main_py = day_dir / "main.py"
    assert main_py.exists(), sys.exit("main.py not found")

    content = main_py.read_text()
    match = re.search(
        r"^def\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        content,
        re.MULTILINE,
    )

    assert match is not None, sys.exit("No Python function found in main.py")

    func_name = match.group(1).replace("_", " ")

    commit_message = f"#{number}: {date_str} - {func_name}"

    subprocess.run(["git", "add", str(day_dir)], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print(f"Committed: {commit_message}")


if __name__ == "__main__":
    main()
