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
- `create-hayate 0.13.1` propagates the client, its types, and drift checks
  into generated projects.
- The released generator passed all
  [112 frontend compositions](https://github.com/hayatepy/create-hayate/actions/runs/30493092512).
  The aggregate evidence JSON SHA-256 is
  `f7be85bf13c135c9c112c3cb504c337f3e0fbad501fe575425ad69be898a84df`.
- The [golden application main
  run](https://github.com/hayatepy/golden-app/actions/runs/30494459938)
  executes authenticated path, query, JSON, multipart, delete, and error
  flows through the compiled client.

The generated [family map](../ecosystem/index.md) pins each listed project to
the source commit used for this site snapshot.
