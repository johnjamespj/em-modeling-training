# Lesson 02 — Current Distribution and Radiation

**Phase:** Antenna Theory Foundations  
**Target time:** 45–60 minutes

## Learning objectives

You should be able to:
- describe the approximate current distribution on a fundamental half-wave dipole;
- identify current maxima and minima;
- connect current distribution to radiation;
- distinguish near-field quantities from the far-field radiation pattern;
- predict how current distribution becomes more complicated when a wire becomes electrically long.

## Mental model

A radiating antenna is not simply a resistor suspended in space. RF voltage and current vary along the conductor.

For the fundamental center-fed dipole, current is approximately:
- largest near the center;
- small near the ends.

The exact distribution depends on geometry and environment.

## Prediction

Sketch the expected current magnitude along a center-fed half-wave dipole.

Mark:
- feed point;
- current maximum;
- current minima.

Do this before opening xnec2c.

## Lab A — fundamental dipole

Load the 10 m free-space model.

Inspect current magnitude along the wire near its fundamental resonance.

Compare the solver result with your sketch.

Answer:
1. Where is current largest?
2. What happens near the wire ends?
3. Does the current distribution look approximately symmetric?

## Lab B — keep geometry fixed, change frequency

Keep the 10 m wire unchanged and inspect current distribution at:

- 5 MHz
- 15 MHz
- 25 MHz
- 35 MHz

For each frequency record:

| Frequency | L/lambda | Number/location of major current maxima | Observation |
|---:|---:|---|---|
| 5 | | | |
| 15 | | | |
| 25 | | | |
| 35 | | | |

## Predict the pattern

Before opening the far-field plot at each frequency, use the current distribution to predict whether the radiation pattern should remain simple or develop additional lobes/nulls.

Then compare against simulation.

## Key distinction

**Current distribution is on the antenna. Radiation pattern describes the far field.**

Do not call a current plot a radiation pattern.

## Connection to NVIS

Across 5–35 MHz, the final antenna may move through several electrical regimes. Tracking current distribution helps explain why high-angle radiation can strengthen, weaken, split into lobes, or disappear even though the physical wires never moved.

## Checkpoint question

If a fixed wire becomes several wavelengths long, would you expect the current to retain one simple maximum at its center? Explain before continuing.
