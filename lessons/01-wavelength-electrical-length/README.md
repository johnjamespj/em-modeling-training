# Lesson 01 — Frequency, Wavelength, and Electrical Length

**Phase:** Antenna Theory Foundations  
**Target time:** 45–60 minutes

## Learning objectives

By the end of this lesson, you should be able to:
- calculate free-space wavelength from frequency;
- express a physical antenna dimension in wavelengths;
- explain why the same physical antenna behaves differently across 5–35 MHz;
- predict how dipole resonant frequency changes with length;
- distinguish physical length from electrical length.

## Theory

Frequency and wavelength are related by

```
lambda = c / f
```

where approximately:

```
c = 3.0e8 m/s
```

A useful HF shortcut is:

```
lambda[m] ≈ 300 / f[MHz]
```

An antenna does not "see" meters by themselves. It responds to dimensions relative to wavelength.

For a physical dimension L:

```
electrical length = L / lambda
```

A 10 m wire is therefore electrically very different at 5 MHz and 35 MHz.

## Hand exercise — no simulator yet

Complete:

| f (MHz) | lambda (m) | 10 m / lambda |
|---:|---:|---:|
| 5 | | |
| 7 | | |
| 10 | | |
| 15 | | |
| 20 | | |
| 25 | | |
| 30 | | |
| 35 | | |

Then answer:

1. At what listed frequency is 10 m approximately half a wavelength?
2. At 5 MHz, is 10 m electrically short or long compared with 35 MHz?
3. Why should you expect a fixed antenna to develop more complicated behavior as frequency increases?

## Predict before simulation

We will model a center-fed straight dipole.

Before running anything, rank these antennas from **lowest to highest expected resonant frequency**:

- 9 m
- 10 m
- 11 m

Write one sentence explaining your ranking.

## Lab

Open the supplied model:

```
models/dipoles/dipole-10m-free-space.nec
```

Sweep around the fundamental resonance.

Record the frequency where input reactance X crosses approximately zero.

Then modify only total length:

- 9 m
- 10 m
- 11 m

Keep wire radius, segmentation, environment, and feed location conceptually equivalent.

| Length | Predicted order | Simulated resonance |
|---:|---:|---:|
| 9 m | | |
| 10 m | | |
| 11 m | | |

## Explain the result

Do not stop at "the frequency went up."

Explain using:

```
L / lambda
```

Why does shortening the physical antenna require a shorter wavelength, and therefore a higher frequency, to recover approximately the same electrical length?

## Connection to the final NVIS project

Your eventual antenna will be characterized from **5–35 MHz**.

A fixed 10 m dimension spans roughly a seven-to-one change in electrical size across that band. This is one reason broadband HF antennas can undergo major changes in impedance, current distribution, and radiation pattern.

## Checkpoint

Without a calculator, estimate:
- wavelength at 5 MHz;
- wavelength at 30 MHz;
- half wavelength at 10 MHz.

If those estimates are not comfortable yet, repeat the wavelength table before continuing.
