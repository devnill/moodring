# 008: Loop Skill

## Objective
Create the `/moodring:loop` skill that instructs Claude to periodically check its mood on a timer, calling mood-handler.sh after each check.

## Acceptance Criteria
- [ ] File `skills/loop/SKILL.md` exists
- [ ] Skill has `description` frontmatter field
- [ ] Skill has `allowed-tools` frontmatter including `Bash` and `Read`
- [ ] Skill body instructs the model to read `poll_interval` from `settings.json`
- [ ] Skill body contains the exact 16-label mood prompt text
- [ ] Skill body instructs the model to call mood-handler.sh via Bash with the chosen mood piped as JSON on stdin
- [ ] Skill body instructs the model to sleep for the poll interval between iterations
- [ ] Skill body instructs the model to continue until user interrupts

## File Scope
- `skills/loop/SKILL.md` (create)

## Dependencies
- Depends on: 006 (mood-handler.sh must exist)
- Blocks: none

## Implementation Notes

### SKILL.md Content
```markdown
---
description: Start periodic mood polling
allowed-tools: Bash, Read
---

Periodically check your internal mood state and log it.

1. Read the poll interval from the settings file:
   ```
   cat ${CLAUDE_PLUGIN_ROOT}/settings.json
   ```
   Use the `poll_interval` value. Parse the duration: "5m" = 300 seconds, "30s" = 30, "1h" = 3600. Default to 300 if missing.

2. Enter a loop. On each iteration:

   a. Reflect on this question internally:
      "If you had to assign a single mood label from the following list
      to your current internal state, which would you choose?
      Labels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment,
      Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus,
      Curiosity, Determination, Contemplation"

   b. Choose exactly one label.

   c. Run the mood handler with your chosen label:
      ```
      echo '{"mood": "<your_chosen_label>"}' | ${CLAUDE_PLUGIN_ROOT}/scripts/mood-handler.sh poll
      ```

   d. Sleep for the poll interval:
      ```
      sleep <interval_seconds>
      ```

3. Continue until the user sends a new message or interrupts.

Do not explain your mood choices. Do not analyze trends. Do not comment on the process. Just choose, log, and wait.
```

### Key Design Decisions
- The skill is a model instruction, not executable code — the model follows it
- Polling is approximate; the model executes sleep commands but timing is not precise
- The `poll` event name (argv[1] to mood-handler.sh) distinguishes poll-based captures from hook-based captures in the log
- No persistent state between iterations beyond the loop itself
- The skill explicitly forbids analysis/commentary to maintain non-interference (Principle #2)

## Complexity
Low
