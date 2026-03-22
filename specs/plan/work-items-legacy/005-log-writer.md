# 005: Log Writer

## Objective
Create `scripts/write-log.sh` that appends a single JSONL entry (timestamp, mood, session_id) to the mood log file.

## Acceptance Criteria
- [ ] File `scripts/write-log.sh` exists and is executable
- [ ] Given arguments "Focus" "session123", appends one line to `mood-log.jsonl`
- [ ] Appended line is valid JSON with exactly three keys: `timestamp`, `mood`, `session_id`
- [ ] `timestamp` is ISO 8601 UTC format (e.g., `2026-03-08T14:23:01Z`)
- [ ] `mood` contains the first argument value
- [ ] `session_id` contains the second argument value
- [ ] If second argument is missing, `session_id` defaults to `"unknown"`
- [ ] If first argument is empty, script exits 0 without writing
- [ ] `mood-log.jsonl` is created if it does not exist
- [ ] Script always exits 0

## File Scope
- `scripts/write-log.sh` (create)

## Dependencies
- Depends on: none
- Blocks: 006

## Implementation Notes

```bash
#!/bin/sh
MOOD="${1:-}"
SESSION_ID="${2:-unknown}"
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
LOG_FILE="${PLUGIN_ROOT}/mood-log.jsonl"

[ -z "$MOOD" ] && exit 0

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "{\"timestamp\":\"${TIMESTAMP}\",\"mood\":\"${MOOD}\",\"session_id\":\"${SESSION_ID}\"}" >> "$LOG_FILE"

exit 0
```

### Key Decisions
- Uses `date -u` for UTC timestamps — consistent regardless of local timezone
- JSON is constructed via string interpolation — safe because mood labels are from a fixed vocabulary (no special characters) and session IDs are alphanumeric
- `>>` creates the file on first write — no explicit touch/mkdir needed
- Atomic writes: a single JSONL line is well under PIPE_BUF (4096 bytes on macOS), so concurrent appends are safe without locking
- No log rotation in v1

## Complexity
Low
