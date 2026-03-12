# Questions: Mood Capture

## Q-1: Hook data-passing assumption is unvalidated
- **Question**: Does Claude Code pass the output of a prompt-type hook as stdin to a subsequent command-type hook in the same event group?
- **Source**: archive/cycles/001/gap-analysis.md (II1); archive/cycles/001/decision-log.md (OQ2); plan/architecture.md (Design Tension #1)
- **Impact**: If the assumption does not hold, mood-handler.sh receives empty stdin on all 18 events — no moods are captured, no sounds play, no logs are written. The loop skill continues to work but the primary 18-event path fails silently. Total primary-path failure.
- **Status**: open
- **Reexamination trigger**: Before marking cycle 2 complete. This is the highest-priority item in the refinement plan.
