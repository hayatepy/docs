from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[1]


def load_config(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_site_uses_canonical_custom_domain() -> None:
    config = load_config("wrangler.jsonc")

    assert config["name"] == "hayate-docs"
    assert config["routes"] == [
        {"pattern": "hayatepy.dev", "custom_domain": True},
    ]
    assert config["assets"]["directory"] == "./site"


def test_http_redirect_only_intercepts_plaintext_requests() -> None:
    config = load_config("wrangler.redirect.jsonc")

    assert config["name"] != "hayate-docs"
    assert config["workers_dev"] is False
    assert config["routes"] == [
        {"pattern": "http://hayatepy.dev/*", "zone_name": "hayatepy.dev"},
    ]
    assert (ROOT / config["main"]).is_file()
