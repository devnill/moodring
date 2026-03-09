# Module: Mood Log

## Scope
Shell script (`scripts/write-log.sh`) that appends a single JSONL entry to the mood log file. Each entry records a timestamp, mood label, and session ID.

NOT responsible for: deciding which mood to log (that comes from `mood-handler`), reading or analyzing the log, or any visualization.

## Provides
- `write-log.sh` — Shell script at `scripts/write-log.sh`
  - Invocation: `write-log.sh <MoodLabel> <SessionID>`
  - Behavior: Appends one JSON line to `mood-log.jsonl`

## Requires
Nothing from other modules at the interface level. Uses the log schema defined in the architecture.

## Boundary Rules
- Must exit 0 on any error
- Must write exactly one line per invocation
- Must use ISO 8601 timestamps (UTC)
- Log file is `${PLUGIN_ROOT}/mood-log.jsonl` — created on first write if it does not exist
- Must not read or parse existing log entries
- Must not perform any analysis or aggregation (Constraint #12, Principle #8)
- Entries contain exactly three fields: `timestamp`, `mood`, `session_id` (Constraint #8)
- Must handle concurrent writes safely (append is atomic for short lines on POSIX)

## Internal Design Notes

### Script Structure

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

### File Creation

The `>>` operator creates the file if it does not exist. No explicit creation needed.

### Concurrency

POSIX guarantees that `write()` calls of `PIPE_BUF` bytes or fewer (512 bytes minimum, typically 4096) are atomic. A single JSONL entry is well under this limit. No locking needed.

### No Rotation

v1 does not rotate or truncate the log file. For long-running experiments, external tooling handles log management.
