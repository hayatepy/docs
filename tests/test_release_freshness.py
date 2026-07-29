from __future__ import annotations

from pathlib import Path

from scripts.check_release_freshness import (
    validate_create_hayate_pins,
    validate_pypi_versions,
)


def manifest(version: str = "0.13.1") -> dict:
    return {
        "packages": [
            {
                "name": "create-hayate",
                "version": version,
                "pypi": "https://pypi.org/project/create-hayate/",
            },
            {
                "name": "source-only",
                "version": "0.1.0",
            },
        ]
    }


def test_public_release_matches_manifest() -> None:
    failures = validate_pypi_versions(
        manifest(),
        lambda name: {"info": {"name": "create_hayate", "version": "0.13.1"}},
    )

    assert failures == []


def test_public_release_drift_is_reported() -> None:
    failures = validate_pypi_versions(
        manifest("0.13.0"),
        lambda name: {"info": {"name": name, "version": "0.13.1"}},
    )

    assert failures == ["create-hayate: manifest has 0.13.0, PyPI latest is 0.13.1"]


def test_documentation_pin_must_match_manifest(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "start.md").write_text(
        "uvx --from create-hayate==0.13.0 create-hayate demo\n",
        encoding="utf-8",
    )

    failures = validate_create_hayate_pins(tmp_path, manifest())

    assert failures == ["docs/start.md:1: create-hayate pin 0.13.0 must match manifest 0.13.1"]


def test_documentation_requires_an_exact_release_pin(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()

    assert validate_create_hayate_pins(tmp_path, manifest()) == [
        "documentation contains no exact create-hayate release pin"
    ]


def test_documentation_release_prose_must_match_manifest(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "evidence.md").write_text(
        "uvx --from create-hayate==0.13.1 create-hayate demo\n"
        "Current evidence uses create-hayate 0.13.0.\n",
        encoding="utf-8",
    )

    failures = validate_create_hayate_pins(tmp_path, manifest())

    assert failures == [
        "docs/evidence.md:2: create-hayate release 0.13.0 must match manifest 0.13.1"
    ]


def test_current_documentation_release_prose_is_accepted(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "evidence.md").write_text(
        "uvx --from create-hayate==0.13.1 create-hayate demo\n"
        "Current evidence uses create-hayate 0.13.1.\n",
        encoding="utf-8",
    )

    assert validate_create_hayate_pins(tmp_path, manifest()) == []
