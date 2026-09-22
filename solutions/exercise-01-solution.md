# Instructor Notes — Exercise 01

Use this as a discussion guide rather than a set of numbers to copy.

## Prediction

At 15 MHz:

```
lambda = 3e8 / 15e6 = 20 m
```

A 10 m dipole is therefore approximately one-half wavelength in free space.

Shortening the dipole should move its resonance upward in frequency. Lengthening it should move resonance downward. To first order, resonant frequency varies inversely with antenna length.

## Resonance versus matching

For input impedance

```
Zin = R + jX
```

resonance occurs when the reactive component is approximately zero:

```
X = 0
```

That does not require `R = 50 ohms`.

For example, an antenna with

```
Zin = 70 + j0 ohms
```

is resonant but is not perfectly matched to a 50-ohm line. Its idealized VSWR is 70/50 = 1.4.

## Current distribution

For the fundamental half-wave dipole, current should be largest near the center/feed and approach zero toward the wire ends.

## Radiation pattern

A thin straight half-wave dipole has maximum radiation broadside to the wire and nulls along the wire axis.

The engineer should connect this result to the current distribution rather than merely identify the shape.

## Length experiment

Expected qualitative ordering:

```
f_res(9 m) > f_res(10 m) > f_res(11 m)
```

Require measured solver values in the submission rather than giving the trainee canned values.

## Convergence

Changing from 41 to 81 segments tests sensitivity to discretization.

A small difference is evidence that this particular reported quantity is stabilizing. It does **not** prove that the physical model is accurate.

Possible errors that mesh refinement cannot fix include:

- incorrect geometry
- incorrect material assumptions
- omitted ground
- omitted feed structure
- nearby structures not represented
- inappropriate solver/model assumptions

The 2% threshold is only the criterion chosen for this training exercise.

## Discussion prompt

Ask the engineer:

> If the numerical result converges perfectly but the antenna is modeled in free space while the real antenna is mounted one meter above conductive ground, what have you actually validated?

Desired idea: numerical convergence tests the numerical representation of the chosen model. It does not validate whether the chosen physical model represents reality.
