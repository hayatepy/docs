# ASGI

ASGI is Hayate's conventional Python server adapter. It is useful when your
deployment already uses Uvicorn, Hypercorn, process managers, or ASGI
middleware.

```sh
uv add hayate uvicorn
uv run uvicorn app:app
```

Hayate's ASGI boundary covers HTTP, streaming responses, WebSockets, lifespan
hooks, disconnect signals, and incremental migration through mounted ASGI
applications.

## What ASGI is not

ASGI is not the core application model and is not required on Cloudflare.
Native Workers call the Fetch-style application through the Workers adapter.

For a generated local ASGI plus production Workers composition, follow the
[first application](../get-started/first-app.md).
