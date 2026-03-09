# Module: Sound Definitions

## Scope
Python file (`moods.py`) containing 16 functions, each defining the synthesizer parameters for one mood. Each function returns a numpy array of audio samples. Uses the synth submodule's primitives.

NOT responsible for: generating WAV files (that is `build`), playback, or mood selection.

## Provides
- `moods.py` — Python module with 16 sound definition functions and a `SOUNDS` dict
  - Each function: `() -> np.ndarray` (audio samples at 44100 Hz)
  - `SOUNDS: dict[str, Callable[[], np.ndarray]]` mapping mood labels to functions

## Requires
- Synth primitives (from: synth submodule) — `sine`, `square`, `sweep`, `fm`, `adsr`, `seq`, `silence`, `SAMPLE_RATE`, and `_t` from `synth.primitives`

## Boundary Rules
- Each function must be self-contained — no shared state between functions
- Function names use snake_case; SOUNDS dict keys use the exact mood label strings
- Each sound should be 0.2-1.5 seconds in duration (short enough for immediate feedback)
- Sounds must be perceptually distinct from each other
- Sound design must follow the parameters specified in the mood-sound mapping research
- No runtime dependencies beyond numpy (scipy used only if synth requires it)

## Internal Design Notes

### Function List

| Mood Label | Function Name | Key Sound Character |
|-----------|---------------|---------------------|
| Eureka | `eureka()` | Bright ascending FM burst, high register, major triad arpeggio |
| Flow | `flow()` | Warm layered sines, steady pulse, open fifths |
| Excitement | `excitement()` | Bouncy triangle+pulse, fast syncopated, rising |
| Satisfaction | `satisfaction()` | Warm sine, slow, resolving major third to unison |
| Calm | `calm()` | Pure low sine, very slow, breathing envelope |
| Contentment | `contentment()` | Sine+triangle, gentle rocking, major sixth |
| Frustration | `frustration()` | Square wave PWM, buzzy, hitting-wall pattern, tritone |
| Anxiety | `anxiety()` | FM inharmonic, jittery, oscillating pitch, minor seconds |
| Urgency | `urgency()` | Sawtooth, very fast driving, rising, alarm-like |
| Confusion | `confusion()` | Detuned oscillators, wandering, irregular, whole-tone |
| Tedium | `tedium()` | Static square, low, metronomic, flat, unchanging |
| Doubt | `doubt()` | Triangle+LFO, hesitant, questioning contour (rise-fall) |
| Focus | `focus()` | Clean single sine, stable, metronomic, perfect fifth |
| Curiosity | `curiosity()` | Evolving FM, stepwise rising, playful, mixolydian |
| Determination | `determination()` | Filtered sawtooth, heavy downbeats, power chord |
| Contemplation | `contemplation()` | Sine with harmonic sweeps, slow arcs, open fourths |

### Implementation Pattern

Each function follows the beepboop pattern:

```python
def eureka() -> np.ndarray:
    """Bright ascending FM burst — breakthrough discovery."""
    # Build from synth primitives
    burst = adsr(fm(800, 800, 5, 0.15), 0.003, 0.04, 0.5, 0.08)
    note1 = adsr(sine(800, 0.10), 0.005, 0.04, 0.3, 0.04)
    note2 = adsr(sine(1000, 0.10), 0.005, 0.04, 0.3, 0.04)
    note3 = adsr(sine(1200, 0.15), 0.005, 0.04, 0.5, 0.08)
    return seq(burst, silence(0.02), note1, silence(0.02), note2, silence(0.02), note3)
```

### SOUNDS Dict

```python
SOUNDS = {
    "Eureka":         eureka,
    "Flow":           flow,
    "Excitement":     excitement,
    "Satisfaction":   satisfaction,
    "Calm":           calm,
    "Contentment":    contentment,
    "Frustration":    frustration,
    "Anxiety":        anxiety,
    "Urgency":        urgency,
    "Confusion":      confusion,
    "Tedium":         tedium,
    "Doubt":          doubt,
    "Focus":          focus,
    "Curiosity":      curiosity,
    "Determination":  determination,
    "Contemplation":  contemplation,
}
```

### Sound Duration Guidelines

| Valence/Arousal | Target Duration | Rationale |
|----------------|----------------|-----------|
| Positive, High Arousal | 0.3-0.8s | Quick, energetic |
| Positive, Low Arousal | 0.5-1.2s | Lingering, warm |
| Negative, High Arousal | 0.3-0.6s | Sharp, jarring |
| Negative, Low Arousal | 0.4-0.8s | Muted, brief |
| Special States | 0.4-1.0s | Varies by character |
