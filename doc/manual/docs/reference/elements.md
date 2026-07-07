<!-- This page is generated from spec/impactz.yaml by scripts/generate_reference.py. Do not edit by hand. -->

# Element reference

Each lattice line in `ImpactZ.in` has the form:

```text
length steps map_steps type v5 v6 ... /
```

where `type` selects the element and the remaining columns are the
parameters listed below. Trailing parameters may be omitted; they
default to zero. The `/` terminates the line.

!!! note "LUME-Impact"
    The *class* named for each element is the corresponding Python class
    in [LUME-Impact](https://github.com/ChristopherMayes/lume-impact)'s
    `impact.z` subpackage.

## Element type codes

| Code | Element | Category |
|-----:|---------|----------|
| 0 | [`drift`](#drift) | beamline element |
| 1 | [`quadrupole`](#quadrupole) | beamline element |
| 2 | [`constant_focusing`](#constant_focusing) | beamline element |
| 3 | [`solenoid`](#solenoid) | beamline element |
| 4 | [`dipole`](#dipole) | beamline element |
| 5 | [`multipole`](#multipole) | beamline element |
| 6 | [`wiggler`](#wiggler) | beamline element |
| 101 | [`dtl`](#dtl) | beamline element |
| 102 | [`ccdtl`](#ccdtl) | beamline element |
| 103 | [`ccl`](#ccl) | beamline element |
| 104 | [`superconducting_cavity`](#superconducting_cavity) | beamline element |
| 105 | [`solenoid_with_rf_cavity`](#solenoid_with_rf_cavity) | beamline element |
| 106 | [`traveling_wave_rf_cavity`](#traveling_wave_rf_cavity) | beamline element |
| 110 | [`user_defined_rf_cavity`](#user_defined_rf_cavity) | beamline element |
| -1 | [`shift_centroid`](#shift_centroid) | control |
| -2 | [`write_full`](#write_full) | control |
| -3 | [`density_profile_input`](#density_profile_input) | control |
| -4 | [`density_profile`](#density_profile) | control |
| -5 | [`projection_2_d`](#projection_2_d) | control |
| -6 | [`density_3_d`](#density_3_d) | control |
| -7 | [`write_phase_space_info`](#write_phase_space_info) | control |
| -8 | [`write_slice_info`](#write_slice_info) | control |
| -10 | [`scale_mismatch_particle_6_d_coordinates`](#scale_mismatch_particle_6_d_coordinates) | control |
| -12 | [`external_linear_map_kick`](#external_linear_map_kick) | control |
| -13 | [`collimate_beam`](#collimate_beam) | control |
| -14 | [`toggle_space_charge`](#toggle_space_charge) | control |
| -16 | [`rotate_beam_x`](#rotate_beam_x) | control |
| -17 | [`rotate_beam_y`](#rotate_beam_y) | control |
| -18 | [`rotate_beam`](#rotate_beam) | control |
| -19 | [`beam_shift`](#beam_shift) | control |
| -20 | [`beam_energy_spread`](#beam_energy_spread) | control |
| -21 | [`shift_beam_centroid`](#shift_beam_centroid) | control |
| -25 | [`integrator_type_switch`](#integrator_type_switch) | control |
| -40 | [`beam_kicker_by_rf_nonlinearity`](#beam_kicker_by_rf_nonlinearity) | control |
| -41 | [`rfcavity_structure_wakefield`](#rfcavity_structure_wakefield) | control |
| -44 | [`thin_lens_rf_deflector`](#thin_lens_rf_deflector) | control |
| -52 | [`energy_modulation`](#energy_modulation) | control |
| -55 | [`kick_beam_using_multipole`](#kick_beam_using_multipole) | control |
| -99 | [`halt_execution`](#halt_execution) | control |

## Beamline elements

### drift

**Type code: `0`** &nbsp;&middot;&nbsp; LUME-Impact class: `Drift`

Drift element.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **0** |
| 5 | `radius` | float | `1.0` | Radius of the pipe, in meters. |
| 6 | `unused_0` | float | `0.0` | *Unused; set to 0.* |
| 7 | `unused_1` | float | `0.0` | *Unused; set to 0.* |

### quadrupole

**Type code: `1`** &nbsp;&middot;&nbsp; LUME-Impact class: `Quadrupole`

A quadrupole element.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **1** |
| 5 | `k1` | float | `0.0` | The quadrupole strength, 1/m^2. (NOTE: the manual is actually wrong here, this is not B1 in units of T/m) |
| 6 | `file_id` | float | `0.0` | An ID for the input gradient file. Determines profile behavior: if greater than 0, a fringe field profile is read; if less than -10, a linear transfer map of an undulator is used; if between -10 and 0, it's the k-value linear transfer map; if equal to 0, it uses the linear transfer map with the gradient. |
| 7 | `radius` | float | `0.0` | The radius of the quadrupole, measured in meters. |
| 8 | `misalignment_error_x` | float | `0.0` | The x-direction misalignment error, given in meters. |
| 9 | `misalignment_error_y` | float | `0.0` | The y-direction misalignment error, given in meters. |
| 10 | `rotation_error_x` | float | `0.0` | Rotation error in radians. |
| 11 | `rotation_error_y` | float | `0.0` | Rotation error in radians. |
| 12 | `rotation_error_z` | float | `0.0` | Rotation error in radians. |

### constant_focusing

**Type code: `2`** &nbsp;&middot;&nbsp; LUME-Impact class: `ConstantFocusing`

3D constant focusing.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **2** |
| 5 | `kx0_squared` | float | `0.0` | The square of the kx0 parameter. |
| 6 | `ky0_squared` | float | `0.0` | The square of the ky0 parameter. |
| 7 | `kz0_squared` | float | `0.0` | The square of the kz0 parameter. |
| 8 | `radius` | float | `0.0` | The radius of the focusing element in meters. |

### solenoid

**Type code: `3`** &nbsp;&middot;&nbsp; LUME-Impact class: `Solenoid`

Solenoid used in beam dynamics simulations.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | The effective length of the solenoid in meters, including two linear fringe regions and a flat top region (solenoid integrator). |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **3** |
| 5 | `Bz0` | float | `0.0` | The axial magnetic field at the center of the solenoid in Tesla. |
| 6 | `file_id` | float | `0.0` | The identifier for the input field file. |
| 7 | `radius` | float | `0.0` | The radius of the solenoid in meters. |
| 8 | `misalignment_error_x` | float | `0.0` | Misalignment error in the x-direction in meters. |
| 9 | `misalignment_error_y` | float | `0.0` | Misalignment error in the y-direction in meters. |
| 10 | `rotation_error_x` | float | `0.0` |  |
| 11 | `rotation_error_y` | float | `0.0` | Rotation error in the y-direction in radians. |
| 12 | `rotation_error_z` | float | `0.0` | Rotation error in the z-direction in radians. |

### dipole

**Type code: `4`** &nbsp;&middot;&nbsp; LUME-Impact class: `Dipole`

Represents a dipole element used in beam simulations.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **4** |
| 5 | `angle` | float | `1e-06` | Bending angle [rad]. Must be non-zero. |
| 6 | `k1` | float | `0.0` | Field strength. |
| 7 | `input_switch` | float | `0.0` | CSR settings. - `input_switch <= 200`: no CSR - `200 < input_switch <=500`: CSR in the bend - `input_switch > 500`: CSR in the bend and the next following drift |
| 8 | `hgap` | float | `0.0` | Half gap [m]. |
| 9 | `e1` | float | `0.0` | Entrance pole face angle [rad]. |
| 10 | `e2` | float | `0.0` | Exit pole face angle [rad]. |
| 11 | `entrance_curvature` | float | `0.0` | Curvature of entrance face [rad]. |
| 12 | `exit_curvature` | float | `0.0` | Curvature of exit face [rad]. |
| 13 | `fint` | float | `0.0` | Integrated fringe field K of entrance (Kf). Fringe field K of exit assumed to be equal (Kb = Kf). |
| 14 | `misalignment_error_x` | float | `0.0` | Misalignment error in the x direction. |
| 15 | `misalignment_error_y` | float | `0.0` | Misalignment error in the y direction. |
| 16 | `rotation_error_x` | float | `0.0` | Rotation error around the x axis. |
| 17 | `rotation_error_y` | float | `0.0` | Rotation error around the y axis. |
| 18 | `rotation_error_z` | float | `0.0` | Rotation error around the z axis. |

### multipole

**Type code: `5`** &nbsp;&middot;&nbsp; LUME-Impact class: `Multipole`

Represents a multipole element used in beam simulations.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **5** |
| 5 | `multipole_type` | int | `2` | The type of multipole element, sextupole, octupole, or decapole. See [MultipoleType](enums.md#multipoletype). |
| 6 | `field_strength` | float | `0.0` | The strength of the magnetic field. Units of T/m^n. |
| 7 | `file_id` | float | `0.0` | Identifier for related input data file. |
| 8 | `radius` | float | `0.0` | The radius of the multipole. |
| 9 | `misalignment_error_x` | float | `0.0` | Misalignment error in the x-direction. |
| 10 | `misalignment_error_y` | float | `0.0` | Misalignment error in the y-direction. |
| 11 | `rotation_error_x` | float | `0.0` | Rotation error around the x-axis. |
| 12 | `rotation_error_y` | float | `0.0` | Rotation error around the y-axis. |
| 13 | `rotation_error_z` | float | `0.0` | Rotation error around the z-axis. |

### wiggler

**Type code: `6`** &nbsp;&middot;&nbsp; LUME-Impact class: `Wiggler`

Represents a planar or helical wiggler element used in beam simulations.

Only supports the integrator type `IntegratorType.runge_kutta`.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **6** |
| 5 | `wiggler_type` | int | `1` | Wiggler type. Defaults to `WigglerType.planar`. See [WigglerType](enums.md#wigglertype). |
| 6 | `max_field_strength` | float | `0.0` | The maximum strength of the magnetic field. Units of T/m^n. |
| 7 | `file_id` | float | `0.0` | File ID (unused?) |
| 8 | `radius` | float | `0.0` | Radius in meters. |
| 9 | `kx` | float | `0.0` | Wiggler strength. |
| 10 | `period` | float | `0.0` | Period of the wiggler. |
| 11 | `misalignment_error_x` | float | `0.0` | Misalignment error in the x-direction. |
| 12 | `misalignment_error_y` | float | `0.0` | Misalignment error in the y-direction. |
| 13 | `rotation_error_x` | float | `0.0` | Rotation error around the x-axis. |
| 14 | `rotation_error_y` | float | `0.0` | Rotation error around the y-axis. |
| 15 | `rotation_error_z` | float | `0.0` | Rotation error around the z-axis. |

### dtl

**Type code: `101`** &nbsp;&middot;&nbsp; LUME-Impact class: `DTL`

Discrete-Transmission-Line element with specified parameters.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **101** |
| 5 | `field_scaling` | float | `0.0` | Scaling factor for the electrical/magnetic field. |
| 6 | `rf_frequency` | float | `0.0` | RF frequency in Hertz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees. |
| 8 | `file_id` | float | `0.0` | Input field ID (using a simple sinusoidal model if ID<0). |
| 9 | `radius` | float | `0.0` | Radius in meters. |
| 10 | `quad1_length` | float | `0.0` | Length of the first quadrupole in meters. |
| 11 | `quad1_gradient` | float | `0.0` | Gradient of the first quadrupole in Tesla/meter. |
| 12 | `quad2_length` | float | `0.0` | Length of the second quadrupole in meters. |
| 13 | `quad2_gradient` | float | `0.0` | Gradient of the second quadrupole in Tesla/meter. |
| 14 | `q1_misalignment_error_x` | float | `0.0` |  |
| 15 | `q1_misalignment_error_y` | float | `0.0` |  |
| 16 | `q1_rotation_error_x` | float | `0.0` |  |
| 17 | `q1_rotation_error_y` | float | `0.0` |  |
| 18 | `q1_rotation_error_z` | float | `0.0` |  |
| 19 | `q2_misalignment_error_x` | float | `0.0` |  |
| 20 | `q2_misalignment_error_y` | float | `0.0` |  |
| 21 | `q2_rotation_error_x` | float | `0.0` |  |
| 22 | `q2_rotation_error_y` | float | `0.0` |  |
| 23 | `q2_rotation_error_z` | float | `0.0` |  |
| 24 | `rf_misalignment_error_x` | float | `0.0` |  |
| 25 | `rf_misalignment_error_y` | float | `0.0` |  |
| 26 | `rf_rotation_error_x` | float | `0.0` |  |
| 27 | `rf_rotation_error_y` | float | `0.0` |  |
| 28 | `rf_rotation_error_z` | float | `0.0` |  |

### ccdtl

**Type code: `102`** &nbsp;&middot;&nbsp; LUME-Impact class: `CCDTL`

A CCDTL (Cell-Coupled Drift Tube Linac) input element represented by its parameters.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **102** |
| 5 | `field_scaling` | float | `0.0` | Field scaling factor. |
| 6 | `rf_frequency` | float | `0.0` | RF frequency in Hertz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees. |
| 8 | `file_id` | float | `0.0` | Input field ID (if ID<0, use simple sinusoidal model, only works for the map integrator). The phase is the design phase with 0 for maximum energy gain. |
| 9 | `radius` | float | `0.0` | Radius in meters. |
| 10 | `misalignment_error_x` | float | `0.0` |  |
| 11 | `misalignment_error_y` | float | `0.0` | Y misalignment error in meters. |
| 12 | `rotation_error_x` | float | `0.0` | Rotation error around the x-axis in radians. |
| 13 | `rotation_error_y` | float | `0.0` | Rotation error around the y-axis in radians. |
| 14 | `rotation_error_z` | float | `0.0` | Rotation error around the z-axis in radians. |

### ccl

**Type code: `103`** &nbsp;&middot;&nbsp; LUME-Impact class: `CCL`

CCL input element with specific parameters.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **103** |
| 5 | `field_scaling` | float | `0.0` | Field scaling factor. |
| 6 | `rf_frequency` | float | `0.0` | RF frequency in Hertz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees. |
| 8 | `file_id` | float | `0.0` | Input field ID. If ID < 0, use the simple sinusoidal model (only works for the map integrator, phase is the design phase with 0 for maximum energy gain). |
| 9 | `radius` | float | `0.0` | Radius of the element in meters. |
| 10 | `misalignment_error_x` | float | `0.0` | X-axis misalignment error in meters. |
| 11 | `misalignment_error_y` | float | `0.0` | Y-axis misalignment error in meters. |
| 12 | `rotation_error_x` | float | `0.0` | Rotation error about the x-axis in radians. |
| 13 | `rotation_error_y` | float | `0.0` | Rotation error about the y-axis in radians. |
| 14 | `rotation_error_z` | float | `0.0` | Rotation error about the z-axis in radians. |

### superconducting_cavity

**Type code: `104`** &nbsp;&middot;&nbsp; LUME-Impact class: `SuperconductingCavity`

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **104** |
| 5 | `field_scaling` | float | `0.0` |  |
| 6 | `rf_frequency` | float | `0.0` | RF frequency in Hz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees (design phase with 0 for maximum energy gain). |
| 8 | `file_id` | float | `0.0` | Input field ID (if ID < 0, only works for the map integrator). |
| 9 | `radius` | float | `0.0` | Radius in meters. |
| 10 | `misalignment_error_x` | float | `0.0` |  |
| 11 | `misalignment_error_y` | float | `0.0` |  |
| 12 | `rotation_error_x` | float | `0.0` |  |
| 13 | `rotation_error_y` | float | `0.0` |  |
| 14 | `rotation_error_z` | float | `0.0` |  |

### solenoid_with_rf_cavity

**Type code: `105`** &nbsp;&middot;&nbsp; LUME-Impact class: `SolenoidWithRFCavity`

A solenoid with an RF cavity.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **105** |
| 5 | `field_scaling` | float | `0.0` | The field scaling factor. |
| 6 | `rf_frequency` | float | `0.0` | The RF frequency in Hertz. |
| 7 | `phase_deg` | float | `0.0` | The driven phase in degrees. |
| 8 | `file_id` | float | `1.0` | The input field ID. |
| 9 | `radius` | float | `0.0` | The radius of the solenoid in meters. |
| 10 | `misalignment_error_x` | float | `0.0` | The x-axis misalignment error in meters. |
| 11 | `misalignment_error_y` | float | `0.0` | The y-axis misalignment error in meters. |
| 12 | `rotation_error_x` | float | `0.0` | The error in rotation about the x-axis in radians. |
| 13 | `rotation_error_y` | float | `0.0` | The error in rotation about the y-axis in radians. |
| 14 | `rotation_error_z` | float | `0.0` | The error in rotation about the z-axis in radians. |
| 15 | `bz0` | float | `0.0` | The Bz0 field value in Tesla. |
| 16 | `aperture_size_for_wakefield` | float | `0.0` | The aperture size for wakefield computations. |
| 17 | `gap_size_for_wakefield` | float | `0.0` | The gap size for the wake field. |
| 18 | `length_for_wakefield` | float | `0.0` | The length for wake, indicating RF structure wakefield should be turned on if this value is greater than zero. |

### traveling_wave_rf_cavity

**Type code: `106`** &nbsp;&middot;&nbsp; LUME-Impact class: `TravelingWaveRFCavity`

Traveling Wave RF Cavity element.

This element represents a traveling wave RF cavity specified by several
parameters that define its physical and operational characteristics.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **106** |
| 5 | `field_scaling` | float | `0.0` | Scaling factor for the field. |
| 6 | `rf_frequency` | float | `0.0` | RF frequency, in Hertz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees. |
| 8 | `file_id` | float | `0.0` | Input field ID. |
| 9 | `radius` | float | `0.0` | Radius of the cavity in meters. |
| 10 | `misalignment_error_x` | float | `0.0` | X misalignment error in meters. |
| 11 | `misalignment_error_y` | float | `0.0` | Y misalignment error in meters. |
| 12 | `rotation_error_x` | float | `0.0` | Rotation errors in x [rad]. |
| 13 | `rotation_error_y` | float | `0.0` | Rotation errors in x [rad]. |
| 14 | `rotation_error_z` | float | `0.0` | Rotation errors in x [rad]. |
| 15 | `phase_diff` | float | `0.0` | Phase difference B and A (pi - beta * d). |
| 16 | `aperture_size_for_wakefield` | float | `0.0` | Aperture size for wakefield. An aperture size >0 enables the wakefield calculation. |
| 17 | `gap_size` | float | `0.0` | Gap size for wakefield. |
| 18 | `length_for_wakefield` | float | `0.0` |  |

### user_defined_rf_cavity

**Type code: `110`** &nbsp;&middot;&nbsp; LUME-Impact class: `UserDefinedRFCavity`

A user-defined RF cavity element in the simulation.

EMfld in IMPACT-Z.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **110** |
| 5 | `field_scaling` | float | `0.0` | Scaling factor for the field. |
| 6 | `rf_frequency` | float | `0.0` | RF frequency in Hertz. |
| 7 | `phase_deg` | float | `0.0` | Driven phase in degrees. |
| 8 | `file_id` | float | `0.0` | ID of the input field. |
| 9 | `radius_x` | float | `0.0` |  |
| 10 | `radius_y` | float | `0.0` | Y radius in meters. |
| 11 | `misalignment_error_x` | float | `0.0` | Misalignment error in the X direction, in meters. |
| 12 | `misalignment_error_y` | float | `0.0` | Misalignment error in the Y direction, in meters. |
| 13 | `rotation_error_x` | float | `0.0` |  |
| 14 | `rotation_error_y` | float | `0.0` |  |
| 15 | `rotation_error_z` | float | `0.0` |  |
| 16 | `data_mode` | int | `1` | Mode of using field data. 1.0 uses discrete data only, 2.0 uses both discrete data and analytical function, other values use analytical function only. See [RFCavityDataMode](enums.md#rfcavitydatamode). |
| 17 | `coordinate_type` | int | `2` | Coordinate type for the field. 2.0 for Cartesian coordinates, 1.0 for Cylindrical coordinates. See [RFCavityCoordinateType](enums.md#rfcavitycoordinatetype). |

## Control and diagnostic elements

### shift_centroid

**Type code: `-1`** &nbsp;&middot;&nbsp; LUME-Impact class: `ShiftCentroid`

Shift the centroid.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Length of the element in meters. |
| 2 | `steps` | int | `0` | Number of space-charge kicks through the beamline element. Each "step" consists of a half-step, a space-charge kick, and another half-step. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-1** |

### write_full

**Type code: `-2`** &nbsp;&middot;&nbsp; LUME-Impact class: `WriteFull`

Write the particle distribution into a fort.N file.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `file_id` | int | `0` | The File ID. |
| 4 | `type_id` | int | — | Element type code: **-2** |
| 5 | `unused_2` | float | `0.0` | *Unused; set to 0.* |
| 6 | `sample_frequency` | int | `0` | Write every Nth particle. |

### density_profile_input

**Type code: `-3`** &nbsp;&middot;&nbsp; LUME-Impact class: `DensityProfileInput`

Input element: density profile input parameters.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-3** |
| 5 | `radius` | float | `0.0` | Radius in meters. |
| 6 | `xmax` | float | `0.0` | Maximum X in meters. |
| 7 | `pxmax` | float | `0.0` | Maximum Px in mc. |
| 8 | `ymax` | float | `0.0` | Maximum Y in meters. |
| 9 | `pymax` | float | `0.0` | Maximum Py in mc. |
| 10 | `zmax` | float | `0.0` | Maximum Z in meters. |
| 11 | `pzmax` | float | `0.0` | Maximum Pz in mc^2. |

### density_profile

**Type code: `-4`** &nbsp;&middot;&nbsp; LUME-Impact class: `DensityProfile`

Input element: write the density along R, X, Y into files.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-4** |
| 5 | `radius` | float | `0.0` | Radius in meters. |
| 6 | `xmax` | float | `0.0` | Maximum value in X direction in meters. |
| 7 | `pxmax` | float | `0.0` | Maximum value in X direction momentum in mc. |
| 8 | `ymax` | float | `0.0` | Maximum value in Y direction in meters. |
| 9 | `pymax` | float | `0.0` | Maximum value in Y direction momentum in mc. |
| 10 | `zmax` | float | `0.0` | Maximum value in Z direction in radians. |
| 11 | `pzmax` | float | `0.0` | Maximum value in Z direction momentum in mc^2. |

### projection_2_d

**Type code: `-5`** &nbsp;&middot;&nbsp; LUME-Impact class: `Projection2D`

Represents the 2D projections of a 6D distribution.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-5** |
| 5 | `radius` | float | `0.0` | The radius of the projection. |
| 6 | `xmax` | float | `0.0` | The maximum x value. |
| 7 | `pxmax` | float | `0.0` | The maximum px value. |
| 8 | `ymax` | float | `0.0` | The maximum y value. |
| 9 | `pymax` | float | `0.0` | The maximum py value. |
| 10 | `zmax` | float | `0.0` | The maximum z value. |
| 11 | `pzmax` | float | `0.0` | The maximum pz value. |

### density_3_d

**Type code: `-6`** &nbsp;&middot;&nbsp; LUME-Impact class: `Density3D`

Input element: 3D density.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-6** |
| 5 | `radius` | float | `0.0` | Radius in meters. |
| 6 | `xmax` | float | `0.0` | Maximum x value in meters. |
| 7 | `pxmax` | float | `0.0` | Maximum px value in mc. |
| 8 | `ymax` | float | `0.0` | Maximum y value in meters. |
| 9 | `pymax` | float | `0.0` | Maximum py value in mc. |
| 10 | `zmax` | float | `0.0` | Maximum z value in degrees. |
| 11 | `pzmax` | float | `0.0` | Maximum pz value in mc^2. |

### write_phase_space_info

**Type code: `-7`** &nbsp;&middot;&nbsp; LUME-Impact class: `WritePhaseSpaceInfo`

Input element: write the 6D phase space information and local computation
domain information.

Writes to files fort.1000, fort.1001, fort.1002, ...,
fort.(1000+Nprocessor-1). This function is used for restart purposes.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` |  |
| 2 | `steps` | int | `0` |  |
| 3 | `map_steps` | int | `0` |  |
| 4 | `type_id` | int | — | Element type code: **-7** |

### write_slice_info

**Type code: `-8`** &nbsp;&middot;&nbsp; LUME-Impact class: `WriteSliceInfo`

Write slice information into file fort.{file_id} using specific slices.

If the twiss mismatch parameters (alpha_x, etc.) are not provided, the
mismatch factor will be ignored.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `file_id` | int | `0` | The file ID to write slice information to. |
| 4 | `type_id` | int | — | Element type code: **-8** |
| 5 | `slices` | int | `0` | Number of slices. |
| 6 | `alpha_x` | float | `0.0` | Twiss parameter alpha_x at the location. |
| 7 | `beta_x` | float | `0.0` | Twiss parameter beta_x at the location (m). |
| 8 | `alpha_y` | float | `0.0` | Twiss parameter alpha_y at the location. |
| 9 | `beta_y` | float | `0.0` | Twiss parameter beta_y at the location (m). |

### scale_mismatch_particle_6_d_coordinates

**Type code: `-10`** &nbsp;&middot;&nbsp; LUME-Impact class: `ScaleMismatchParticle6DCoordinates`

Scale/mismatch the particle 6D coordinates.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-10** |
| 5 | `radius` | float | `0.0` | The radius, not used in computations. |
| 6 | `xmis` | float | `0.0` | The x-coordinate mismatch. |
| 7 | `pxmis` | float | `0.0` | The px-coordinate mismatch. |
| 8 | `ymis` | float | `0.0` | The y-coordinate mismatch. |
| 9 | `pymis` | float | `0.0` | The py-coordinate mismatch. |
| 10 | `tmis` | float | `0.0` | The time-coordinate mismatch. |
| 11 | `ptmis` | float | `0.0` | The pt-coordinate mismatch. |

### external_linear_map_kick

**Type code: `-12`** &nbsp;&middot;&nbsp; LUME-Impact class: `ExternalLinearMapKick`

Apply an instant kick using a 6x6 linear transfer map from an external file.

The map is read from ``fort.N``, where ``N`` is `file_id`. The file
contains the six rows of the matrix, one row per line. The matrix is
applied in ``(x [m], x' [rad], y [m], y' [rad], z [m], dp/p)``
coordinates.

Available in IMPACT-Z v2.7+.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `file_id` | int | `0` | The file ID N; the transfer matrix is read from ``fort.N``. |
| 4 | `type_id` | int | — | Element type code: **-12** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |

### collimate_beam

**Type code: `-13`** &nbsp;&middot;&nbsp; LUME-Impact class: `CollimateBeam`

Collimate the beam with transverse rectangular aperture sizes.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-13** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |
| 6 | `xmin` | float | `0.0` | Minimum x value in meters. |
| 7 | `xmax` | float | `0.0` | Maximum x value in meters. |
| 8 | `ymin` | float | `0.0` | Minimum y value in meters. |
| 9 | `ymax` | float | `0.0` | Maximum y value in meters. |

### toggle_space_charge

**Type code: `-14`** &nbsp;&middot;&nbsp; LUME-Impact class: `ToggleSpaceCharge`

Toggle space charge. Available in IMPACT-Z v2.5+.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-14** |
| 5 | `unused` | float | `0.0` | *Unused; set to 0.* |
| 6 | `enable` | float | bool | `false` | Toggle space charge on or off. |

### rotate_beam_x

**Type code: `-16`** &nbsp;&middot;&nbsp; LUME-Impact class: `RotateBeamX`

Instantly rotate the beam about the horizontal x-axis.

Both positions and momenta are rotated, using the longitudinal momentum
of each particle.

Available in IMPACT-Z v2.7+.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Unused. |
| 4 | `type_id` | int | — | Element type code: **-16** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |
| 6 | `angle` | float | `0.0` | The rotation angle in radians (counter-clockwise for the beam, i.e. clockwise for the reference coordinate system). |

### rotate_beam_y

**Type code: `-17`** &nbsp;&middot;&nbsp; LUME-Impact class: `RotateBeamY`

Instantly rotate the beam about the vertical y-axis.

Both positions and momenta are rotated, using the longitudinal momentum
of each particle.

Available in IMPACT-Z v2.7+.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Unused. |
| 4 | `type_id` | int | — | Element type code: **-17** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |
| 6 | `angle` | float | `0.0` | The rotation angle in radians (counter-clockwise for the beam, i.e. clockwise for the reference coordinate system). |

### rotate_beam

**Type code: `-18`** &nbsp;&middot;&nbsp; LUME-Impact class: `RotateBeam`

Rotate the beam with respect to the longitudinal axis.

Both (x,y), and (px,py) are rotated.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-18** |
| 5 | `radius` | float | `0.0` | The radius in meters. |
| 6 | `tilt` | float | `0.0` | The rotation angle in radians. |

### beam_shift

**Type code: `-19`** &nbsp;&middot;&nbsp; LUME-Impact class: `BeamShift`

BeamShift shifts the beam longitudinally to the bunch centroid.so that <dt>=<dE>=0.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-19** |
| 5 | `unused` | float | `0.0` | *Unused; set to 0.* |

### beam_energy_spread

**Type code: `-20`** &nbsp;&middot;&nbsp; LUME-Impact class: `BeamEnergySpread`

Input element: a beam energy spread input element.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-20** |
| 5 | `radius` | float | `0.0` | The radius (not used). |
| 6 | `energy_spread` | float | `0.0` | The increased energy spread in eV. |

### shift_beam_centroid

**Type code: `-21`** &nbsp;&middot;&nbsp; LUME-Impact class: `ShiftBeamCentroid`

Shift the beam centroid in 6D phase space.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-21** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |
| 6 | `xshift` | float | `0.0` | Shift in x direction in meters. |
| 7 | `pxshift` | float | `0.0` | Shift in x momentum in radians. |
| 8 | `yshift` | float | `0.0` | Shift in y direction in meters. |
| 9 | `pyshift` | float | `0.0` | Shift in y momentum in radians. |
| 10 | `zshift` | float | `0.0` | Shift in z direction in degrees. |
| 11 | `pzshift` | float | `0.0` | Shift in z momentum in MeV. |

### integrator_type_switch

**Type code: `-25`** &nbsp;&middot;&nbsp; LUME-Impact class: `IntegratorTypeSwitch`

Input element: switch the integrator type.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `integrator_type` | int | `1` | Integrator type. See [IntegratorType](enums.md#integratortype). |
| 4 | `type_id` | int | — | Element type code: **-25** |
| 5 | `unused` | float | `0.0` | *Unused; set to 0.* |

### beam_kicker_by_rf_nonlinearity

**Type code: `-40`** &nbsp;&middot;&nbsp; LUME-Impact class: `BeamKickerByRFNonlinearity`

Beam kicker element that applies a longitudinal kick to the beam by the RF
nonlinearity.

Note that the linear part has been included in the map integrator and
subtracted.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-40** |
| 5 | `radius` | float | `0.0` | Radius in meters (not used). |
| 6 | `vmax` | float | `0.0` | Maximum voltage in volts (V). |
| 7 | `phi0` | float | `0.0` | Initial phase offset in degrees. |
| 8 | `harm` | int | `0` | Harmonic number with respect to the reference frequency. |

### rfcavity_structure_wakefield

**Type code: `-41`** &nbsp;&middot;&nbsp; LUME-Impact class: `RfcavityStructureWakefield`

Input element: read in RF cavity structure wakefield.

This element can read an external input file (see `file_id` below).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-41** |
| 5 | `unused` | float | `1.0` | *Unused; set to 0.* |
| 6 | `file_id` | float | `0.0` | The file ID to load from. |
| 7 | `enable_wakefield` | float | `0.0` | -1.0 RF off, 1.0 RF on, < 10 no transverse wakefield effects included |

### thin_lens_rf_deflector

**Type code: `-44`** &nbsp;&middot;&nbsp; LUME-Impact class: `ThinLensRFDeflector`

Apply a thin-lens RF deflecting cavity kick.

This is a transverse-longitudinal coupling (crab-cavity-like) kick: the
transverse momentum is kicked proportional to the longitudinal offset,
and the particle energy proportional to the transverse offset:
``px [mc] += strength * z [m] * gamma*beta`` and
``pt [mc^2] -= strength * x [m] * gamma`` (or ``y``/``py`` for vertical
deflection).

Available in IMPACT-Z v2.7+.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Unused. |
| 4 | `type_id` | int | — | Element type code: **-44** |
| 5 | `strength` | float | `0.0` | The integrated deflecting strength in 1/m. |
| 6 | `direction` | float | `0.0` | Deflection direction switch: >= 0 for horizontal, < 0 for vertical. |

### energy_modulation

**Type code: `-52`** &nbsp;&middot;&nbsp; LUME-Impact class: `EnergyModulation`

Input element: energy modulation (emulate laser heater).

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-52** |
| 5 | `beam_size` | float | `0.0` | The matched beam size in meters. |
| 6 | `laser_wavelength` | float | `0.0` | The laser wavelength in meters. |
| 7 | `energy_spread` | float | `0.0` | The uncorrelated energy spread in eV. |

### kick_beam_using_multipole

**Type code: `-55`** &nbsp;&middot;&nbsp; LUME-Impact class: `KickBeamUsingMultipole`

Input element: kick the beam using thin lens multipole.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Number of "map steps". Each half-step involves computing a map for that half-element which is computed by numerical integration. |
| 4 | `type_id` | int | — | Element type code: **-55** |
| 5 | `unused` | float | `0.0` | *Unused; set to 0.* |
| 6 | `k0` | float | `0.0` | Dipole strength. |
| 7 | `k1` | float | `0.0` | Quadrupole strength. |
| 8 | `k2` | float | `0.0` | Sextupole strength. |
| 9 | `k3` | float | `0.0` | Octupole strength. |
| 10 | `k4` | float | `0.0` | Decapole strength. |
| 11 | `k5` | float | `0.0` | Dodecapole strength. |

### halt_execution

**Type code: `-99`** &nbsp;&middot;&nbsp; LUME-Impact class: `HaltExecution`

Halt execution at this point in the input file.

This is useful if you have a big file and want to run part-way through it
without deleting a lot of lines.

| Col | Parameter | Type | Default | Description |
|----:|-----------|------|---------|-------------|
| 1 | `length` | float | `0.0` | Unused. |
| 2 | `steps` | int | `0` | Unused. |
| 3 | `map_steps` | int | `0` | Unused. |
| 4 | `type_id` | int | — | Element type code: **-99** |
