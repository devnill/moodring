# Module: Hook Configuration

## Scope
Defines the `hooks/hooks.json` file that maps Claude Code hook events to prompt-type and command-type hooks. Each hookable event gets a two-hook chain: a prompt hook to elicit the mood label, followed by a command hook to handle the response.

NOT responsible for: the prompt text itself (that comes from `mood-prompt`), the handler logic (that comes from `mood-handler`), or settings.

## Provides
- `hooks.json` — Hook configuration file at `hooks/hooks.json`

## Requires
- Mood prompt text (from: `mood-prompt`) — The exact prompt string to embed in each prompt hook
- `mood-handler.sh` path (from: `mood-handler`) — The script path for command hooks

## Boundary Rules
- Every hookable Claude Code event gets a hook entry
- Each entry contains a prompt hook followed by a command hook, in a single hook group
- Prompt hooks use `"type": "prompt"` with the mood capture prompt
- Command hooks use `"type": "command"` invoking `mood-handler.sh`
- Timeout for prompt hooks should be generous (10-15s) to allow model inference
- Timeout for command hooks should be short (5s) — just playback and logging
- Uses `${CLAUDE_PLUGIN_ROOT}` for script paths (same as beepboop)

## Internal Design Notes

### Hook Events to Configure

All hookable events from the beepboop reference, each getting a prompt+command pair:

| Event | Notes |
|-------|-------|
| SessionStart | First mood capture of the session |
| UserPromptSubmit | Mood when user gives new input |
| PreToolUse | Mood before executing a tool |
| PostToolUse | Mood after tool execution |
| PostToolUseFailure | Mood after a failed tool call |
| PermissionRequest | Mood when waiting for permission |
| Notification | Mood on notification events |
| SubagentStart | Mood when spawning a subagent |
| SubagentStop | Mood when a subagent finishes |
| Stop | Mood when the model stops |
| TeammateIdle | Mood on teammate idle |
| TaskCompleted | Mood on task completion |
| InstructionsLoaded | Mood after loading instructions |
| ConfigChange | Mood on config change |
| WorktreeCreate | Mood on worktree creation |
| WorktreeRemove | Mood on worktree removal |
| PreCompact | Mood before context compaction |
| SessionEnd | Final mood of the session |

### Hook Structure Pattern

Each event follows this pattern:

```json
{
  "EventName": [
    {
      "hooks": [
        {
          "type": "prompt",
          "prompt": "<mood capture prompt text>",
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
}
```

### Design Concern: Prompt-to-Command Data Flow

The two-hook chain assumes the command hook receives the prompt hook's response in its stdin context. If this assumption proves false during implementation, the fallback is to restructure so that the prompt hook instructs the model to include a tool call to `mood-handler.sh`. See architecture.md Design Tension #1.
