# Lesson 17 — Mutual Coupling

**Phase:** HF/NVIS Engineering  
**Target time:** 90 minutes

## Objective

Understand why adding another conductor can change the behavior of the antenna you thought you already understood.

## Theory intuition

A driven element produces fields.

Nearby conductors respond to those fields, producing induced currents.

Those currents produce additional fields that act back on the driven structure.

Consequences can include changes in:
- input impedance;
- current distribution;
- radiation pattern;
- polarization;
- bandwidth.

## Lab A — two parallel dipoles

Use two similar dipoles.

Vary spacing:

```
0.1 lambda
0.25 lambda
0.5 lambda
1.0 lambda
```

Excite the intended driven structure consistently.

Record:

| Spacing | Driven R | Driven X | Induced-current observation | Pattern change |
|---:|---:|---:|---|---|
| | | | | |

## Lab B — crossed conductors

Compare:
- one sloping dipole;
- crossed/sloping geometry.

Inspect current on both structures.

Does the second structure remain electromagnetically invisible simply because it is not independently driven?

## Lab C — frequency

Hold physical geometry fixed and compare coupling behavior at several frequencies.

Explain why fixed spacing in meters becomes different spacing in wavelengths.

## Define negligible

Choose one metric, such as:
- change in feed impedance;
- change in zenith gain;
- induced current magnitude.

Define a project-specific threshold for "negligible coupling."

State explicitly that the threshold is an engineering criterion, not a universal physical constant.

## NVIS connection

The crossed reference architecture and future broadband candidates cannot be analyzed as a collection of isolated dipoles. Coupling is part of the design.
