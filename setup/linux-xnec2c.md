# Linux Setup: xnec2c

## Why xnec2c?

xnec2c is a Linux-friendly graphical NEC2 antenna-modeling program. It is a good first solver because the geometry and physics remain visible instead of being buried beneath a large CAD workflow.

NEC is especially useful for wire antennas and conducting structures. It is not a general-purpose replacement for full 3D finite-element or FDTD solvers.

## Ubuntu / Linux Mint

```bash
sudo apt update
sudo apt install xnec2c
```

Launch:

```bash
xnec2c
```

## Verify the installation

Open xnec2c and load:

```
lessons/01-dipole-basics/dipole.nec
```

The model should show a straight, center-fed 10 m wire.

## Alternative for later lessons

After learning the fundamentals with NEC, **openEMS** is a useful Linux-friendly next step for FDTD and volumetric 3D EM problems.
