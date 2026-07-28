# Competitive benchmarks

The reproducible 2026-07-28 same-workload baseline used Hayate 0.15.1,
FastAPI 0.140.0, Django 6.0.7, and Hono 4.12.32.

| Boundary | Hayate | FastAPI | Django | Hono |
|---|---:|---:|---:|---:|
| Cold start | 149.0 ms | 471.4 ms | 392.6 ms | **61.3 ms** |
| Production packages | 5 | 13 | 6 | **2** |
| gzip payload | 298.1 KiB | 2,802.2 KiB | 5,147.2 KiB | **281.5 KiB** |
| Throughput | 14,906 req/s | 10,086 req/s | 2,557 req/s | **59,187 req/s** |
| Shared HTTP contract | **14/14** | 12/14 | 12/14 | 12/14 |

On this workload Hayate delivered 1.48× FastAPI's and 5.83× Django's
throughput. Hono delivered 3.97× Hayate's throughput and retained the best
startup, dependency-count, and deployment-payload results.

## What this does not prove

- It does not rank every endpoint shape or deployment platform.
- The 14 checks are not a universal standards-compliance percentage.
- The local machine result is not a Cloudflare or AWS production benchmark.
- Ecosystem size and production history are adoption factors outside the
  request-per-second measurement.

[Read the immutable publication and raw methodology](https://github.com/hayatepy/hayate/blob/9e27b0191c7fa9f920ad6fe5b126e190268afba2/benchmarks/competitive/results/2026-07-28-hayate-0.15.1-macos-arm64.md){ .md-button .md-button--primary }

The separate
[capability matrix](https://github.com/hayatepy/hayate/blob/9e27b0191c7fa9f920ad6fe5b126e190268afba2/docs/capabilities.md)
records feature evidence without inventing a weighted universal winner.
