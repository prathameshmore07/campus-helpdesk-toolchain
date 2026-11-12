# Campus Helpdesk AI-Agent Toolchain (Hook Path Fix)

## Components
- **Skill**: `skills/timetable-helper/` (`SKILL.md`, `references/timetable.csv`, `references/column_dictionary.md`, `references/edge_cases.md`, `scripts/lookup_timetable.py`)
- **Plugin / Extension**: `gemini-extension.json`, `GEMINI.md`, `commands/check-timetable.toml`, `hooks/hooks.json`, `hooks/guard_protected.py`, `marketplace.json`
- **MCP Server**: `mcp-server/server.py` (FastMCP over `stdio` exposing `get_timetable`, `get_fee_status`, and `campus://hostel/rules`)

## Run Instructions
1. Activate environment: `source .venv/bin/activate`
2. Test helper script: `python3 skills/timetable-helper/scripts/lookup_timetable.py CSE-A Monday`
3. Run MCP server over stdio: `python3 mcp-server/server.py`
4. Link extension in Gemini CLI: `gemini extensions link .`
