# AWS Lambda

Hayate supports API Gateway HTTP API payload v2 and Lambda Function URLs
through a native event adapter.

## Buffered responses

Use the normal Lambda adapter for JSON, HTML, binary responses, cookies, and
ordinary buffered streaming bodies.

## Native response streaming

When time-to-first-byte matters, Hayate also provides a custom Runtime API
path for Lambda response streaming. It writes the Lambda streaming prelude,
metadata, body chunks, and terminal framing directly instead of claiming that
the ordinary buffered handler streams.

This path has core CI evidence but is not yet part of the production golden
application's deployment flow. Treat that distinction as an adoption input.

See the
[core runtime guide](https://github.com/hayatepy/hayate/blob/main/docs/guide/runtimes.md#aws-lambda)
for adapter APIs and limits.
