<!-- This page is generated from spec/impactz.yaml by scripts/generate_reference.py. Do not edit by hand. -->

# Header reference

The first eleven (non-comment) lines of `ImpactZ.in` are global
settings, in the fixed order below. Lines starting with `!` are
comments and are skipped.

## Line 1: `ncpu_y`, `ncpu_z`, `gpu`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `ncpu_y` | int | `1` | Number of processors in y direction. Default is 1. |
| `ncpu_z` | int | `1` | Number of processors in z direction. Default is 1. |
| `gpu` | int | `0` |  See [GPUFlag](enums.md#gpuflag). |

## Line 2: `seed`, `n_particle`, `integrator_type`, `err`, `diagnostic_type`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `seed` | int | `0` | Random number seed. Default is 0. |
| `n_particle` | int | `0` | Number of particles. Default is 0. |
| `integrator_type` | int | `1` | Type of integrator. Default is `IntegratorType.linear_map` (equivalently "linear_map"). See [IntegratorType](enums.md#integratortype). |
| `err` | int | `1` | Error flag. Default is 1. |
| `diagnostic_type` | int | `2` | Type of diagnostics. Default is DiagnosticType.extended. See [DiagnosticType](enums.md#diagnostictype). |

## Line 3: `nx`, `ny`, `nz`, `boundary_type`, `radius_x`, `radius_y`, `z_period_size`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `nx` | int | `0` | Number of mesh points in x. Default is 0. |
| `ny` | int | `0` | Number of mesh points in y. Default is 0. |
| `nz` | int | `0` | Number of mesh points in z. Default is 0. |
| `boundary_type` | int | `1` | Boundary condition type. Default is `BoundaryType.trans_open_longi_open`. See [BoundaryType](enums.md#boundarytype). |
| `radius_x` | float | `0.0` | Pipe radius in x direction. Default is 0.0. |
| `radius_y` | float | `0.0` | Pipe radius in y direction. Default is 0.0. |
| `z_period_size` | float | `0.0` | Period size in z direction. Default is 0.0. |

## Line 4: `distribution`, `restart`, `subcycle`, `nbunch`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `distribution` | int | `1` | Particle distribution type. Default is `DistributionType.uniform`. See [DistributionType](enums.md#distributiontype). |
| `restart` | int | `0` | Restart flag. Default is 0. |
| `subcycle` | int | `0` | Subcycling flag. Default is 0. |
| `nbunch` | int | `1` | Number of bunches. Default is 0. |

## Line 5: `particle_list`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `particle_list` | list[int] | `[0]` | List of particles. Default is [0]. This must be the same length as `current_list` and `charge_over_mass_list`. |

## Line 6: `current_list`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `current_list` | list[float] | `[0.0]` | List of currents for each particle type. Default is [0.0]. This is used with: * `DistributionType.waterbag` and `DistributionType.multi_charge_state_gaussian`. |

## Line 7: `charge_over_mass_list`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `charge_over_mass_list` | list[float] | `[0.0]` | List of charge-to-mass ratios for each particle type. Default is [0.0]. This is used with: * `DistributionType.waterbag` and `DistributionType.multi_charge_state_gaussian`. * `CollimateBeam` elements * Calculating space charge forces |

## Line 8: `twiss_alpha_x`, `twiss_beta_x`, `twiss_norm_emit_x`, `twiss_mismatch_x`, `twiss_mismatch_px`, `twiss_offset_x`, `twiss_offset_px`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `twiss_alpha_x` | float | `0.0` | Alpha Twiss parameter in x plane. Default is 0.0. |
| `twiss_beta_x` | float | `1.0` | Beta Twiss parameter in x plane. Default is 1.0. |
| `twiss_norm_emit_x` | float | `1e-06` | Normalized emittance in x plane. Default is 1e-6. |
| `twiss_mismatch_x` | float | `1.0` | Mismatch factor for x coordinate. Default is 1.0. |
| `twiss_mismatch_px` | float | `1.0` | Mismatch factor for px coordinate. Default is 1.0. |
| `twiss_offset_x` | float | `0.0` | Offset in x coordinate. Default is 0.0. |
| `twiss_offset_px` | float | `0.0` | Offset in px coordinate. Default is 0.0. |

## Line 9: `twiss_alpha_y`, `twiss_beta_y`, `twiss_norm_emit_y`, `twiss_mismatch_y`, `twiss_mismatch_py`, `twiss_offset_y`, `twiss_offset_py`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `twiss_alpha_y` | float | `0.0` | Alpha Twiss parameter in y plane. Default is 0.0. |
| `twiss_beta_y` | float | `1.0` | Beta Twiss parameter in y plane. Default is 1.0. |
| `twiss_norm_emit_y` | float | `1e-06` | Normalized emittance in y plane. Default is 1e-6. |
| `twiss_mismatch_y` | float | `1.0` | Mismatch factor for y coordinate. Default is 1.0. |
| `twiss_mismatch_py` | float | `1.0` | Mismatch factor for py coordinate. Default is 1.0. |
| `twiss_offset_y` | float | `0.0` | Offset in y coordinate. Default is 0.0. |
| `twiss_offset_py` | float | `0.0` | Offset in py coordinate. Default is 0.0. |

## Line 10: `twiss_alpha_z`, `twiss_beta_z`, `twiss_norm_emit_z`, `twiss_mismatch_z`, `twiss_mismatch_e_z`, `twiss_offset_phase_z`, `twiss_offset_energy_z`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `twiss_alpha_z` | float | `1e-09` | Alpha Twiss parameter in z plane. Default is 1e-9. This must be non-zero, or compute domain calculations in IMPACT-Z may lead to crashes. |
| `twiss_beta_z` | float | `1.0` | Beta Twiss parameter in z plane. Default is 1.0. |
| `twiss_norm_emit_z` | float | `1e-06` | Normalized emittance in z plane. Default is 1e-6. |
| `twiss_mismatch_z` | float | `1.0` | Mismatch factor for z coordinate. Default is 1.0. |
| `twiss_mismatch_e_z` | float | `1.0` | Mismatch factor for energy coordinate. Default is 1.0. |
| `twiss_offset_phase_z` | float | `0.0` | Offset in z phase. Default is 0.0. |
| `twiss_offset_energy_z` | float | `0.0` | Offset in energy. Default is 0.0. |

## Line 11: `average_current`, `reference_kinetic_energy`, `reference_particle_mass`, `reference_particle_charge`, `reference_frequency`, `initial_phase_ref`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `average_current` | float | `1.0` | Average beam current in Amperes. Default is 1.0. |
| `reference_kinetic_energy` | float | `0.0` | Reference particle kinetic energy. Default is 0.0. |
| `reference_particle_mass` | float | `0.0` | Reference particle mass. Default is 0.0. |
| `reference_particle_charge` | float | `0.0` | Reference particle charge. Default is 0.0. |
| `reference_frequency` | float | `0.0` | Reference RF frequency. Default is 0.0. |
| `initial_phase_ref` | float | `0.0` | Initial phase of reference particle. Default is 0.0. |

## Line 12: `filename`, `verbose`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `filename` | Path |  | Input file path. Default is None. (Excluded from JSON serialization.) |
| `verbose` | bool | `false` | Verbose output flag when running IMPACT-Z. Default is False. |
