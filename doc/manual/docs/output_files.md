# Output files

IMPACT-Z writes its standard diagnostics to Fortran unit files (`fort.NN`)
in the working directory. The amount of output is controlled by the
`diagnostic_type` flag on header line 2
(see [DiagnosticType](reference/enums.md#diagnostictype)).

All diagnostics below are written at every space-charge step.

## Standard diagnostics

### fort.18 — reference particle

| Column | Quantity | Unit |
|-------:|----------|------|
| 1 | distance z | m |
| 2 | absolute phase | rad |
| 3 | relativistic gamma | 1 |
| 4 | kinetic energy | MeV |
| 5 | beta | 1 |
| 6 | maximum radius R (from the pipe axis) | m |

### fort.24, fort.25, fort.26 — RMS beam sizes (x, y, z)

`fort.24` is the x plane, `fort.25` the y plane, `fort.26` the z
(longitudinal) plane.

| Column | Quantity | Unit (x, y) | Unit (z) |
|-------:|----------|-------------|----------|
| 1 | distance z | m | m |
| 2 | centroid position | m | deg |
| 3 | RMS size | m | deg |
| 4 | centroid momentum | rad | MeV |
| 5 | RMS momentum | rad | MeV |
| 6 | Twiss parameter alpha | 1 | 1 |
| 7 | normalized RMS emittance | m·rad | deg·MeV |

### fort.27 — maximum amplitudes

| Column | Quantity | Unit |
|-------:|----------|------|
| 1 | distance z | m |
| 2 | max \|x\| | m |
| 3 | max \|px\| | rad |
| 4 | max \|y\| | m |
| 5 | max \|py\| | rad |
| 6 | max \|phase\| | deg |
| 7 | max \|energy deviation\| | MeV |

### fort.28 — load balance and particle loss

| Column | Quantity |
|-------:|----------|
| 1 | distance z (m) |
| 2 | minimum number of particles on a processor |
| 3 | maximum number of particles on a processor |
| 4 | total number of particles in the bunch |

Particle loss shows up as a decrease of column 4.

### fort.29 — third moments

Cube roots of the third central moments of the distribution.
Columns as in fort.27: z, x (m), px (rad), y (m), py (rad), phase (deg),
energy deviation (MeV).

### fort.30 — fourth moments

Fourth roots of the fourth central moments of the distribution.
Columns as in fort.29.

### fort.32 — charge states

| Column | Quantity |
|-------:|----------|
| 1 | distance z (m) |
| 2+ | number of particles for each charge state |

## Element-triggered output

Several control elements write additional files at their location in the
lattice (see the [element reference](reference/elements.md) for parameters):

| Element | Files | Contents |
|--------:|-------|----------|
| -2 `write_full` | `fort.N` | full particle distribution, 9 columns (see below) |
| -3 `density_profile_input` | `Xprof.data`, `Yprof.data`, `RadDens.data` | accumulated density along X, Y, R |
| -4 `density_profile` | `Xprof2.data`, `Yprof2.data`, `RadDens2.data` | density along X, Y, R |
| -5 `projection2_d` | `XY.data`, `XPx.data`, `XZ.data`, `YPy.data`, `YZ.data`, `ZPz.data` | 2D projections of the 6D distribution |
| -6 `density3_d` | `fort.8` | 3D density |
| -7 `write_phase_space_info` | `fort.1000+rank` | per-processor 6D phase space and domain info, for restart |
| -8 `write_slice_info` | `fort.N` | slice analysis (see below) |

### Particle dump format (`write_full`, -2)

One particle per line, in IMPACT-Z internal units (see
[Units and coordinates](units.md)):

| Column | Quantity | Unit |
|-------:|----------|------|
| 1 | x | c/ω |
| 2 | px | mc |
| 3 | y | c/ω |
| 4 | py | mc |
| 5 | phase | rad |
| 6 | energy deviation (E₀ − E) | mc² |
| 7 | charge-to-mass ratio q/m | 1/eV·c² |
| 8 | charge per macroparticle | C |
| 9 | particle id | — |

The file number `N` must avoid units used by the code itself: 5, 6, 24, 25,
26, 27, 29, 30, 32. A negative sample frequency writes IMPACT-T-style
columns instead (with z as Δz and pz as gamma).

### Slice analysis format (`write_slice_info`, -8)

| Column | Quantity |
|-------:|----------|
| 1 | bunch length coordinate (m) |
| 2 | number of particles per slice |
| 3 | current per slice (A) |
| 4 | x normalized emittance per slice (m·rad) |
| 5 | y normalized emittance per slice (m·rad) |
| 6 | dE/E |
| 7 | uncorrelated energy spread per slice (eV) |
| 8 | ⟨x⟩ per slice (m) |
| 9 | ⟨y⟩ per slice (m) |
| 10 | x mismatch factor |
| 11 | y mismatch factor |

The mismatch factors are only meaningful if the design Twiss parameters are
supplied as element parameters.

!!! note
    The source also contains a time-domain diagnostic variant that writes
    analogous statistics to `fort.34`–`fort.40` and `fort.48`
    (`diagnosticT_Output` in `src/Contrl/Output.f90`).
