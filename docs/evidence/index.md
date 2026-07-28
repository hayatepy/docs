# How to read the evidence

Hayate separates three questions that are often collapsed into one claim.

## 1. Does the same application contract work?

The competitive HTTP workload executes routing, parameters, query strings,
JSON, headers, cookies, errors, middleware, body limits, and streaming. It is
a shared-workload contract, not a universal standards score.

## 2. What does the boundary cost?

Startup, production dependency count, compressed deployment payload,
throughput, CPU, and memory are recorded separately. No weighted score hides
the trade-offs.

## 3. Does the ecosystem work together?

Compatibility evidence installs candidate or released packages into
downstream repositories and executes direct, ASGI, and native Workerd paths.
An import check is not treated as deployment evidence.

Continue with [compatibility](compatibility.md) or [benchmarks](benchmarks.md).
