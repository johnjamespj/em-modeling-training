# Lesson 12 — Ground, Reflection, and Antenna Height

**Phase:** HF/NVIS Engineering  
**Target time:** 90 minutes

## Objective

Understand why a low-HF antenna cannot be evaluated independently of the ground beneath it.

By the end, you should be able to explain:
- why ground changes impedance and radiation pattern;
- antenna height in wavelengths;
- the roles of conductivity and relative permittivity;
- why perfect ground is useful as a reference but not a deployment model;
- why the same mast height behaves differently across 5–35 MHz.

## Theory

A horizontal antenna above ground radiates both directly and toward the ground. The ground-reflected field combines with the direct field.

The relative phase depends on:
- frequency;
- antenna height;
- elevation angle;
- ground electrical properties;
- polarization.

This interference can reinforce some elevation angles and suppress others.

## Height must be electrical

Always calculate:

```
h/lambda
```

For a 4.5 m antenna height, complete:

| f (MHz) | lambda (m) | h/lambda |
|---:|---:|---:|
| 5 | | |
| 7 | | |
| 10 | | |
| 15 | | |
| 20 | | |
| 25 | | |
| 30 | | |
| 35 | | |

## Prediction

Before simulation:

1. Will a horizontal dipole at 0.1 lambda produce the same elevation pattern as at 0.5 lambda?
2. What do you expect a very low horizontal dipole to do to high-angle radiation?
3. Should perfect ground and lossy soil produce identical efficiency?

## Lab A — perfect-ground reference

Model a horizontal dipole over ideal ground.

Compare several heights expressed in wavelengths around the chosen operating frequency.

Record:
- feed R+jX;
- zenith gain;
- peak elevation angle;
- major nulls.

## Lab B — finite ground

Repeat selected cases using finite ground.

Record the exact:
- conductivity;
- relative permittivity;
- ground model used.

Never label a case merely "real ground."

## Lab C — frequency

Hold physical height fixed and sweep frequency.

Explain pattern changes using h/lambda.

## Deliverable

Provide:
- height/wavelength table;
- perfect-ground versus finite-ground comparison;
- elevation patterns;
- impedance comparison;
- one paragraph explaining the physical mechanism.

## NVIS connection

For a low-HF antenna, ground is part of the electromagnetic system. Soil uncertainty can become design uncertainty.
