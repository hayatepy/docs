# Get started

Hayate is a family of focused packages around one portable HTTP core. The
fastest supported start is the generated production composition because it
exercises the same package versions and runtime boundaries as the public
golden application.

## Pick the shortest path

| Goal | Continue with |
|---|---|
| Generate a complete Workers/D1 application | [First application](first-app.md) |
| Add Hayate to an existing service | [`hayate` core guide](https://github.com/hayatepy/hayate/blob/main/docs/guide/getting-started.md) |
| Decide between ASGI, Workers, and Lambda | [Choose a runtime](choose-runtime.md) |
| Select auth, MCP, OpenAPI, SQL, admin, or HTML | [Compose a stack](../ecosystem/compose.md) |

!!! note "Python support"

    Published Hayate packages require Python 3.12 or newer. The production
    golden application currently locks Python 3.13 and Node.js 24 for its
    real Workerd path.

## What stays stable across runtimes

- application routes and middleware;
- Fetch-style request and response objects;
- direct `app.request(...)` tests;
- validation and Problem Details responses;
- optional OpenAPI, MCP, auth, SQL, and request-correlation contracts.

Runtime bindings, lifecycle details, and streaming capabilities remain
explicit. Portability does not mean pretending every platform is identical.
