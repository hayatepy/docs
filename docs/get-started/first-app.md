# Build the first application

This path creates one tested application for local ASGI/SQLite and native
Cloudflare Workers/D1, with OpenAPI 3.1.1, MCP 2026-07-28 discovery and tools,
Cloudflare Access, checked SQL, request correlation, and production middleware.

## 1. Generate

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
uvx --refresh --from create-hayate==0.12.0 \
  create-hayate my-app --template workers --preset production
cd my-app
```

The version is intentional. Check the [compatibility snapshot](../evidence/compatibility.md)
before changing individual pre-1.0 package pins.

## 2. Lock and verify

```sh
uv sync
test -f uv.lock
uv sync --locked
uv run pytest
uv run ruff check .
uv run python scripts/check_sql_contracts.py
```

Commit `uv.lock` and use `uv sync --locked` in CI. The generated `.dev.vars`
contains ignored local development identity values; never commit production
credentials.

## 3. Read the shape

- `src/app.py` is the portable application core.
- Uvicorn supplies local ASGI; SQLite supplies local data.
- Workerd supplies the native Workers adapter; D1 is a runtime binding.
- HTTP and MCP share request identity and checked storage.
- The default Workers export is a `WorkerEntrypoint` class, preserving named
  RPC and class handlers such as `scheduled`.

ASGI is not involved in the native Workers path.

## 4. Prepare production

Compare the result with the
[golden application](https://github.com/hayatepy/golden-app), then complete
its [production checklist](https://github.com/hayatepy/golden-app/blob/main/PRODUCTION.md)
and read its [trust boundaries](https://github.com/hayatepy/golden-app/blob/main/ARCHITECTURE.md).

Do not deploy placeholder Access audiences, D1 identifiers, CORS origins,
rate-limit namespaces, or observability policy.
