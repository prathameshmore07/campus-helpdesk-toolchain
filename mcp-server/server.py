#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("campus-helpdesk-server")

TIMETABLE_DATA = {
    ("CSE-A", "Monday"): [
        {"time": "09:00-10:00", "course": "CS301 Operating Systems", "room": "LH-101"},
        {"time": "10:00-11:00", "course": "CS302 DBMS", "room": "LH-101"},
        {"time": "11:15-13:15", "course": "CS302L DBMS Lab", "room": "LAB-03"},
    ],
    ("CSE-B", "Monday"): [
        {"time": "09:00-10:00", "course": "CS303 Computer Networks", "room": "LH-201"},
    ],
}

FEE_RECORDS = {
    "STU1001": {"name": "Aarav Mehta", "semester": "Sem 5", "status": "PAID", "balance_inr": 0, "receipt_id": "RCP-2026-881"},
    "STU1002": {"name": "Diya Nair", "semester": "Sem 5", "status": "PENDING", "balance_inr": 42500, "receipt_id": None},
}

HOSTEL_RULES_MD = """# University Hostel Rules
1. Main gate curfew is 10:30 PM on weekdays and 11:30 PM on weekends.
2. Electric kettles, heaters, and induction stoves are prohibited inside dorm rooms.
3. Overnight guests require prior warden approval 24 hours in advance.
4. Quiet hours are enforced from 11:00 PM to 06:00 AM daily.
"""

@mcp.tool()
def get_timetable(batch: str, day: str) -> dict:
    """Return verified class schedule entries for an exact university batch (e.g., CSE-A) and weekday (e.g., Monday)."""
    clean_batch = batch.strip().upper()
    clean_day = day.strip().capitalize()
    if clean_day not in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}:
        raise ValueError(f"Invalid day '{day}'. Provide a full weekday name such as Monday.")
    entries = TIMETABLE_DATA.get((clean_batch, clean_day), [])
    return {"batch": clean_batch, "day": clean_day, "classes": entries}

@mcp.tool()
def get_fee_status(student_id: str) -> dict:
    """Look up tuition fee payment status, remaining balance, and receipt ID for a valid student ID (e.g., STU1001)."""
    clean_id = student_id.strip().upper()
    if clean_id not in FEE_RECORDS:
        raise ValueError(f"Unknown student_id '{student_id}'. Expected format: STU1001.")
    return {"student_id": clean_id, **FEE_RECORDS[clean_id]}

@mcp.resource("campus://hostel/rules")
def hostel_rules() -> str:
    """Official university hostel rules and curfew policy document."""
    return HOSTEL_RULES_MD

if __name__ == "__main__":
    mcp.run(transport="stdio")
