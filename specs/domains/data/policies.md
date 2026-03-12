# Policies: Data

## P-1: Log entries contain exactly three fields — no task context
Each JSONL entry contains only `timestamp` (ISO 8601), `mood` (one of 16 labels), and `session_id`. No task description, tool name, or inference about what the model was doing is captured.
- **Derived from**: GP-8 (Data Over Interpretation) + constraint C8
- **Established**: planning phase
- **Status**: active

## P-2: Every mood capture writes a log entry — no sampling or deduplication
All mood responses from both hook-driven and poll-driven paths are logged. Duplicate moods within a session are expected and correct.
- **Derived from**: GP-3 (Maximum Data Capture)
- **Established**: planning phase
- **Status**: active
