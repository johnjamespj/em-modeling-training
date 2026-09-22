# Analysis and Automation

These utilities support reproducible analysis after the trainee understands the underlying model manually.

## Current utilities
- `wavelength.py` — wavelength and electrical-length calculations
- `angular_integration.py` — solid-angle integration of **linear** radiation data over elevation regions

## Planned utilities
- NEC output parser
- parameter-sweep generator/runner
- convergence report
- frequency/elevation heatmap generator
- candidate comparison report

## Rules
1. Understand an individual model before automating it.
2. Preserve units, parameters, solver warnings, failed runs, and model revision.
3. Never silently drop invalid runs.
4. Never integrate dB values directly. Convert to a linear power-like quantity first.
5. Confirm angular conventions before post-processing.
6. Generated plots must state exactly what quantity is shown: directivity, gain, realized gain, or normalized level.

Automation exists to make experiments reproducible, not to conceal assumptions.
