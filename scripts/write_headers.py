"""Generate Cloudflare Static Assets headers from the built documentation."""

from __future__ import annotations

import argparse
import base64
import hashlib
import re
from pathlib import Path

SCRIPT_PATTERN = re.compile(
    r"<script\b(?P<attributes>[^>]*)>(?P<body>.*?)</script\s*>",
    flags=re.IGNORECASE | re.DOTALL,
)
SOURCE_ATTRIBUTE = re.compile(r"\bsrc\s*=", flags=re.IGNORECASE)
JSON_TYPE = re.compile(
    r"\btype\s*=\s*[\"']application/(?:ld\+)?json[\"']",
    flags=re.IGNORECASE,
)


def script_hashes(root: Path) -> list[str]:
    """Return sorted CSP hashes for every executable inline script in the site."""
    hashes: set[str] = set()
    for path in root.rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        for match in SCRIPT_PATTERN.finditer(html):
            attributes = match.group("attributes")
            body = match.group("body")
            if SOURCE_ATTRIBUTE.search(attributes) or JSON_TYPE.search(attributes) or not body:
                continue
            digest = hashlib.sha256(body.encode()).digest()
            hashes.add("'sha256-" + base64.b64encode(digest).decode() + "'")
    return sorted(hashes)


def render_headers(root: Path) -> str:
    hashes = script_hashes(root)
    if not hashes:
        raise ValueError("site contains no executable inline scripts")

    content_security_policy = " ".join(
        (
            "default-src 'self';",
            "base-uri 'self';",
            "connect-src 'self';",
            "font-src 'self';",
            "form-action 'self';",
            "frame-ancestors 'none';",
            "img-src 'self' data:;",
            "manifest-src 'self';",
            "object-src 'none';",
            f"script-src 'self' {' '.join(hashes)};",
            "style-src 'self' 'unsafe-inline';",
            "worker-src 'self' blob:;",
            "upgrade-insecure-requests",
        )
    )
    return "\n".join(
        (
            "/*",
            f"  Content-Security-Policy: {content_security_policy}",
            "  Cross-Origin-Opener-Policy: same-origin",
            "  Cross-Origin-Resource-Policy: same-origin",
            "  Permissions-Policy: camera=(), geolocation=(), microphone=()",
            "  Referrer-Policy: strict-origin-when-cross-origin",
            "  X-Content-Type-Options: nosniff",
            "  X-Frame-Options: DENY",
            "",
        )
    )


def write_headers(root: Path) -> Path:
    output = root / "_headers"
    output.write_text(render_headers(root), encoding="utf-8")
    (root / ".assetsignore").write_text(".DS_Store\n", encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    args = parser.parse_args()
    output = write_headers(args.site)
    print(f"Generated {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
