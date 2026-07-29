# Compose a stack

Begin with `hayate`, then add packages only for contracts your application
owns.

## Agent backend

```sh
uv add hayate hayate-mcp hayate-auth hayate-openapi hayate-sql
```

- `hayate-mcp` exposes MCP Streamable HTTP.
- `hayate-auth` can issue or verify OAuth tokens and DPoP proofs.
- `hayate-openapi` describes adjacent HTTP APIs and typed clients.
- `hayate-sql` keeps application data contracts explicit.

The public [compatibility snapshot](../evidence/compatibility.md) records the
downstream FolioMCP production gate alongside public Workerd tests. Runtime
compatibility is based on execution, not import success.

## Conventional typed API

```sh
uv add hayate hayate-openapi
```

Use explicit `Annotated` request sources and return types to drive runtime
binding, validation, JSON serialization, OpenAPI 3.1, and TypeScript types.

## Server-rendered application

```sh
uv add hayate hayate-auth hayate-htmx hayate-sql
```

`hayate-htmx` supplies Jinja, typed `HX-*` metadata, page/fragment selection,
SSE, and CSRF guidance while the core remains renderer-independent.

## Operational control plane

Add `hayate-admin` when trusted operators need explicit resources, bounded
list/search/export behavior, per-object authorization, and redacted audit
history. It is not a model-driven ORM admin and is not intended for public
customer workflows.

## Generate instead of assembling by hand

`create-hayate` validates backend and frontend combinations before publishing
them:

```sh
uvx --from create-hayate==0.12.0 create-hayate --help
```

Use the [family map](index.md) for current release state and package links.
