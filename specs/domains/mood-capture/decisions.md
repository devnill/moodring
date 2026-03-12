# Decisions: Mood Capture

## D-1: Fixed 16-mood vocabulary spanning the valence-arousal space
- **Decision**: The mood palette is fixed at 16 labels organized across the valence-arousal space. The model selects freely from this set at each prompt.
- **Rationale**: A fixed vocabulary ensures consistent logging and sound mapping.
- **Source**: archive/cycles/001/decision-log.md (DL2); steering/interview.md Q3
- **Status**: settled

## D-2: Prompt hooks on all 18 lifecycle events; downgrade if specific events cause issues
- **Decision**: Start with prompt-type hooks on all 18 Claude Code lifecycle events. If specific events cause problems during testing, downgrade those to command-only hooks or remove them.
- **Rationale**: Maximum data capture principle. Cost of over-sampling is negligible compared to missing state transitions.
- **Source**: archive/cycles/001/decision-log.md (DL4, DL12); steering/guiding-principles.md GP-3
- **Status**: settled

## D-3: Prompt hook followed by command hook per event — sequential chain
- **Decision**: Each lifecycle event gets a prompt hook that elicits the mood label, followed by a command hook that runs mood-handler.sh. The architecture assumes the prompt hook's response is available in the stdin JSON passed to the subsequent command hook.
- **Rationale**: Most direct path from mood elicitation to sound dispatch within the Claude Code hook system. Alternatives rejected: model calling Bash tool directly (violates non-interference); background scraping (loses immediacy); external LLM API (requires different model instance).
- **Assumes**: Claude Code executes hooks within a group sequentially and passes prompt hook output to subsequent command hooks via stdin JSON.
- **Source**: archive/cycles/001/decision-log.md (DL5); plan/architecture.md (Design Tension #1)
- **Status**: settled — **assumption unvalidated** (see Q-1)

## D-4: Neutral forced-choice prompt framing
- **Decision**: The mood prompt uses neutral language: "If you had to assign a mood label from the following list to your current internal state, which would you choose?" with no suggestion that having emotions is expected or desirable.
- **Rationale**: Experimental neutrality is foundational. Any bias in the prompt invalidates the data.
- **Source**: archive/cycles/001/decision-log.md (DL6); steering/interview.md Q5
- **Status**: settled

## D-5: Accept approximate polling in the loop skill
- **Decision**: The /moodring:loop skill is model-driven. The poll interval is advisory, not a precise timer. Claude manages the loop via sleep between iterations.
- **Rationale**: Claude Code skills are markdown files that instruct the model. Precise timer enforcement is not possible within this system.
- **Source**: archive/cycles/001/decision-log.md (DL11); plan/architecture.md (Design Tension #5)
- **Status**: settled

## D-6: Loop skill prompt must include JSON response instruction
- **Decision**: The loop skill's mood prompt explicitly instructs the model to respond with JSON format `{"mood": "<label>"}`, matching the hook prompt format.
- **Rationale**: Without the JSON instruction, the loop skill produced free-form responses that mood-handler.sh could not parse.
- **Source**: archive/cycles/001/decision-log.md (DL23); archive/cycles/001/decision-log.md execution phase
- **Status**: settled
