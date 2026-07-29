"""Fail when the public ecosystem manifest or quickstart pins lag behind PyPI."""

from __future__ import annotations

import argparse
import json
import re
import tomllib
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "ecosystem.toml"
CREATE_HAYATE_PIN = re.compile(r"create-hayate==(\d+\.\d+\.\d+)")
CREATE_HAYATE_RELEASE = re.compile(r"\bcreate-hayate (\d+\.\d+\.\d+)\b")
PYPI_ORIGIN = "https://pypi.org"
USER_AGENT = "hayatepy-docs-release-freshness/1"

FetchProject = Callable[[str], Mapping[str, Any]]


def _normalize_project_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def _public_packages(data: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    packages = data.get("packages")
    if not isinstance(packages, list):
        raise ValueError("ecosystem manifest needs a package list")
    return [package for package in packages if isinstance(package, Mapping) and package.get("pypi")]


def fetch_pypi_project(name: str) -> Mapping[str, Any]:
    request = Request(
        f"{PYPI_ORIGIN}/pypi/{name}/json",
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
    )
    with urlopen(request, timeout=10) as response:
        payload = json.load(response)
    if not isinstance(payload, Mapping):
        raise ValueError(f"PyPI returned a non-object payload for {name}")
    return payload


def validate_pypi_versions(
    data: Mapping[str, Any], fetch_project: FetchProject = fetch_pypi_project
) -> list[str]:
    failures: list[str] = []
    for package in _public_packages(data):
        expected_name = str(package["name"])
        expected_version = str(package["version"])
        payload = fetch_project(expected_name)
        info = payload.get("info")
        if not isinstance(info, Mapping):
            failures.append(f"{expected_name}: PyPI payload has no info object")
            continue
        published_name = str(info.get("name", ""))
        published_version = str(info.get("version", ""))
        if _normalize_project_name(published_name) != _normalize_project_name(expected_name):
            failures.append(
                f"{expected_name}: PyPI returned project {published_name or '<missing>'}"
            )
        if published_version != expected_version:
            failures.append(
                f"{expected_name}: manifest has {expected_version}, "
                f"PyPI latest is {published_version or '<missing>'}"
            )
    return failures


def validate_create_hayate_pins(root: Path, data: Mapping[str, Any]) -> list[str]:
    versions = {str(package["name"]): str(package["version"]) for package in _public_packages(data)}
    expected = versions.get("create-hayate")
    if expected is None:
        return ["ecosystem manifest has no public create-hayate package"]

    failures: list[str] = []
    references = 0
    for path in sorted((root / "docs").rglob("*.md")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in CREATE_HAYATE_PIN.finditer(line):
                references += 1
                if match.group(1) != expected:
                    relative = path.relative_to(root)
                    failures.append(
                        f"{relative}:{line_number}: create-hayate pin "
                        f"{match.group(1)} must match manifest {expected}"
                    )
            for match in CREATE_HAYATE_RELEASE.finditer(line):
                if match.group(1) != expected:
                    relative = path.relative_to(root)
                    failures.append(
                        f"{relative}:{line_number}: create-hayate release "
                        f"{match.group(1)} must match manifest {expected}"
                    )
    if references == 0:
        failures.append("documentation contains no exact create-hayate release pin")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    data = tomllib.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = validate_pypi_versions(data)
    failures.extend(validate_create_hayate_pins(ROOT, data))
    if failures:
        raise SystemExit("\n".join(failures))
    print("Validated public PyPI releases and documentation pins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
