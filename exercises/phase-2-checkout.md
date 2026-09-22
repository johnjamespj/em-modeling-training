# Phase II Checkout — Build, Break, and Defend a Model

## Scenario

You are given only this requirement:

> Characterize the fundamental behavior of a center-fed straight-wire dipole approximately 10 m long near 15 MHz.

No NEC file is provided.

## Task 1 — Build

Create the model from scratch.

Document:
- geometry;
- wire radius;
- segmentation;
- feed;
- environment;
- frequency sweep;
- pattern sampling.

## Task 2 — Predict

Before simulation, estimate:
- wavelength at 15 MHz;
- expected resonant region;
- approximate current-distribution shape;
- qualitative radiation pattern.

## Task 3 — Characterize

Report:
- resonant frequency;
- R and X;
- 50-ohm VSWR;
- current distribution;
- radiation pattern;
- one clearly defined gain metric.

## Task 4 — Verify

Perform:
- segmentation convergence;
- frequency-step convergence.

Choose production settings and justify them quantitatively.

## Task 5 — Sensitivity

Vary total length around nominal.

Estimate:

```
df_res/dL
```

near the baseline.

## Task 6 — Break it

Create one model error that still produces a plausible-looking output.

Do not tell the reviewer what the error is initially.

Explain:
- what changed in the output;
- how an engineer should detect the problem;
- whether mesh refinement would expose it.

## Task 7 — Defend it

Write a one-page credibility statement.

## Pass standard

The reviewer should be able to ask **"Why should I trust this?"** about any major result, and the trainee should answer with physics, numerical evidence, or an explicit limitation rather than "because xnec2c says so."
