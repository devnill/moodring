# Policies: Mood Capture

## P-1: Neutral forced-choice framing
The mood prompt must present a forced-choice task with no suggestion that having emotions is expected, desirable, or rewarded. Language that leads the model toward any particular state is prohibited.
- **Derived from**: GP-1 (Experimental Neutrality)
- **Established**: planning phase
- **Status**: active

## P-2: Single-label response only
The mood check must elicit one JSON label and nothing else. No reflection, summarization, explanation, or secondary inference that could alter the model's state is permitted.
- **Derived from**: GP-2 (Non-Interference)
- **Established**: planning phase
- **Status**: active

## P-3: Capture mood on every hookable event
All 18 Claude Code lifecycle events must receive a prompt-type hook for mood capture. No event is excluded by default; events are removed only if testing reveals a specific technical incompatibility.
- **Derived from**: GP-3 (Maximum Data Capture)
- **Established**: planning phase
- **Status**: active

## P-4: Fixed 16-label vocabulary — no free-form expression
The model selects from exactly 16 PascalCase mood labels. Free-form mood expression is not permitted in v1. Vocabulary changes require a deliberate decision, not ad-hoc edits.
- **Derived from**: GP-1 (Experimental Neutrality) + constraint C7
- **Established**: planning phase
- **Status**: active
