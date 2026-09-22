# NVIS Metric Definition Sheet

Complete before candidate optimization.

| Metric | Definition | Units | Convention | Source | Purpose |
|---|---|---|---|---|---|
| R | | ohm | | solver | |
| X | | ohm | | solver | |
| VSWR | | ratio | Z0 = | | |
| Accepted power | | | | | |
| Radiation efficiency | | % | | | |
| Realized gain | | dBi | | | |
| Zenith gain | | dBi | elevation=90° | | |
| P_high | | | elevation=__ to __ | derived | |
| P_low | | | elevation=__ to __ | derived | |
| High/low ratio | 10log10(P_high/P_low) | dB | | derived | |
| High-angle azimuth variation | Gmax-Gmin | dB | elevation=__ | derived | |

## Coordinate convention
Document exactly how the solver defines theta, phi, elevation, azimuth, and zenith.

## Normalization
State whether pattern values are directivity, gain, realized gain, or normalized relative level.

## Change control
If a metric changes after comparison begins, record why and rerun affected comparisons.
