# Tested compatibility

The current public snapshot is dated **2026-07-30**. All packages remain
pre-1.0, so compatible versions must be selected from evidence rather than
assumed from package names.

[Open the immutable compatibility snapshot](https://github.com/hayatepy/.github/blob/c9c19d02e15c3030be2e6eed9d8ab3c8cc6c9226/docs/COMPATIBILITY.md){ .md-button .md-button--primary }

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

- `hayate-openapi 0.8.2` generates the dependency-free callable TypeScript
  client and validates it against a real Hayate ASGI process.
- `create-hayate 0.13.2` propagates the client, its types, and drift checks
  into generated projects.
- `hayate-mcp 0.12.1` passes the official 70-case MCP 2026-07-28
  conformance suite, real Workerd execution, and release provenance checks.
- `hayate 0.15.3`, `hayate-sql 0.1.2`, `hayate-fetch 0.1.4`, and
  `hayate-auth 0.10.5` publish immutable wheels with SLSA provenance and SPDX
  SBOMs.
- Its [release workflow](https://github.com/hayatepy/create-hayate/actions/runs/30502570222)
  resolved and imported all 52 supported backend compositions before publishing
  the signed, attested wheel.
- The `0.13.2` wheel also passed the current
  [10-case frontend smoke](https://github.com/hayatepy/create-hayate/actions/runs/30502309672)
  across htmx renderers, React, Astro, ASGI, and real Workerd. The aggregate
  evidence JSON SHA-256 is
  `f207dcd979c695508c4bf672432848e5469ebf4ab1b58b0f2c4fecb8e004af05`.
- The [golden application main
  run](https://github.com/hayatepy/golden-app/actions/runs/30507749113)
  executes authenticated path, query, JSON, multipart, delete, and error
  flows through the compiled client and locks `hayate 0.15.3`,
  `hayate-mcp 0.12.1`, `hayate-openapi 0.8.2`, and `hayate-sql 0.1.2`.

The generated [family map](../ecosystem/index.md) pins each listed project to
the source commit used for this site snapshot.
