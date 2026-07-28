# Cloudflare Workers

Hayate runs as native Python inside Workerd. The normal entrypoint is a
`WorkerEntrypoint` class, not an ASGI server embedded at the edge.

## Choose the class entrypoint by default

The class path preserves:

- HTTP `fetch`;
- environment and D1 bindings;
- `ctx.waitUntil`;
- named RPC methods;
- class handlers such as `scheduled`.

The optional global handler is deliberately HTTP-only. It can reduce a small
amount of dispatch overhead, but it cannot express the complete class
contract.

## Be honest about the runtime trade

The native Workerd benchmark records two different conclusions:

- Hayate's class adapter is close to its raw Python class ceiling.
- Hono's JavaScript Workers path remains materially better for startup,
  memory, CPU, and upload size.

Choose Python Workers when Python package reuse, one application contract, D1,
MCP, or the Hayate ecosystem creates more value than JavaScript's runtime
efficiency. Read the [benchmark interpretation](../evidence/benchmarks.md)
before presenting the result.

The executable reference is
[`golden-app`](https://github.com/hayatepy/golden-app).
