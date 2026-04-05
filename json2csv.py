#!/usr/bin/env python3
"""json2csv -- convert JSON files to CSV with smart column detection."""

from __future__ import annotations

import csv
import json
import pathlib
import sys


def _flatten(obj: dict, prefix: str = "") -> dict:
    out: dict = {}
    for k, v in obj.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(_flatten(v, key))
        elif isinstance(v, list):
            out[key] = json.dumps(v)
        else:
            out[key] = v
    return out


def convert(
    input_path: str,
    output_path: str | None = None,
    delimiter: str = ",",
) -> str:
    inp = pathlib.Path(input_path)
    data = json.loads(inp.read_text())

    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON array or object, got {type(data).__name__}")

    flat = [_flatten(item) for item in data]
    columns = []
    seen = set()
    for row in flat:
        for k in row:
            if k not in seen:
                columns.append(k)
                seen.add(k)

    if output_path is None:
        output_path = str(inp.with_suffix(".csv"))

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(flat)

    return output_path


def inspect(input_path: str) -> None:
    inp = pathlib.Path(input_path)
    data = json.loads(inp.read_text())
    if isinstance(data, dict):
        data = [data]

    print(f"File: {inp}")
    print(f"Records: {len(data)}")
    if not data:
        return

    flat = [_flatten(data[0])]
    cols = list(flat[0].keys())
    print(f"Columns ({len(cols)}):")
    for c in cols:
        val = flat[0][c]
        val_str = repr(val)[:60]
        print(f"  {c} -- {val_str}")


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ('--help', '-h'):
        print('Usage:')
        print('  python -m json2csv convert input.json [output.csv]')
        print('  python -m json2csv inspect input.json')
        print('  python -m json2csv convert --delimiter "|" data.json')
        return

    cmd = sys.argv[1]
    if cmd == 'inspect':
        inspect(sys.argv[2])
    elif cmd == 'convert':
        inp = sys.argv[2]
        out = sys.argv[3] if len(sys.argv) > 3 else None
        delim = ","
        if '--delimiter' in sys.argv:
            idx = sys.argv.index('--delimiter')
            if idx + 1 < len(sys.argv):
                delim = sys.argv[idx + 1]
        result = convert(inp, out, delim)
        print(f"Written: {result}")
    else:
        print(f'Unknown command: {cmd}')
        sys.exit(1)


if __name__ == '__main__':
    main()
