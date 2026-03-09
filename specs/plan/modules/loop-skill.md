# Module: Loop Skill

## Scope
Defines the `/moodring:loop` slash command that starts periodic mood polling. This is a Claude Code skill (markdown file) that instructs the model to repeatedly check its mood on a timer.

NOT responsible for: the mood prompt text (uses the canonical prompt from `mood-prompt`), sound playback, or log writing (those are triggered via `mood-handler`).

## Provides
- `loop.md` — Skill definition at `commands/loop.md`
  - Slash command: `/moodring:loop`
  - Behavior: Starts a polling loop that periodically captures mood

## Requires
- Mood prompt text (from: `mood-prompt`) — The prompt to present to itself on each poll
- `mood-handler.sh` (from: `mood-handler`) — Called via Bash tool after each mood response
- `settings.json` (from: `settings`) — Read for `poll_interval`

## Boundary Rules
- The skill instructs the model; it does not execute code directly
- Polling is approximate — the model follows timing instructions but is not a precise timer
- The loop must be interruptible (user can type to stop it)
- Must read `poll_interval` from settings at loop start
- Must use the canonical mood prompt (same as hooks use)
- Must call `mood-handler.sh` after each mood self-assessment
- Must not perform any analysis of mood trends or patterns

## Internal Design Notes

### Skill Definition (commands/loop.md)

```markdown
---
description: Start periodic mood polling
allowed-tools: Bash, Read
---

Periodically check your internal mood state and log it.

1. Read the poll interval from the settings file:
   ```bash
   cat ${CLAUDE_PLUGIN_ROOT}/settings.json
   ```
   Use the `poll_interval` value (default "5m" = 300 seconds).

2. Enter a loop. On each iteration:

   a. Reflect on this question internally:
      "If you had to assign a single mood label from the following list
      to your current internal state, which would you choose?
      Labels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment,
      Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus,
      Curiosity, Determination, Contemplation"

   b. Choose exactly one label.

   c. Run the mood handler with your chosen label:
      ```bash
      echo '{"mood": "<your_chosen_label>"}' | ${CLAUDE_PLUGIN_ROOT}/scripts/mood-handler.sh poll
      ```

   d. Sleep for the poll interval:
      ```bash
      sleep <interval_seconds>
      ```

3. Continue until the user sends a new message or interrupts.

Do not explain your mood choices. Do not analyze trends. Just choose, log, and wait.
```

### Interval Parsing

The skill instructs the model to parse the interval string. Common formats:
- `"5m"` -> 300 seconds
- `"30s"` -> 30 seconds
- `"1h"` -> 3600 seconds

The model handles this parsing as part of following the skill instructions.

### Interruption

When the user types a new message, Claude Code interrupts the model's current activity. The sleep command is killed, and the model processes the user's input. The loop does not resume automatically — the user must re-invoke `/moodring:loop`.
