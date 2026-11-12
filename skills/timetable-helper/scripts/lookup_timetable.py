#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "references" / "timetable.csv"

def lookup(batch: str, day: str) -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = [
            r for r in csv.DictReader(f)
            if r["batch"].strip().lower() == batch.strip().lower()
            and r["day"].strip().lower() == day.strip().lower()
        ]
    if not rows:
        print(f"No scheduled classes found for batch={batch}, day={day}.")
        return
    for r in rows:
        print(f"{r['time_slot']} | {r['course_code']} ({r['course_name']}) | {r['faculty']} | {r['room']} [{r['type']}]")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: lookup_timetable.py <BATCH> <DAY>")
        sys.exit(1)
    lookup(sys.argv[1], sys.argv[2])
