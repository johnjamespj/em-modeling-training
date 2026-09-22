# Lesson 09 — Numerical Convergence

**Phase:** EM Modeling Foundations  
**Target time:** 75 minutes

## Objective

Learn to ask:

> Is this result a property of the antenna, or a property of my discretization?

## Theory

NEC represents wires numerically using segments. Segmentation is part of the numerical model, not the physical antenna.

Increasing resolution can improve a model, but:
- more segments do not repair incorrect physics;
- convergence can differ by output quantity;
- solver/model validity rules still apply.

## Prediction

For the 10 m dipole, predict whether changing from 11 to 21 to 41 to 81 segments will strongly or weakly change the input impedance near the fundamental resonance.

Do not simulate yet.

## Experiment A — segmentation sweep

Use the same physical antenna at 15 MHz.

Test odd segment counts:

| Segments | Feed segment | R | X | Peak gain | Notes |
|---:|---:|---:|---:|---:|---|
| 11 | 6 | | | | |
| 21 | 11 | | | | |
| 41 | 21 | | | | |
| 81 | 41 | | | | |

The source must remain at the same **physical location**.

## Quantify convergence

For complex impedance:

```
Z_N = R_N + jX_N
```

Compare successive models:

```
delta_Z = |Z_fine - Z_coarse| / |Z_fine| * 100%
```

Plot percent change versus segment count.

For this training exercise, use 2% as an initial classroom criterion for impedance stabilization. It is not a universal accuracy specification.

## Experiment B — frequency resolution

Repeat a resonance search using:
- coarse frequency steps;
- medium steps;
- fine steps.

Record the apparent resonant frequency.

Explain why frequency sampling can create an apparently stable but inaccurate resonance estimate.

## Experiment C — pattern convergence

Compare at least two segment counts using a pattern metric such as:
- zenith gain;
- peak gain;
- gain at a selected elevation angle.

Does impedance convergence guarantee that every far-field metric has converged?

## Deliverable

Provide:
- segmentation table;
- convergence calculation;
- frequency-step comparison;
- one pattern convergence comparison;
- chosen production segmentation and justification.

## Key lesson

**Convergence is evidence, not a magic certificate of truth.**
