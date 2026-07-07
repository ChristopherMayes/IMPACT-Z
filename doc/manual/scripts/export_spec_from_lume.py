#!/usr/bin/env python
"""
Bootstrap the IMPACT-Z input-file specification (YAML) from the LUME-Impact
Pydantic models in ``impact.z``.

This walks the element registry (``impact.z.input.input_element_by_id``), the
header model (``impact.z.ImpactZInput``), and the enums in
``impact.z.constants`` and writes a machine-readable YAML description of the
ImpactZ.in file format: every element type code, every parameter in
file-column order with type/default/units/description, and every controlled
vocabulary.

Usage::

    python export_spec_from_lume.py [-o ../spec/impactz.yaml]

Requires an environment with lume-impact installed (e.g. lume-impact-dev).
"""

from __future__ import annotations

import argparse
import datetime
import enum
import inspect
import pathlib
import re
import typing

import pydantic
import pydantic.alias_generators
import yaml

import impact.z
import impact.z.constants
from impact.z.input import ImpactZInput, InputElement, input_element_by_id

SPEC_VERSION = "0.1"


def parse_numpydoc_fields(docstring: str | None) -> tuple[str, dict[str, str]]:
    """
    Parse a numpy-style docstring.

    Returns (summary, {field_name: description}) where fields are collected
    from the Attributes and/or Parameters sections.
    """
    if not docstring:
        return "", {}

    lines = inspect.cleandoc(docstring).splitlines()

    # Summary: everything up to the first section header.
    summary_lines: list[str] = []
    for i, line in enumerate(lines):
        if i + 1 < len(lines) and re.match(r"^\s*-{3,}\s*$", lines[i + 1]):
            break
        summary_lines.append(line)
    summary = "\n".join(summary_lines).strip()

    fields: dict[str, str] = {}
    section = None
    current: str | None = None
    desc_lines: list[str] = []

    def flush():
        nonlocal current, desc_lines
        if current is not None:
            fields[current] = " ".join(x.strip() for x in desc_lines).strip()
        current, desc_lines = None, []

    for i, line in enumerate(lines):
        header = line.strip()
        if i + 1 < len(lines) and re.match(r"^\s*-{3,}\s*$", lines[i + 1]):
            flush()
            section = header
            continue
        if re.match(r"^\s*-{3,}\s*$", line):
            continue
        if section not in ("Attributes", "Parameters"):
            continue
        m = re.match(r"^(\w+)\s*:\s*.+$", line.strip())
        if m and not line.startswith((" " * 5,)) and line.strip() == line.lstrip():
            flush()
            current = m.group(1)
        elif current is not None and line.strip():
            desc_lines.append(line)
    flush()
    return summary, fields


def _unwrap_annotated(ann) -> tuple[typing.Any, str | None]:
    """Strip typing.Annotated, returning (base type, units or None)."""
    units = None
    while typing.get_origin(ann) is typing.Annotated:
        args = typing.get_args(ann)
        for meta in args[1:]:
            if isinstance(meta, dict) and "units" in meta:
                units = str(meta["units"])
        ann = args[0]
    return ann, units


def _type_name(ann) -> str:
    ann, _ = _unwrap_annotated(ann)
    origin = typing.get_origin(ann)
    if origin is typing.Literal:
        return "int"
    if origin in (typing.Union, getattr(__import__("types"), "UnionType", None)):
        args = [a for a in typing.get_args(ann) if a is not type(None)]
        return " | ".join(dict.fromkeys(_type_name(a) for a in args))
    if origin in (list, typing.List):
        (arg,) = typing.get_args(ann)
        return f"list[{_type_name(arg)}]"
    if isinstance(ann, type):
        return ann.__name__
    return str(ann).replace("typing.", "")


def annotation_info(field: pydantic.fields.FieldInfo) -> dict:
    """Extract python type name, enum name, and units from a model field."""
    ann, units = _unwrap_annotated(field.annotation)
    out: dict = {"python_type": _type_name(ann)}

    if isinstance(ann, type) and issubclass(ann, enum.IntEnum):
        out["enum"] = ann.__name__
        out["python_type"] = "int"

    for meta in field.metadata:
        if isinstance(meta, dict) and "units" in meta:
            units = str(meta["units"])
    if units:
        out["units"] = units
    return out


def field_default(field: pydantic.fields.FieldInfo):
    default = field.get_default(call_default_factory=True)
    if isinstance(default, enum.IntEnum):
        return int(default)
    if isinstance(default, pathlib.Path):
        return str(default)
    if default is pydantic.fields.PydanticUndefined:
        return None
    return default


def export_element(code: int, cls: type[InputElement]) -> dict:
    summary, descriptions = parse_numpydoc_fields(cls.__doc__)
    meta = cls._impactz_metadata_

    file_fields = [name for name in cls._impactz_fields_ if name in cls.model_fields]
    parameters = []
    for column, name in enumerate(file_fields, start=1):
        field = cls.model_fields[name]
        if name == "type_id":
            parameters.append(
                {"column": column, "name": name, "python_type": "int", "value": code}
            )
            continue
        param = {"column": column, "name": name}
        param.update(annotation_info(field))
        param["default"] = field_default(field)
        desc = descriptions.get(name) or field.description
        if desc:
            param["description"] = desc
        if name.startswith("unused"):
            param["unused"] = True
        parameters.append(param)

    return {
        "type_code": code,
        "name": pydantic.alias_generators.to_snake(cls.__name__),
        "class_name": cls.__name__,
        "category": "beamline_element" if code >= 0 else "control",
        "summary": summary,
        "has_input_file": meta.has_input_file,
        "has_output_file": meta.has_output_file,
        "parameters": parameters,
    }


def export_header() -> list[dict]:
    """
    Export the ImpactZ.in header (lines 1-11) from ImpactZInput.

    The line grouping is parsed from the ``# Line N`` comments in the source
    of the ImpactZInput class, so it stays in sync with lume-impact.
    """
    src = inspect.getsource(ImpactZInput)
    line_of_field: dict[str, int] = {}
    current_line: int | None = None
    for src_line in src.splitlines():
        m = re.match(r"\s*# Line (\d+)", src_line)
        if m:
            current_line = int(m.group(1))
            continue
        m = re.match(r"\s{4}(\w+)\s*:", src_line)
        if m and current_line is not None:
            line_of_field[m.group(1)] = current_line

    _, descriptions = parse_numpydoc_fields(ImpactZInput.__doc__)

    lines: dict[int, dict] = {}
    for name, field in ImpactZInput.model_fields.items():
        file_line = line_of_field.get(name)
        if file_line is None or name == "lattice":
            continue
        entry = {"name": name}
        entry.update(annotation_info(field))
        entry["default"] = field_default(field)
        desc = descriptions.get(name) or field.description
        if desc:
            entry["description"] = desc
        lines.setdefault(file_line, {"line": file_line, "fields": []})
        lines[file_line]["fields"].append(entry)

    return [lines[k] for k in sorted(lines)]


def export_enums() -> dict:
    enums = {}
    for name in dir(impact.z.constants):
        obj = getattr(impact.z.constants, name)
        if isinstance(obj, type) and issubclass(obj, enum.IntEnum) and len(obj):
            enums[name] = {member.name: int(member.value) for member in obj}
    return enums


def main(output: pathlib.Path) -> None:
    codes = sorted(input_element_by_id, key=lambda c: (c < 0, abs(c)))
    spec = {
        "spec_version": SPEC_VERSION,
        "code": "IMPACT-Z",
        "code_version": "2.7.1",
        "generated_by": pathlib.Path(__file__).name,
        "generated_from": f"lume-impact impact.z (impact version {impact.__version__})",
        "generated_date": datetime.date.today().isoformat(),
        "enums": export_enums(),
        "header_lines": export_header(),
        "elements": [export_element(c, input_element_by_id[c]) for c in codes],
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as fp:
        yaml.dump(spec, fp, sort_keys=False, default_flow_style=False, width=88)
    n_params = sum(len(e["parameters"]) for e in spec["elements"])
    print(f"Wrote {output}: {len(spec['elements'])} elements, {n_params} parameters")


if __name__ == "__main__":
    import impact

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent.parent / "spec" / "impactz.yaml",
    )
    args = parser.parse_args()
    main(args.output)
