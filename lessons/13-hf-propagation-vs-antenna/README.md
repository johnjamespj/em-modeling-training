# Lesson 13 — HF Propagation vs. Antenna Performance

**Phase:** HF/NVIS Engineering  
**Target time:** 60–75 minutes

## Objective

Separate two engineering questions that are often mixed together:

1. **Where does the antenna radiate energy?**
2. **Will the ionosphere return that energy to a desired region?**

NEC primarily helps answer the first question. It does not predict the complete time-varying ionospheric path.

## NVIS concept

Near Vertical Incidence Skywave uses high-elevation HF radiation so that ionospheric refraction/return can support regional coverage.

For this course, high-angle antenna performance will often be examined over a region such as:

```
60° to 90° elevation
```

That angular range is an engineering analysis choice, not a universal definition of every NVIS path.

## Important distinction

A model may show strong radiation at 80° elevation at 25 MHz.

That does **not** prove an NVIS link will exist at 25 MHz at a particular place and time.

Propagation depends on ionospheric conditions in addition to the antenna.

## Classification exercise

For each quantity, classify it as primarily:
- antenna-model output;
- propagation/environment input;
- link/system result.

Items:
- feed impedance;
- radiation efficiency;
- elevation pattern;
- soil conductivity;
- ionospheric critical frequency;
- path loss;
- received SNR;
- transmitter power;
- operating frequency;
- antenna polarization.

Discuss ambiguous cases.

## Lab

Take one low horizontal-dipole model.

At several frequencies, record:
- zenith gain;
- gain at 60°, 70°, 80°;
- peak elevation angle;
- low-angle gain.

Then write two conclusions:

### Allowed antenna conclusion
Example structure:

> Under the modeled ground and geometry assumptions, the antenna produces ______ high-angle radiation at ______ MHz.

### Unsupported propagation conclusion
Identify a claim you cannot make from NEC alone.

## Deliverable

Submit the classification table and a one-page explanation titled:

**What my antenna model can and cannot tell me about NVIS.**
