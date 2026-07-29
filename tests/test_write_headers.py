from __future__ import annotations

import base64
import hashlib
from pathlib import Path

import pytest

from scripts.write_headers import render_headers, script_hashes, write_headers


def expected_hash(script: str) -> str:
    digest = hashlib.sha256(script.encode()).digest()
    return "'sha256-" + base64.b64encode(digest).decode() + "'"


def test_collects_unique_executable_inline_script_hashes(tmp_path: Path) -> None:
    script = "window.test = true"
    (tmp_path / "index.html").write_text(
        f"""
        <script>{script}</script>
        <script>{script}</script>
        <script src="/bundle.js"></script>
        <script type="application/json">{{"ignored": true}}</script>
        """,
        encoding="utf-8",
    )

    assert script_hashes(tmp_path) == [expected_hash(script)]


def test_writes_cloudflare_headers_with_strict_script_policy(tmp_path: Path) -> None:
    script = "window.test = true"
    (tmp_path / "index.html").write_text(f"<script>{script}</script>", encoding="utf-8")

    output = write_headers(tmp_path)

    headers = output.read_text(encoding="utf-8")
    assert expected_hash(script) in headers
    assert "script-src 'self'" in headers
    assert "'unsafe-inline'" not in headers.split("script-src", 1)[1].split(";", 1)[0]
    assert "Strict-Transport-Security: max-age=31536000; includeSubDomains" in headers
    assert "X-Content-Type-Options: nosniff" in headers
    assert "Cache-Control:" not in headers
    assert (tmp_path / ".assetsignore").read_text(encoding="utf-8") == ".DS_Store\n"


def test_rejects_site_without_inline_scripts(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text("<script src='/bundle.js'></script>", encoding="utf-8")

    with pytest.raises(ValueError, match="no executable inline scripts"):
        render_headers(tmp_path)
