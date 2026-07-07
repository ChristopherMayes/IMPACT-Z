# IMPACT-Z manual sources

This directory contains the sources for the IMPACT-Z user manual.

## Layout

- `spec/impactz.yaml` — machine-readable specification of the `ImpactZ.in`
  input format: header lines, every element type code with its parameters in
  file-column order, and enumerations. This is the single source of truth
  for the reference documentation, and is consumable by external tools
  (e.g. [LUME-Impact](https://github.com/ChristopherMayes/lume-impact)).
- `docs/` — manual pages (markdown). `docs/reference/` is **generated** from
  the spec; do not edit those pages by hand.
- `scripts/generate_reference.py` — regenerates `docs/reference/` from the
  spec.
- `scripts/export_spec_from_lume.py` — the bootstrap script originally used
  to create the spec from LUME-Impact's `impact.z` Pydantic models.
- `legacy/` — the old v2.7 Word manual converted to markdown, kept as
  reference material.
- `mkdocs.yml` — site configuration.

## Building the manual

```bash
pip install mkdocs-material
cd doc/manual
mkdocs serve    # live preview at http://127.0.0.1:8000
mkdocs build    # static site in site/
```

## Updating the reference

1. Edit `spec/impactz.yaml`.
2. Run `python scripts/generate_reference.py`.
3. Commit both the spec and the regenerated pages.
