# EM Modeling Training

A hands-on introduction to electromagnetic modeling for engineers using Linux and **xnec2c/NEC2**.

The goal is not to teach button-clicking. Every lesson follows the engineering loop:

1. Predict the physics.
2. Build the model.
3. Run the simulation.
4. Check whether the result makes physical sense.
5. Perturb the model.
6. Test numerical convergence.
7. State what the model does and does not prove.

## Course path

| Lesson | Topic | Main idea |
|---|---|---|
| [1](lessons/01-dipole-basics/README.md) | Half-wave dipole | Resonance, impedance, pattern, convergence |
| [2](lessons/02-ground-effects/README.md) | Ground effects | The environment is part of the antenna |
| [3](lessons/03-wire-radius-bandwidth/README.md) | Radius & bandwidth | Geometry changes electrical behavior |
| [4](lessons/04-feed-and-matching/README.md) | Feed & matching | Resonance is not the same as matching |
| [5](lessons/05-parameter-sweeps/README.md) | Sensitivity | Turn simulations into engineering experiments |
| [6](lessons/06-two-element-array/README.md) | Two-element array | Phase and spacing shape beams |
| [7](lessons/07-mutual-coupling/README.md) | Mutual coupling | Nearby antennas are not independent |
| [8](lessons/08-model-validation/README.md) | Model credibility | Verification, validation, and limitations |

Finish with the [Final Challenge](exercises/final-challenge.md).

## Suggested progression

Lessons 1–4 build fundamentals. Lessons 5–7 develop engineering analysis habits. Lesson 8 is deliberately solver-agnostic and focuses on deciding whether simulation evidence deserves trust.

## Linux setup

See [setup/linux-xnec2c.md](setup/linux-xnec2c.md).

## Expected background

Basic circuits, complex impedance, and introductory electromagnetics are useful. No prior EM-solver experience is required.

## Modeling rule

**Never trust a plot just because it looks smooth.** A converged answer to the wrong physical model is still the wrong answer.
