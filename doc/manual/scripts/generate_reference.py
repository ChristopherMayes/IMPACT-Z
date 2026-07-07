#!/usr/bin/env python
"""
Generate the manual's reference pages from the machine-readable spec.

Reads ``doc/manual/spec/impactz.yaml`` and writes:

* ``docs/reference/header.md`` - the ImpactZ.in header lines
* ``docs/reference/elements.md`` - every beamline/control element
* ``docs/reference/enums.md`` - controlled vocabularies

Run this after editing the spec, then commit the regenerated pages::

    python generate_reference.py
"""

from __future__ import annotations

import pathlib

import yaml

MANUAL = pathlib.Path(__file__).parent.parent
SPEC = MANUAL / "spec" / "impactz.yaml"
REFERENCE = MANUAL / "docs" / "reference"

GENERATED_NOTE = (
    "<!-- This page is generated from spec/impactz.yaml by "
    "scripts/generate_reference.py. Do not edit by hand. -->\n"
)


def escape_cell(text: str) -> str:
    """Make text safe for a one-line markdown table cell."""
    return " ".join(str(text).split()).replace("|", "\\|")


def format_default(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return f"`{str(value).lower()}`"
    return f"`{value}`"


def parameter_table(parameters: list[dict]) -> list[str]:
    lines = [
        "| Col | Parameter | Type | Default | Description |",
        "|----:|-----------|------|---------|-------------|",
    ]
    for param in parameters:
        name = param["name"]
        if param.get("unused"):
            desc = "*Unused; set to 0.*"
        else:
            desc = escape_cell(param.get("description", ""))
        if param.get("enum"):
            desc += f" See [{param['enum']}](enums.md#{param['enum'].lower()})."
        if "value" in param:  # the fixed type_id column
            lines.append(
                f"| {param['column']} | `{name}` | int | — | "
                f"Element type code: **{param['value']}** |"
            )
            continue
        lines.append(
            f"| {param['column']} | `{name}` | {param.get('python_type', '')} "
            f"| {format_default(param.get('default'))} | {desc} |"
        )
    return lines


def write_elements(spec: dict) -> None:
    out = [
        GENERATED_NOTE,
        "# Element reference",
        "",
        "Each lattice line in `ImpactZ.in` has the form:",
        "",
        "```text",
        "length steps map_steps type v5 v6 ... /",
        "```",
        "",
        "where `type` selects the element and the remaining columns are the",
        "parameters listed below. Trailing parameters may be omitted; they",
        "default to zero. The `/` terminates the line.",
        "",
        "Positive type codes are physical beamline elements; negative type codes",
        "are zero-length control and diagnostic operations. A negative type code",
        "not listed below is **silently ignored** by IMPACT-Z v2.7.1 (no warning",
        "is printed), with one exception: type `-11` prints \"Not available in",
        "current version!\" and stops the run.",
        "",
    ]

    groups = [
        ("Beamline elements", [e for e in spec["elements"] if e["type_code"] >= 0]),
        ("Control and diagnostic elements", [e for e in spec["elements"] if e["type_code"] < 0]),
    ]

    # Index table
    out += ["## Element type codes", ""]
    out += [
        "| Code | Element | Category |",
        "|-----:|---------|----------|",
    ]
    for _, elements in groups:
        for ele in elements:
            anchor = ele["name"]
            out.append(
                f"| {ele['type_code']} | [`{ele['name']}`](#{anchor}) "
                f"| {ele['category'].replace('_', ' ')} |"
            )
    out.append("")

    for title, elements in groups:
        out += [f"## {title}", ""]
        for ele in elements:
            out += [f"### {ele['name']}", ""]
            out += [f"**Type code: `{ele['type_code']}`**", ""]
            if ele.get("summary"):
                out += [ele["summary"], ""]
            if ele.get("has_input_file"):
                out += [
                    "This element can read an external input file "
                    "(see `file_id` below).",
                    "",
                ]
            out += parameter_table(ele["parameters"])
            out.append("")

    (REFERENCE / "elements.md").write_text("\n".join(out))


def write_header(spec: dict) -> None:
    out = [
        GENERATED_NOTE,
        "# Header reference",
        "",
        "The first eleven (non-comment) lines of `ImpactZ.in` are global",
        "settings, in the fixed order below. Lines starting with `!` are",
        "comments and are skipped.",
        "",
    ]
    for line in spec["header_lines"]:
        names = ", ".join(f"`{f['name']}`" for f in line["fields"])
        out += [f"## Line {line['line']}: {names}", ""]
        out += [
            "| Field | Type | Default | Description |",
            "|-------|------|---------|-------------|",
        ]
        for field in line["fields"]:
            desc = escape_cell(field.get("description", ""))
            if field.get("enum"):
                desc += f" See [{field['enum']}](enums.md#{field['enum'].lower()})."
            out.append(
                f"| `{field['name']}` | {field.get('python_type', '')} "
                f"| {format_default(field.get('default'))} | {desc} |"
            )
        out.append("")

    (REFERENCE / "header.md").write_text("\n".join(out))


def write_enums(spec: dict) -> None:
    out = [
        GENERATED_NOTE,
        "# Enumerations",
        "",
        "Integer flags in the input file with fixed sets of allowed values.",
        "",
    ]
    for name, members in spec["enums"].items():
        out += [f"## {name}", ""]
        out += ["| Name | Value |", "|------|------:|"]
        for member, value in members.items():
            out.append(f"| `{member}` | {value} |")
        out.append("")

    (REFERENCE / "enums.md").write_text("\n".join(out))


def main() -> None:
    with open(SPEC) as fp:
        spec = yaml.safe_load(fp)

    REFERENCE.mkdir(parents=True, exist_ok=True)
    write_header(spec)
    write_elements(spec)
    write_enums(spec)
    print(f"Wrote reference pages to {REFERENCE}")


if __name__ == "__main__":
    main()
