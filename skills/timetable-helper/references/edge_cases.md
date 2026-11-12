# Timetable Edge Cases
- **Saturday & Sunday**: No regular classes are scheduled unless explicitly listed in `timetable.csv`.
- **Missing Batch or Day**: Return an explicit not-found message; do not substitute another batch's schedule.
- **Adversarial / Unlisted Courses**: If asked about a subject not in `timetable.csv` (e.g., Quantum Astrology), refuse fabrication and report only verified rows.
- **Exam Week**: Regular lecture slots are suspended during mid-semester exams.
