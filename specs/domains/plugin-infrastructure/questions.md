# Questions: Plugin Infrastructure

## Q-1: Loop skill lacks CLAUDE_PLUGIN_ROOT fallback that config skill has
- **Question**: Should the find-based CLAUDE_PLUGIN_ROOT fallback from the config skill be copied into the loop skill?
- **Source**: archive/cycles/001/code-quality.md (S1); archive/cycles/001/decision-log.md (OQ1, CR1)
- **Impact**: Loop skill Bash commands fail silently when CLAUDE_PLUGIN_ROOT is unset. Supplementary polling path becomes non-functional.
- **Status**: open
- **Reexamination trigger**: Start of cycle 2 — low-complexity fix, copy the pattern from config skill.

## Q-2: No README exists
- **Question**: Should a README.md be added? If so, what audience and scope?
- **Source**: archive/cycles/001/gap-analysis.md (MI1); archive/cycles/001/summary.md
- **Impact**: Plugin is not self-documenting. Users discovering it have no installation, configuration, or usage guidance.
- **Status**: open
- **Reexamination trigger**: When preparing to share or publish the plugin.

## Q-3: Documentation inconsistencies unresolved — architecture.md, build.md, playback.md
- **Question**: Should architecture.md, build.md, and playback.md be updated to match the implemented behavior?
- **Source**: archive/cycles/001/spec-adherence.md (R1, R2, R3); archive/cycles/001/decision-log.md (OQ4)
- **Impact**: Future contributors receive incorrect information about directory layout, output_dir, and missing-settings behavior.
- **Status**: open
- **Reexamination trigger**: Cycle 2 refinement — low-complexity documentation updates.

## Q-4: No .gitignore; __pycache__ already committed
- **Question**: Should a .gitignore be added and __pycache__ removed from tracking?
- **Source**: archive/cycles/001/gap-analysis.md (MI2); archive/cycles/001/code-quality.md (M1)
- **Impact**: Build artifacts accumulate in the repository. __pycache__ is already present.
- **Status**: open
- **Reexamination trigger**: Cycle 2 refinement — standard infrastructure, low effort.
