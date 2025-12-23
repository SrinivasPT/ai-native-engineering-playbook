"""Architecture linter (template).

Purpose
- Enforce import boundaries (“architecture as code”).
- Fail fast when forbidden imports appear.

This is a minimal, working Python example.
If your repo is not Python, keep the concept and implement the equivalent check
for your language/tooling.

Usage
  python arch_linter.py --root src

Exit codes
- 0: no violations
- 2: violations found
"""

from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Violation:
    file: Path
    lineno: int
    imported: str
    rule: str


# Define boundaries as "module prefix" -> list of forbidden module prefixes.
# Example: "src.features" cannot import anything in "src.infra".
FORBIDDEN_IMPORTS: dict[str, list[str]] = {
    "src.features": ["src.infra"],
    "src.api": ["src.infra"],
}


def _iter_python_files(root: Path) -> list[Path]:
    return [
        p
        for p in root.rglob("*.py")
        if p.is_file() and "venv" not in p.parts and ".venv" not in p.parts
    ]


def _module_prefix_for_path(root: Path, file_path: Path) -> str:
    rel = file_path.relative_to(root)
    parts = (root.name, *rel.with_suffix("").parts)
    # Convert to dotted module path-like prefix.
    return ".".join(parts)


def _imported_modules(tree: ast.AST) -> list[tuple[int, str]]:
    imports: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((node.lineno or 0, alias.name))
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append((node.lineno or 0, node.module))
    return imports


def _violations_for_file(root: Path, file_path: Path) -> list[Violation]:
    try:
        source = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        source = file_path.read_text(encoding="utf-8", errors="replace")

    try:
        tree = ast.parse(source)
    except SyntaxError:
        # Treat parse errors as out-of-scope for the architecture linter.
        return []

    file_prefix = _module_prefix_for_path(root, file_path)
    violations: list[Violation] = []

    # Find the first matching rule prefix.
    for rule_prefix, forbidden_prefixes in FORBIDDEN_IMPORTS.items():
        if not file_prefix.startswith(rule_prefix):
            continue

        for lineno, imported in _imported_modules(tree):
            for forbidden in forbidden_prefixes:
                if imported == forbidden or imported.startswith(forbidden + "."):
                    violations.append(
                        Violation(
                            file=file_path,
                            lineno=lineno,
                            imported=imported,
                            rule=f"{rule_prefix} must not import {forbidden}",
                        )
                    )
        break

    return violations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Path to source root, e.g. src")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"arch_linter: root not found: {root}")
        return 2

    all_violations: list[Violation] = []
    for py_file in _iter_python_files(root):
        all_violations.extend(_violations_for_file(root, py_file))

    if not all_violations:
        print("arch_linter: OK")
        return 0

    print("arch_linter: VIOLATIONS")
    for v in all_violations:
        print(f"- {v.file}:{v.lineno} imports {v.imported} ({v.rule})")

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
