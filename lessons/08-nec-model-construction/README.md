# Lesson 08 — NEC/xnec2c Model Construction

**Phase:** EM Modeling Foundations  
**Target time:** 75–90 minutes

## Objective

Build a complete NEC model from a blank file and explain every modeling choice.

By the end, you should be able to:
- define wire geometry and coordinates;
- choose a sensible segmentation;
- place a source correctly;
- configure a frequency sweep;
- request radiation-pattern data;
- distinguish physical parameters from numerical parameters;
- document assumptions before trusting results.

## Part 1 — Start from paper

Do not copy an existing NEC file.

Design a center-fed 10 m dipole in free space. Before opening xnec2c, write down:

- coordinate system;
- wire endpoints;
- radius;
- number of segments;
- center segment;
- frequency range;
- source definition;
- requested outputs.

Sketch the geometry with labeled axes.

## Part 2 — NEC anatomy

Identify the role of the cards used in the baseline model:

- `GW` — wire geometry;
- `GE` — end geometry input;
- `EX` — excitation;
- `FR` — frequency;
- `RP` — radiation-pattern request;
- `EN` — end.

For every line in your model, add a comment in your lab notes explaining what it controls.

## Part 3 — Build from blank

Create:

```
work/lesson08/my-first-model.nec
```

Requirements:
- 10 m straight wire;
- 1 mm radius;
- odd segment count;
- source on the physical center segment;
- free-space environment;
- frequency sweep containing the fundamental resonance.

Run it.

## Part 4 — Sanity checks

Before accepting any plot, verify:

1. Is the antenna where you think it is?
2. Are the dimensions in the expected units?
3. Is the feed at the center?
4. Is the frequency range correct?
5. Is the pattern coordinate system understood?
6. Did the solver report warnings?
7. Does the approximate resonant region agree with a wavelength estimate?

## Part 5 — Change one thing incorrectly

Move the source one or more segments away from center without changing anything else.

Compare:
- input impedance;
- current distribution;
- pattern symmetry.

Explain why the output changed.

Then restore the correct model.

## Deliverable

Submit:
- your NEC file;
- geometry sketch;
- annotated explanation of each NEC card;
- baseline impedance plot;
- baseline pattern;
- one deliberately incorrect-feed result;
- a short statement of assumptions.

## Rule

A model file without documented geometry, excitation, environment, and numerical settings is not a complete engineering artifact.
