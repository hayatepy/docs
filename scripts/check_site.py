"""Validate generated site structure and internal links without browser dependencies."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

SITE_ORIGIN = "https://hayatepy.dev"
DESIGN_PARTNER_APPLICATION = (
    "https://github.com/hayatepy/.github/issues/new?template=design_partner.yml"
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonicals: list[str] = []
        self.description = False
        self.h1_count = 0
        self.hrefs: list[str] = []
        self.html_lang: str | None = None
        self.images_without_alt: list[str] = []
        self.main_count = 0
        self.title_depth = 0
        self.title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang")
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        elif tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src") or "<unknown>")
        elif tag == "meta" and values.get("name") == "description":
            self.description = bool(values.get("content"))
        elif tag == "link" and values.get("rel") == "canonical" and values.get("href"):
            self.canonicals.append(values["href"] or "")
        elif tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def page_url(path: Path, root: Path) -> str:
    relative = path.relative_to(root)
    if relative == Path("index.html"):
        return "/"
    if relative.name == "index.html":
        return "/" + relative.parent.as_posix().strip("/") + "/"
    return "/" + relative.as_posix()


def target_file(url_path: str, root: Path) -> Path:
    path = unquote(url_path).lstrip("/")
    candidate = root / path
    if not path or url_path.endswith("/"):
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    return candidate / "index.html"


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    html_files = sorted(root.rglob("*.html"))
    if not html_files:
        return ["site contains no HTML pages"]

    for path in html_files:
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        relative = path.relative_to(root)
        if parser.html_lang != "en":
            failures.append(f"{relative}: html lang must be en")
        if parser.main_count != 1:
            failures.append(f"{relative}: expected one main landmark, got {parser.main_count}")
        if parser.h1_count != 1:
            failures.append(f"{relative}: expected one h1, got {parser.h1_count}")
        if not "".join(parser.title_text).strip():
            failures.append(f"{relative}: missing document title")
        if not parser.description:
            failures.append(f"{relative}: missing meta description")
        if relative != Path("404.html") and len(parser.canonicals) != 1:
            failures.append(f"{relative}: expected one canonical URL")
        if parser.images_without_alt:
            failures.append(
                f"{relative}: images missing alt: {', '.join(parser.images_without_alt)}"
            )
        if relative == Path("index.html") and DESIGN_PARTNER_APPLICATION not in parser.hrefs:
            failures.append("index.html: missing direct design-partner application link")

        base = SITE_ORIGIN + page_url(path, root)
        for href in parser.hrefs:
            parsed = urlparse(urljoin(base, href))
            if (
                parsed.scheme not in {"http", "https"}
                or parsed.netloc != urlparse(SITE_ORIGIN).netloc
            ):
                continue
            target = target_file(parsed.path, root)
            if not target.exists():
                failures.append(f"{relative}: broken internal link {href!r}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    args = parser.parse_args()
    failures = validate(args.site)
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Validated generated HTML and internal links in {args.site}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
