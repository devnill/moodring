# Policies: Plugin Infrastructure

## P-1: Plugin structure must conform to Claude Code plugin layout following beepboop
Directory layout, hook configuration, shell scripts, and synth integration follow the established beepboop plugin patterns. Deviate only when Moodring's requirements demand it.
- **Derived from**: GP-6 (Follow Beepboop Pattern) + constraint C3
- **Established**: planning phase
- **Status**: active

## P-2: v1 configuration is limited to muted and poll_interval
settings.json exposes exactly two user-facing settings. No additional configurability is added to v1 without a deliberate decision to extend scope.
- **Derived from**: GP-7 (Minimal Configuration)
- **Established**: planning phase
- **Status**: active

## P-3: Runtime shell scripts must guard against unset CLAUDE_PLUGIN_ROOT
Any shell script that references `${CLAUDE_PLUGIN_ROOT}` must include the find-based fallback path resolution pattern established in the config skill.
- **Derived from**: GP-6 (Follow Beepboop Pattern) — derived from execution-phase finding
- **Established**: execution phase (DL21)
- **Status**: active
