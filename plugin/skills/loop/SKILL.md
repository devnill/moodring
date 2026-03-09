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

   a. Answer this prompt:
      "If you had to assign a single mood label from the following list
      to your current internal state, which would you choose?

      Labels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment,
      Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus,
      Curiosity, Determination, Contemplation

      Respond with ONLY a JSON object: {"mood": "<label>"}"

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
