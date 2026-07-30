# Tested compatibility

The current public snapshot is dated **2026-07-30**. All packages remain
pre-1.0, so compatible versions must be selected from evidence rather than
assumed from package names.

[Open the immutable compatibility snapshot](https://github.com/hayatepy/.github/blob/1496dc87b780ff81470518df468a18bd6783ebce/docs/COMPATIBILITY.md){ .md-button .md-button--primary }

## Golden runtime lock

| Boundary | Tested value |
|---|---|
| Minimum package Python | 3.12+ |
| Golden application Python | 3.13 |
| Golden application Node.js | 24 |
| MCP revision | 2026-07-28 |
| OpenAPI revision | 3.1.1 |
| Workers compatibility date | 2026-07-01 |
| Workers flags | `python_workers` |
| Default Workers entrypoint | `WorkerEntrypoint` class |

## Released client evidence

- `hayate-openapi 0.8.1` generates the dependency-free callable TypeScript
  client and validates it against a real Hayate ASGI process.
- `create-hayate 0.13.2` propagates the client, its types, and drift checks
  into generated projects.
- Its [release workflow](https://github.com/hayatepy/create-hayate/actions/runs/30502570222)
  resolved and imported all 52 supported backend compositions before publishing
  the signed, attested wheel.
- The `0.13.2` wheel also passed the current
  [10-case frontend smoke](https://github.com/hayatepy/create-hayate/actions/runs/30502309672)
  across htmx renderers, React, Astro, ASGI, and real Workerd. The aggregate
  evidence JSON SHA-256 is
  `f207dcd979c695508c4bf672432848e5469ebf4ab1b58b0f2c4fecb8e004af05`.
- The [golden application main
  run](https://github.com/hayatepy/golden-app/actions/runs/30494459938)
  executes authenticated path, query, JSON, multipart, delete, and error
  flows through the compiled client.

The generated [family map](../ecosystem/index.md) pins each listed project to
the source commit used for this site snapshot.
