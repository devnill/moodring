# Decisions: Data

## D-1: Log only timestamp, mood, and session_id — no task summarization
- **Decision**: Each log entry contains exactly three fields. No task context is captured alongside the mood.
- **Rationale**: Summarizing task context would require a secondary inference step that could influence the model's mood state and violate the non-interference principle.
- **Source**: archive/cycles/001/decision-log.md (DL7); steering/interview.md Q6
- **Status**: settled

## D-2: JSONL format with one entry per line
- **Decision**: Mood log is a newline-delimited JSON file (`mood-log.jsonl`) stored inside the plugin directory. One JSON object per line.
- **Rationale**: Rationale not recorded; JSONL is specified as a hard constraint.
- **Source**: steering/constraints.md (C8)
- **Status**: settled

## D-3: session_id resolved from CLAUDE_SESSION_ID env var with "unknown" fallback
- **Decision**: write-log.sh uses `${CLAUDE_SESSION_ID:-unknown}`. If Claude Code does not export the variable, entries log `"unknown"` as session_id.
- **Rationale**: Most direct resolution path given available Claude Code environment. Fallback prevents log write failure.
- **Source**: archive/cycles/001/decision-log.md (DL13); plan/architecture.md (Design Tension #4)
- **Status**: settled — **fallback behavior degrades log quality** (see Q-1)
