# Units and coordinates

## Internal coordinates

IMPACT-Z uses z as the independent variable and stores particle coordinates
in dimensionless internal units, scaled by the reference frequency ω = 2πf
(where f is `reference_frequency` from header line 11), the speed of light
c, and the particle rest mass m:

| Coordinate | Internal unit | To convert |
|-----------|----------------|------------|
| x, y | c/ω | multiply by c/ω to get meters |
| px, py | mc | divide by γβ to get x′, y′ in radians |
| phase (longitudinal position) | rad | Δt·ω |
| pt (energy deviation, E₀ − E) | mc² | multiply by mc² to get energy deviation |

These are the units used in `particle.in` (distribution type 19) and in the
particle dumps written by `write_full` (-2).

## Input Twiss conventions

Header lines 8–10 specify the initial distribution as an uncoupled
quadratic form per plane:

```text
alpha beta emittance mismatch mismatch_p offset offset_p
```

| Plane | beta unit | emittance unit |
|-------|-----------|----------------|
| x, y | m | m·rad (normalized) |
| z | degree/MeV | degree·MeV |

The mismatch factors scale the distribution in position and momentum; the
offsets displace it.

## Charge-to-mass ratio

Header line 7 lists q/m for each charge state, normalized such that the
reference particle has 1 AMU mass but possibly reduced charge. For example,
a proton: 1 / 938.272e6 ≈ 1.0658e-9. For an electron, q = −1 and
m = 0.511001e6 eV/c².

## Longitudinal quantities in output

In the standard diagnostic files, longitudinal position is reported as phase
in degrees, and longitudinal momentum as energy deviation in MeV
(see [Output files](output_files.md)).
