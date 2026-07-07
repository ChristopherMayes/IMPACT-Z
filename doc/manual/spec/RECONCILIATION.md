# Spec reconciliation record

The spec (`impactz.yaml`) was bootstrapped from LUME-Impact's `impact.z`
Pydantic models and then audited parameter-by-parameter against the
IMPACT-Z v2.7.1 Fortran source (`src/Contrl/Input.f90`,
`src/Contrl/AccSimulator.f90`, `src/Appl/*.f90`, `src/Contrl/Output.f90`)
and against the legacy v2.7 Word manual (`../legacy/`). This file records
what the audit found (July 2026).

## Corrections applied (fixed in LUME-Impact and re-exported)

| Element | Issue |
|---------|-------|
| 1 `quadrupole` | `k1` (col 5) is the field gradient B1 [T/m] in the default mode (`file_id` ≥ 0); it is a MAD-style K1 [1/m²] only when −10 < `file_id` < 0. The earlier claim that it is always 1/m² was wrong. |
| 4 `dipole` | Entrance/exit pole-face curvatures (cols 11–12) are [1/m], not [rad]. |
| 6 `wiggler` | Max field strength is in Tesla; `file_id` is a real field-file ID. |
| 106 `traveling_wave_rf_cavity` | Rotation-error y/z descriptions were copy-pasted from x. |
| −2 `write_full` | Sample frequency is column **5** (`drange(2)`); column 6 is never read. Previously swapped. |
| −3 `density_profile_input` | Writes *accumulated* density to `RadDens.data`, `Xprof.data`, `Yprof.data`; only radius/xmax/ymax are read. |
| −7 `write_phase_space_info` | Column 3 is the base file ID; rank *r* writes `fort.(file_id+r)`. |
| −41 `rfcavity_structure_wakefield` | Column 5 is the wakefield scale factor `scwk`, previously mislabeled "unused". |

## Errors in the legacy v2.7 Word manual

- The example lines for **−16**, **−17**, and **−20** all misprint the type
  code as `-18` (copy-paste errors).
- The **−2** example (`0. 0 N -2 0.0 10 /`) puts the sample frequency in
  column 6, but the code reads it from column 5.
- The **−41** description says the first parameter is "not used"; it is the
  wakefield scale factor.
- The **−25** entry contains stray text copied from −21.
- The time-domain diagnostics (`fort.34`–`fort.40`, `fort.48`) are not
  documented.

## Fortran issues found during the audit (upstream candidates)

- **−6 `density_3_d`** (`AccSimulator.f90` ~line 901): the branch does not
  call `getparam_BeamLineElem` before using `drange`, so the frame ranges
  are stale values from a previously processed element.
- **−8 `write_slice_info`** (`AccSimulator.f90` ~line 919):
  `if(betax0.eq.0.0d0) betay0=1.0d0` — the condition should test `betay0`.
- Unhandled negative type codes fall through **silently** (no warning);
  only −11 aborts and −99 exits cleanly.
- Stale module-header comments in `src/Appl/Dipole.f90` (parameter list) and
  a typo in `src/Appl/DTL.f90` (Param(17) says "x misalignment for Quad 2",
  should be y).

## Known gaps / future work

- The spec's `units:` field is unpopulated; units currently live in the
  description text. A structured pass adding `units:` per parameter (the
  audit produced a complete table) would let tools do conversions.
- Distribution type codes 22 (Elegant read), 35 (IMPACT-T read), and 199
  (parallel binary read) are accepted by the Fortran but not part of the
  `DistributionType` enum exported from LUME-Impact.
