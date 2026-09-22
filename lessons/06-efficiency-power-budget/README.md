# Lesson 06 — Efficiency and the RF Power Budget

**Phase:** Antenna Theory Foundations  
**Target time:** 60 minutes

## Learning objectives

Follow transmitter power through the modeled antenna system and distinguish:
- incident power;
- reflected power;
- accepted power;
- radiated power;
- conductor/material loss;
- ground loss;
- radiation efficiency;
- mismatch efficiency;
- realized gain.

## Power accounting

Conceptually:

```
Pincident
  ├── Preflected
  └── Paccepted
       ├── Pradiated
       └── Ploss
```

A matching network can alter the first split. It does not automatically eliminate losses in the second.

## Exercise

For an incident power of 100 W and |Gamma| = 0.3:

Calculate:
- reflected fraction;
- accepted fraction;
- accepted watts.

Then suppose radiation efficiency is 60%.

Calculate radiated power.

## Compare two hypothetical antennas

A:
- excellent match
- 35% radiation efficiency

B:
- worse match
- 90% radiation efficiency

Calculate total radiated fraction for representative mismatch values supplied by the instructor.

Discuss why the lower-VSWR antenna is not automatically the better radiator.

## Modeling lab

Use available solver outputs to identify which power/gain quantities xnec2c/NEC directly provides and which must be derived or require assumptions.

Document those limitations instead of inventing unavailable precision.

## NVIS connection

For the capstone, the useful question is not merely "Did the transmitter accept power?"

It is closer to:

> How much accepted power becomes radiation in the desired high-elevation angular region?

That requires keeping mismatch, losses, and angular distribution conceptually separate.
