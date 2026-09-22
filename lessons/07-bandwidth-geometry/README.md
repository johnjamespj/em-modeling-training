# Lesson 07 — Bandwidth, Q, and Geometry

**Phase:** Antenna Theory Foundations  
**Target time:** 60 minutes

## Learning objectives

Understand:
- operational bandwidth versus a single resonance;
- qualitative Q intuition;
- how conductor radius affects impedance behavior;
- why broadband HF design is difficult;
- why a 5–35 MHz requirement is much more demanding than tuning one frequency.

## Lab

Use a dipole and vary wire radius while holding total length fixed.

Suggested radii:
- 0.5 mm
- 1 mm
- 5 mm
- 20 mm

For each, measure:
- resonant frequency;
- minimum VSWR;
- approximate 2:1 VSWR bandwidth;
- reactance slope near resonance.

| Radius | f_res | Min VSWR | 2:1 bandwidth | Observation |
|---:|---:|---:|---:|---|
| | | | | |

## Model validity

Do not assume every geometry accepted by a solver is physically or numerically valid.

Check:
- segment length;
- wire radius;
- junction geometry;
- solver warnings;
- whether the wire approximation remains reasonable.

## Broadband thought exercise

The target band ratio is:

```
35 / 5 = 7
```

That is a **7:1 frequency range**.

Discuss why maintaining simultaneously:
- manageable impedance;
- high efficiency;
- desired high-angle pattern;
- practical dimensions

over that entire span is a multi-objective problem.

## Phase I gate

Before moving to modeling fundamentals, the trainee should be able to explain, without software:

1. wavelength and electrical length;
2. current distribution on a basic dipole;
3. R + jX;
4. resonance versus matching;
5. VSWR;
6. radiation-pattern lobes/nulls;
7. gain versus efficiency;
8. why bandwidth depends on geometry.

If any of these are shaky, revisit the relevant lesson.
