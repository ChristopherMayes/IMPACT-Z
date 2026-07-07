# The input file

IMPACT-Z reads a single main input file, **`ImpactZ.in`**, from the working
directory. Depending on the settings it may also read auxiliary files:
external RF/field data (`rfdataN.in`), an initial particle distribution
(`particle.in`), and files used by specific control elements.

## Formatting rules

- The file is read with Fortran free-format (list-directed) reads.
- Any line starting with `!` is a comment and is skipped.
- **Every lattice line must end with `/`.** The read statement for a lattice
  line expects up to 28 numbers; the `/` terminates the read early so that
  unspecified trailing parameters default to zero. Omitting it will crash or
  misread the file.
- Text after the `/` may be used as an element name/comment.

## Structure

`ImpactZ.in` has two sections:

1. **Header** — eleven lines of global settings: processor layout,
   particle number, integrator choice, space-charge grid, initial
   distribution, and reference-particle parameters.
2. **Lattice** — one line per beamline element, in order.

### Header

The eleven header lines, in order (see the
[header reference](reference/header.md) for every field):

| Line | Contents |
|-----:|----------|
| 1 | Processor layout: `ncpu_y ncpu_z` (product must equal the number of MPI ranks) |
| 2 | `seed n_particle integrator_type err diagnostic_type` |
| 3 | Space-charge grid and boundary: `nx ny nz boundary_type radius_x radius_y z_period_size` |
| 4 | Distribution: `distribution restart subcycle nbunch` |
| 5 | Particle count per charge state (`nbunch` values) |
| 6 | Current per charge state, in Amperes (`nbunch` values) |
| 7 | Charge-to-mass ratio per charge state (`nbunch` values) |
| 8 | x-plane Twiss/distribution parameters (7 values) |
| 9 | y-plane Twiss/distribution parameters (7 values) |
| 10 | z-plane Twiss/distribution parameters (7 values) |
| 11 | Reference particle: `average_current kinetic_energy mass charge frequency initial_phase` |

The Twiss lines 8–10 each contain:

```text
alpha beta emittance mismatch mismatch_p offset offset_p
```

For x and y, `beta` is in meters and the emittance is the *normalized*
emittance in m·rad. For z, `beta` is in degrees/MeV and the emittance in
degree·MeV. The distribution in each plane is a quadratic form with no
coupling between planes. See [Units and coordinates](units.md).

!!! warning
    The z-plane `alpha` (line 10, first value) must be non-zero; a value of
    exactly zero can crash the compute-domain calculation. Use a tiny value
    such as `1e-9` if zero is intended.

The initial distribution type (line 4) is selected by an integer code such
as uniform, Gaussian, waterbag, KV, multi-charge-state variants, or
read-from-file. See
[DistributionType](reference/enums.md#distributiontype). Codes for reading
external distributions:

- `19` — read `particle.in` in IMPACT-Z format (first line: particle count;
  then one particle per line in internal units, see
  [Units and coordinates](units.md)).
- `22` — read `particle.in` in Elegant format.
- `35` — read `particle.in` in IMPACT-T output format.
- `199` — parallel read of per-processor binary files `fort.(x+myid)`.

### Lattice

Each non-comment line after the header defines one element:

```text
length steps map_steps type v5 v6 ... /
```

- `length` — element length in meters.
- `steps` — number of space-charge kicks through the element. Each step is
  a half-step map, a space-charge kick, then another half-step map.
- `map_steps` — number of numerical-integration steps used to compute the
  transfer map for each half-step. (For a few control elements this column
  is reused as a file ID or mode switch.)
- `type` — the element type code.
- remaining columns — element parameters.

Positive type codes are physical beamline elements (drift, quadrupole,
dipole, RF cavities, ...). Negative type codes are zero-length control and
diagnostic operations applied at that point in the lattice (write particles,
rotate beam, toggle space charge, ...). The full list with all parameters is
in the [element reference](reference/elements.md).

Example lattice section (drift + quad + drift + RF cavity):

```text
0.062082 1 1 0 1.0 /
0.05 3 1 1 16.442385 0 1.0 0. 0. 0. 0. 0. /
0.062082 1 1 0 1.0 /
0.948049 80 1 104 34000000.0 650000000.0 96.805648 1 1.0 /
```

## Auxiliary input files

### rfdataN.in

Elements with type codes above 100 (RF structures) and some others read
external field data from `rfdataN.in`, where `N` is the element's `file_id`
parameter. Depending on the element and integrator, the file contains either
Fourier expansion coefficients of the on-axis field (prepared with
`utilities/RFcoef.f90`) or discrete field data. A negative `file_id` selects
a simple built-in sinusoidal cavity model instead (map integrator only).

### particle.in

Used when the distribution type is a read-in code (see above). For the
IMPACT-Z format, the first line is the total particle number and each
subsequent line is one particle in internal units — the same 9-column format
written by the `write_full` (-2) element:

```text
x px y py phase delta_energy charge_to_mass charge_per_macroparticle id
```

### Other files

- `fort.N` (6×6 matrix, six rows) — read by the
  [`external_linear_map_kick`](reference/elements.md#external_linear_map_kick)
  (-12) element.
- `rfdataN.in` wakefield tables (4 columns: bunch-length coordinate,
  longitudinal wake, x wake, y wake) — read by
  [`rfcavity_structure_wakefield`](reference/elements.md#rfcavity_structure_wakefield)
  (-41).
