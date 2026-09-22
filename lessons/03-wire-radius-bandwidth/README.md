# Lesson 3: Wire Radius, Q, and Bandwidth

**Target time:** 45 minutes

## Objective
Explore how conductor geometry affects impedance behavior and bandwidth.

## Prediction
Keep dipole length fixed and change only wire radius. Predict whether a thicker conductor produces a narrower or broader impedance response.

## Experiment
Use the same nominal 10 m dipole and sweep a frequency range wide enough to see the impedance change.

Try representative radii:

| Radius | Resonant frequency | Min VSWR | Approx. 2:1 VSWR bandwidth |
|---:|---:|---:|---:|
| 0.5 mm | | | |
| 1 mm | | | |
| 5 mm | | | |
| 20 mm | | | |

Do not compare bandwidth until you confirm each model is numerically reasonable.

## Questions
1. Does radius affect only loss?
2. Did resonance move?
3. How did the slope of reactance near resonance change?
4. What happened to usable bandwidth?
5. Why can an electrically thicker antenna have different bandwidth behavior?

## Modeling caution
NEC wire models have geometric validity constraints. Extremely large wire radii relative to segment length or geometry can make a model invalid even if the solver produces numbers.

## Deliverable
Provide impedance/VSWR plots, the completed table, and a short explanation connecting geometry to bandwidth.
