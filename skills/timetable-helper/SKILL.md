---
name: timetable-helper
description: Look up university class schedules, room numbers, faculty, and lab timings for student batches from the official CSV timetable. Trigger whenever a user asks about classes, lectures, labs, schedules, rooms, or timetable slots for a batch or day.
---

# Timetable Helper

## Instructions
1. Always query `scripts/lookup_timetable.py` or inspect `references/timetable.csv` before answering any schedule question.
2. Never invent, extrapolate, or guess classes, rooms, or instructors not explicitly present in `references/timetable.csv`.
3. If a batch, day, or course is missing from the CSV, state clearly: `"No scheduled class found in the official timetable for that query."`
4. Consult `references/column_dictionary.md` for schema definitions and `references/edge_cases.md` for holidays, cancelled slots, and lab groupings.
