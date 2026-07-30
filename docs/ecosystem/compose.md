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
binding, validation, JSON serialization, OpenAPI 3.1, TypeScript types, and a
callable Fetch client.

## Typed client boundary

`hayate-openapi` emits `api-types.ts` and a status-discriminated
`api-client.ts` from the same OpenAPI 3.1.1 document. The generated client
uses the platform `fetch`, `URL`, `Headers`, `FormData`, and `Blob` APIs, so it
has no runtime npm dependency. Path, query, header, cookie, JSON,
URL-encoded, and multipart inputs stay tied to the published schema.

The [golden application executes the compiled client against a real ASGI
process](https://github.com/hayatepy/golden-app/blob/f0e334554f4b98e4be941dcb84feaaf6b47a9c89/client/check-api-client.ts)
instead of treating generation or type-checking alone as interoperability.

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
uvx --from create-hayate==0.14.0 create-hayate --help
```

Use the [family map](index.md) for current release state and package links.
