# Running IMPACT-Z

## Installing

Prebuilt executables are available from conda-forge:

```bash
# Serial
conda install -c conda-forge impact-z
# OpenMPI
conda install -c conda-forge impact-z=*=mpi_openmpi*
# MPICH
conda install -c conda-forge impact-z=*=mpi_mpich*
```

This provides `ImpactZexe` (serial) or `ImpactZexe-mpi` (parallel) on your
`PATH`.

## Building from source

The source builds with CMake and a Fortran compiler (gfortran works; all
compilers and dependencies are available from conda-forge):

```bash
conda create -n impactz-build -c conda-forge compilers cmake openmpi
conda activate impactz-build

# Serial
cmake -S src/ -B build-single
cmake --build build-single -j 4

# MPI
cmake -S src/ -B build-mpi -DUSE_MPI=ON
cmake --build build-mpi -j 4
```

See `src/INSTRUCTIONS.md` in the repository for more detail, including
system-wide installs.

## Running

IMPACT-Z always reads `ImpactZ.in` from the current working directory and
writes its output files there:

```bash
# Serial
./ImpactZexe

# Parallel
mpirun -n 16 ImpactZexe-mpi
```

The number of MPI ranks must equal `ncpu_y × ncpu_z` from line 1 of
`ImpactZ.in`. For the serial executable both must be 1.

While running, the console shows the current element number, element type
code, position z, step within the element, and total steps.

To stop a run early, interrupt it with ++ctrl+c++. A
[`halt_execution`](reference/elements.md#halt_execution) (-99) element can
be placed in the lattice to stop the simulation part-way through a large
input file without deleting lines.

## Examples

The repository contains worked examples under `examples/`, each with a
complete `ImpactZ.in` and any required auxiliary files (`rfdata*.in`,
`particle.in`). `examples/Example1` also includes reference output files
for comparison.

## Running via LUME-Impact

The [LUME-Impact](https://github.com/ChristopherMayes/lume-impact) Python
package can generate `ImpactZ.in` programmatically, run the code, and parse
all output into structured Python objects:

```python
from impact.z import ImpactZ, ImpactZInput

input = ImpactZInput.from_file("ImpactZ.in")
I = ImpactZ(input)
output = I.run()
```

## Utility programs

- `utilities/RFcoef.f90` — prepares Fourier expansion coefficients of RF or
  solenoid fields for use with the Lorentz integrator.
- `utilities/Engscan.py` — single-cavity phase scan.
- `utilities/phaseOptZ.py` — sets RF driven phases from user-specified
  design phases.
- `utilities/Tr2Impact.f90` — input conversion helper.
