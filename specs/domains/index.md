# Domain Registry

current_cycle: 1

## Domains

### mood-capture
The experimental core: mood vocabulary, prompt design, neutrality constraints, hook mechanism for eliciting mood labels, and polling. Covers both the 18-event hook chain and the /moodring:loop polling path.
Files: domains/mood-capture/policies.md, decisions.md, questions.md

### audio
Sound design, synthesis definitions, build-time WAV generation via synth tool, and runtime playback via afplay. Covers moods.py, generate.sh, the synth submodule, and play-sound.sh.
Files: domains/audio/policies.md, decisions.md, questions.md

### data
JSONL log schema, session identity, log write mechanics, and data quality. Covers mood-log.jsonl, write-log.sh, and the session_id resolution strategy.
Files: domains/data/policies.md, decisions.md, questions.md

### plugin-infrastructure
Claude Code plugin structure, hook configuration, shell script conventions, settings schema, skills (loop and config), and repository hygiene. The beepboop conformance layer.
Files: domains/plugin-infrastructure/policies.md, decisions.md, questions.md

## Cross-Cutting Concerns

**Hook data-passing (mood-capture Q-1 + plugin-infrastructure)**: The entire event-driven architecture depends on prompt hook output being available in command hook stdin. This assumption spans both the mood-capture domain (where the prompt runs) and the plugin-infrastructure domain (where hooks.json is configured). If it fails, remediation touches both domains.

**CLAUDE_PLUGIN_ROOT asymmetry (plugin-infrastructure Q-1)**: The config skill has the fallback; the loop skill does not. Fixing the loop skill is infrastructure work but the root cause is shared execution environment assumptions that affect both skills.

**Documentation drift (plugin-infrastructure Q-3)**: Three architecture/module docs contradict the implementation. Updates touch plan/architecture.md, plan/modules/build.md, and plan/modules/playback.md — outside the domains/ layer but tracked here for traceability.
