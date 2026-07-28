from __future__ import annotations

from pathlib import Path

from scripts.check_site import validate


def write_page(root: Path, relative: str, *, href: str = "/target/") -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <title>Page</title>
  <meta name="description" content="Useful page">
  <link rel="canonical" href="https://hayate-docs.yusuke8h.workers.dev/">
</head>
<body><main><h1>Page</h1><a href="{href}">Target</a></main></body>
</html>
""",
        encoding="utf-8",
    )


def test_validates_nested_directory_links(tmp_path: Path) -> None:
    write_page(tmp_path, "index.html")
    write_page(tmp_path, "target/index.html", href="/")
    assert validate(tmp_path) == []


def test_reports_broken_internal_link(tmp_path: Path) -> None:
    write_page(tmp_path, "index.html", href="/missing/")
    assert validate(tmp_path) == ["index.html: broken internal link '/missing/'"]
