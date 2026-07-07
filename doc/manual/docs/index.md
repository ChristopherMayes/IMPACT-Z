# IMPACT-Z

IMPACT-Z is a three-dimensional parallel/serial particle-in-cell (PIC) code
for simulating intense charged-particle beams in accelerators. It uses the
longitudinal position *z* as the independent variable and can transport beams
through drifts, quadrupoles, solenoids, dipoles, multipoles, wigglers, and a
variety of RF accelerating structures, using either a linear map integrator
or a nonlinear Lorentz integrator.

Key capabilities:

- **Space charge**: 3D space-charge fields solved on a grid, with several
  boundary-condition options (open, periodic, round or rectangular pipe).
- **Map-based RF cavities**: gap transfer maps are computed on the fly from
  externally supplied RF field data (e.g. Superfish output), avoiding
  fine-scale integration of millions of particles through rapidly varying
  cavity fields. Fine-scale integration is used only to compute the maps.
- **Multiple charge states**: beams composed of several charge states,
  each with its own current and charge-to-mass ratio.
- **Machine errors**: field errors, misalignment errors, and rotation
  errors, for error studies.
- **Collective effects**: 1D CSR in bends (and downstream elements),
  RF structure wakefields, and a laser-heater energy modulation model.
- **Parallelism**: runs serially or on MPI parallel computers with a 2D
  (y, z) processor decomposition.

This manual documents **IMPACT-Z version 2.7.1**.

## About this manual

The reference sections of this manual are generated from a machine-readable
specification of the input format,
[`spec/impactz.yaml`](https://github.com/impact-lbl/IMPACT-Z/tree/master/doc/manual/spec),
which is cross-checked against the Fortran source. External tools can parse
the same specification to interpret or compose IMPACT-Z input files.

- [The input file](input_file.md) — structure of `ImpactZ.in` and the
  auxiliary input files.
- [Header reference](reference/header.md) — the global settings lines.
- [Element reference](reference/elements.md) — every element type code and
  its parameters.
- [Running IMPACT-Z](running.md) — installing, building, and running.
- [Output files](output_files.md) — what the code writes and the meaning of
  every column.
- [Units and coordinates](units.md) — the internal coordinate system and
  unit conversions.

## Authors and license

IMPACT-Z was written by Ji Qiang (Lawrence Berkeley National Laboratory),
with contributions from collaborators. Copyright © The Regents of the
University of California. See the
[license](https://github.com/impact-lbl/IMPACT-Z/blob/master/license.txt)
for terms of use.

A detailed description of the physics models can be found in:
J. Qiang, R. D. Ryne, S. Habib, V. Decyk, "An Object-Oriented Parallel
Particle-in-Cell Code for Beam Dynamics Simulation in Linear Accelerators,"
*J. Comput. Phys.* **163**, 434 (2000).
