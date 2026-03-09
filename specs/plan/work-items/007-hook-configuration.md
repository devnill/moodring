# 007: Hook Configuration

## Objective
Create `hooks/hooks.json` with prompt-type and command-type hooks for every Claude Code lifecycle event, implementing the two-hook chain that captures mood and dispatches handling.

## Acceptance Criteria
- [ ] File `hooks/hooks.json` exists and is valid JSON
- [ ] Every hookable event has an entry: SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, Notification, SubagentStart, SubagentStop, Stop, TeammateIdle, TaskCompleted, InstructionsLoaded, ConfigChange, WorktreeCreate, WorktreeRemove, PreCompact, SessionEnd
- [ ] Each event entry contains a hook group with a prompt-type hook followed by a command-type hook
- [ ] Each prompt hook has `"type": "prompt"` and contains the exact mood capture prompt text
- [ ] The prompt text lists all 16 mood labels and requests JSON response format `{"mood": "<label>"}`
- [ ] Each command hook has `"type": "command"` and invokes `${CLAUDE_PLUGIN_ROOT}/scripts/mood-handler.sh <EventName>`
- [ ] Prompt hooks have `"timeout": 15`
- [ ] Command hooks have `"timeout": 5`

## File Scope
- `hooks/hooks.json` (create)

## Dependencies
- Depends on: 006 (mood-handler.sh must exist at the referenced path)
- Blocks: none

## Implementation Notes

### Hook Structure Pattern
Each event follows this structure:
```json
"EventName": [
  {
    "hooks": [
      {
        "type": "prompt",
        "prompt": "If you had to assign a single mood label from the following list to your current internal state, which would you choose?\n\nLabels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment, Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus, Curiosity, Determination, Contemplation\n\nRespond with ONLY a JSON object: {\"mood\": \"<label>\"}",
        "timeout": 15
      },
      {
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/scripts/mood-handler.sh EventName",
        "timeout": 5
      }
    ]
  }
]
```

### 18 Events
Repeat the pattern for all 18 events. The only variation is the event name passed as argv[1] to mood-handler.sh.

### Prompt Text
The prompt text is identical across all events. It is the canonical prompt from the mood-prompt module spec:
```
If you had to assign a single mood label from the following list to your current internal state, which would you choose?

Labels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment, Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus, Curiosity, Determination, Contemplation

Respond with ONLY a JSON object: {"mood": "<label>"}
```

### Design Tension #1 Fallback
If testing reveals that command hooks do not receive prompt hook responses in their stdin, the fallback is to remove the command hooks and modify the prompt to instruct the model to call the mood-handler script via Bash tool. This would change the prompt to:
```
... After choosing, run this command with your chosen label:
echo '{"mood": "<label>"}' | ${CLAUDE_PLUGIN_ROOT}/scripts/mood-handler.sh <EventName>
```
This fallback should only be implemented if the two-hook chain does not work.

## Complexity
Medium
