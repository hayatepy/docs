# Tested compatibility

The current public snapshot is dated **2026-07-30**. All packages remain
pre-1.0, so compatible versions must be selected from evidence rather than
assumed from package names.

[Open the immutable compatibility snapshot](https://github.com/hayatepy/.github/blob/74327adddc10cad0f3f802a4bfd29ef484572907/docs/COMPATIBILITY.md){ .md-button .md-button--primary }

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
- `create-hayate 0.14.0` propagates the client, its types, and drift checks
  into generated projects. Its production Workers template also propagates
  application and Cloudflare deployment identity to every response.
- `hayate-mcp 0.12.1` passes the official 70-case MCP 2026-07-28
  conformance suite, real Workerd execution, and release provenance checks.
- `hayate 0.15.3`, `hayate-sql 0.1.2`, `hayate-fetch 0.1.4`, and
  `hayate-auth 0.10.5` publish immutable wheels with SLSA provenance and SPDX
  SBOMs.
- Its [release workflow](https://github.com/hayatepy/create-hayate/actions/runs/30510444651)
  resolved and imported all 52 supported backend compositions before publishing
  the signed, attested wheel.
- The `0.14.0` public wheel also passed the full
  [112-case composition matrix](https://github.com/hayatepy/create-hayate/actions/runs/30511183502)
  across backend and frontend combinations, ASGI, and real Workerd. No expected
  case was missing or failed. The aggregate
  evidence JSON SHA-256 is
  `d980477da29e494182080adcd79b864ab533a1dcfbc8035b401f75f7dfa97e43`.
- The [golden application main
  run](https://github.com/hayatepy/golden-app/actions/runs/30511141307)
  executes authenticated path, query, JSON, multipart, delete, and error
  flows through the compiled client and locks `hayate 0.15.3`,
  `hayate-mcp 0.12.1`, `hayate-openapi 0.8.2`, and `hayate-sql 0.1.2`.
- The same run proves both class and global Workers entrypoints under real
  Workerd. Each returns `X-Hayate-App-Version: 0.1.0` and a platform-issued
  `X-Hayate-Worker-Version` UUID. The ASGI smoke returns the app version and
  deliberately omits the Worker-only identifier.

The generated [family map](../ecosystem/index.md) pins each listed project to
the source commit used for this site snapshot.
