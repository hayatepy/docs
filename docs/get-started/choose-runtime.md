# Choose a runtime

Start with the operational boundary you actually need. Hayate does not require
ASGI when the target is Cloudflare Workers.

| If you need… | Choose | Important constraint |
|---|---|---|
| Conventional Python hosting and its server ecosystem | [ASGI](../deploy/asgi.md) | Adapter and server are separate dependencies |
| D1, Workers bindings, and class handlers at the edge | [Cloudflare Workers](../deploy/workers.md) | Python/Wasm costs more CPU and memory than Hono's JavaScript path |
| API Gateway v2 or Function URLs | [AWS Lambda](../deploy/lambda.md) | Streaming uses the custom native runtime path |
| Pure contract tests | `app.request(...)` | No network server is started |

## A practical default

- Use ASGI for established Python infrastructure and ordinary server
  deployments.
- Use the Workers class entrypoint when D1, Workers bindings, named RPC,
  scheduled work, or a Python edge deployment is the reason for choosing
  Cloudflare.
- Use Lambda when AWS event integration and Function URLs are the deployment
  boundary.

The optional Workers global handler is an HTTP-only compatibility mode. It is
not the feature-complete default and cannot represent named RPC or scheduled
class handlers.
