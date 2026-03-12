# Decisions: Plugin Infrastructure

## D-1: Adopt beepboop plugin as structural template
- **Decision**: Moodring's plugin structure, hook configuration, shell scripts, and synth integration follow beepboop's established patterns.
- **Rationale**: Beepboop is a proven architecture for Claude Code audio plugins. Deviating without cause adds risk.
- **Source**: archive/cycles/001/decision-log.md (DL1); steering/guiding-principles.md GP-6
- **Status**: settled

## D-2: Expose only muted and poll_interval as v1 configuration
- **Decision**: settings.json exposes exactly two user-facing settings: muted (boolean) and poll_interval (duration string). volume and player are internal implementation fields.
- **Rationale**: Minimal configuration principle. Plugin should work out of the box.
- **Source**: archive/cycles/001/decision-log.md (DL9); steering/guiding-principles.md GP-7
- **Status**: settled

## D-3: Use grep -qwF (fixed-string matching) for mood label validation
- **Decision**: mood-handler.sh validates the mood label using `grep -qwF` (fixed-string, whole-word, quiet match).
- **Rationale**: Defense against regex injection on mood label input. A mood label containing regex metacharacters could otherwise escape validation.
- **Source**: archive/cycles/001/decision-log.md (DL19); archive/incremental/ work item 006
- **Status**: settled

## D-4: Add CLAUDE_PLUGIN_ROOT find-based fallback to config skill
- **Decision**: The config skill includes an explicit fallback: if `CLAUDE_PLUGIN_ROOT` is unset, locate the plugin root via `find`.
- **Rationale**: Skills may execute in contexts where the variable is not exported. Without the fallback, all path-dependent commands fail silently.
- **Source**: archive/cycles/001/decision-log.md (DL21); archive/cycles/001/code-quality.md (S1)
- **Status**: settled — **not yet propagated to loop skill** (see Q-1)

## D-5: Accept two spec documentation inconsistencies as documentation errors
- **Decision**: (a) architecture.md showing `commands/` instead of `skills/`; (b) synth.toml output_dir showing `"plugin/sounds"` instead of `"sounds"` — both are documentation errors. The implementation is correct.
- **Rationale**: Implementation followed the more specific documents (constraints.md, work items, generate.sh working directory). Architecture doc was written before the discrepancy was noticed.
- **Source**: archive/cycles/001/spec-adherence.md (D1, D2); archive/cycles/001/decision-log.md (DL24)
- **Status**: settled — **documentation not yet updated** (see Q-3)
