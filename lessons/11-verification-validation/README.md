# Lesson 11 — Verification, Validation, and Model Credibility

**Phase:** EM Modeling Foundations  
**Target time:** 90 minutes

## Objective

Learn the most important modeling distinction in the course:

> A solver can accurately solve the wrong problem.

## Three layers of confidence

### 1. Physics sanity

Does the result agree with basic expectations?

Examples:
- approximate half-wave resonance;
- expected current symmetry;
- plausible pattern orientation;
- conservation/power-accounting checks where applicable.

### 2. Numerical verification

Did we solve the selected mathematical/numerical model adequately?

Examples:
- segmentation convergence;
- frequency-step convergence;
- solver warnings;
- stable reported metrics.

### 3. Physical validation

Does the model represent the real system well enough for the intended decision?

Examples:
- geometry;
- materials;
- ground;
- feed structure;
- nearby conductors;
- losses;
- measurement comparison.

## Broken-model laboratory

Start from a trusted baseline.

Create four variants.

### A — Coarse discretization
Use intentionally weak segmentation.

### B — Wrong geometry
Introduce a dimension error.

### C — Wrong environment
Use free space for a case intended to represent an antenna near ground.

### D — Wrong excitation
Move or alter the source.

For each case record:

| Case | Plot looks plausible? | Numerical issue? | Physical issue? | How detected? |
|---|---|---|---|---|
| Baseline | | | | |
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |

## Important experiment

Take one physically wrong model and refine its segmentation until its numerical result is highly stable.

Answer:

> What did convergence prove?

Expected idea: it demonstrated stability of the numerical solution to the chosen model. It did not prove the physical model represented reality.

## Independent checks

For the baseline, use at least two:
- hand wavelength estimate;
- known qualitative dipole pattern;
- independent calculation;
- alternate solver later in the course;
- measurement when hardware becomes available.

## Model credibility statement

Write one page containing:

### Purpose
What engineering question is the model intended to answer?

### Physical assumptions
What real effects are represented or omitted?

### Numerical evidence
What convergence checks were performed?

### Sanity checks
What independent physics expectations were checked?

### Limitations
What conclusions should **not** be drawn?

### Validation status
What measurement or independent model would increase confidence?

## Phase II gate

Before moving to HF/NVIS modeling, the trainee must demonstrate that they can:

1. build a NEC model from blank;
2. explain each important model input;
3. maintain physical source position during mesh changes;
4. perform segmentation convergence;
5. test frequency resolution;
6. run controlled parameter sweeps;
7. calculate a sensitivity;
8. distinguish verification from validation;
9. identify a plausible-looking bad model;
10. write a defensible model credibility statement.

Passing means the trainee can defend **why a simulation should be trusted for a stated purpose**, not merely reproduce a plot.
