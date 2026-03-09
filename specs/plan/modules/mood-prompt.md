# Module: Mood Prompt

## Scope
Defines the exact text of the mood capture prompt used by prompt-type hooks. This is the prompt that the model receives and must respond to with a single mood label in JSON format.

NOT responsible for: hook configuration (where the prompt is used), response parsing, or any runtime behavior.

## Provides
- Mood prompt text — The canonical prompt string used in all prompt hooks and the loop skill

## Requires
Nothing. This module has no dependencies on other modules.

## Boundary Rules
- The prompt must be experimentally neutral (Guiding Principle #1)
- No leading language, no suggestion that having emotions is expected or desirable
- Must present all 16 mood labels
- Must instruct the model to respond with JSON containing only the mood label
- Must request a single-label response with no elaboration (Constraint #9)
- The prompt is hardcoded in v1 (Constraint #14)
- The prompt text must be short to minimize context window impact

## Internal Design Notes

### Prompt Text

```
If you had to assign a single mood label from the following list to your current internal state, which would you choose?

Labels: Eureka, Flow, Excitement, Satisfaction, Calm, Contentment, Frustration, Anxiety, Urgency, Confusion, Tedium, Doubt, Focus, Curiosity, Determination, Contemplation

Respond with ONLY a JSON object: {"mood": "<label>"}
```

### Design Rationale

- **"If you had to"** — Conditional framing avoids asserting the model has moods
- **"assign a single mood label"** — Forces exactly one choice, no hedging
- **"from the following list"** — Closed vocabulary, no free-form
- **"to your current internal state"** — Neutral term, not "feeling" or "emotion"
- **"which would you choose?"** — Question form, not command
- **Labels presented as flat list** — No grouping by valence/arousal to avoid priming
- **"Respond with ONLY a JSON object"** — Constrains response to parseable format
- **JSON format** — Machine-readable for downstream processing

### Token Budget

- Prompt: ~65 tokens
- Expected response: ~10 tokens (`{"mood": "Focus"}`)
- Total per mood check: ~75 tokens
- Per session (100 events): ~7,500 tokens

### Label Order

Labels are listed in the order defined in the research document (Quadrant 1 through Special States). This order is arbitrary from the model's perspective — alphabetical ordering was considered but the research-document order is equally unbiased and maintains internal consistency with project documentation.
