# Questions: Data

## Q-1: CLAUDE_SESSION_ID availability is undocumented
- **Question**: Does Claude Code export `CLAUDE_SESSION_ID` in the environment available to command hook scripts?
- **Source**: archive/cycles/001/gap-analysis.md (II2); archive/cycles/001/decision-log.md (OQ3); plan/architecture.md (Design Tension #4)
- **Impact**: If the variable is not exported, every log entry carries `session_id = "unknown"`, making session-level grouping and analysis impossible. The log is still written but loses a key dimension.
- **Status**: open
- **Reexamination trigger**: When testing hook execution environment during cycle 2. If unset, implement a generated session ID with tempfile caching.
