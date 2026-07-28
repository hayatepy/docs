# Hayate documentation

Unified documentation and the public home for the
[Hayate Python ecosystem](https://github.com/hayatepy), built with
[Zensical](https://zensical.org/) and deployed as
[Cloudflare Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/).

Production: <https://hayatepy.dev/>

## Work locally

```sh
uv sync --locked
npm ci
uv run python scripts/export_ecosystem.py --check
uv run zensical serve
```

Run the complete local gate before opening a pull request:

```sh
uv run ruff check scripts tests
uv run ruff format --check scripts tests
uv run pytest -q
uv run zensical build --clean --strict
uv run python scripts/write_headers.py site
uv run python scripts/check_site.py site
```

Preview the exact Cloudflare runtime locally:

```sh
npm run preview
```

Deploy with the account authenticated by Wrangler:

```sh
npm run deploy
```

The central site owns cross-package onboarding, runtime selection, ecosystem
navigation, and evidence interpretation. Package-specific API details remain
next to their implementation repositories.
