# Analysis and Automation Scripts

This directory is reserved for reproducible post-processing and parameter-sweep tools.

The training progression is intentional:

1. First understand individual NEC models manually.
2. Then automate repetitive sweeps.
3. Never automate a model you do not understand.

Planned utilities:
- wavelength/electrical-length calculator;
- complex-impedance convergence calculator;
- parameter sweep generator;
- NEC output parser;
- frequency/elevation heatmap generator;
- high-angle versus low-angle integrated-radiation calculator.

Automation must retain model parameters, units, failures, and solver warnings. A script that produces a clean plot while silently dropping bad runs is unacceptable.
