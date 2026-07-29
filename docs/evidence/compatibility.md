# Tested compatibility

The current public snapshot is dated **2026-07-30**. All packages remain
pre-1.0, so compatible versions must be selected from evidence rather than
assumed from package names.

[Open the immutable compatibility snapshot](https://github.com/hayatepy/.github/blob/975173da2c1be720a4f902cde36ba3822b9b6e56/docs/COMPATIBILITY.md){ .md-button .md-button--primary }

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
- `create-hayate 0.13.0` propagates the client, its types, and drift checks
  into generated projects.
- The released generator passed all
  [112 frontend compositions](https://github.com/hayatepy/create-hayate/actions/runs/30488857568).
  The aggregate evidence JSON SHA-256 is
  `fb3f4dc15e8d49bd1fdb6a658df70cc33e174a0f9342895f732dca8aa57a8bb9`.
- The [golden application main
  run](https://github.com/hayatepy/golden-app/actions/runs/30488723553)
  executes authenticated path, query, JSON, multipart, delete, and error
  flows through the compiled client.

The generated [family map](../ecosystem/index.md) pins each listed project to
the source commit used for this site snapshot.
