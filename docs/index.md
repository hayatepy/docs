---
hide:
  - navigation
  - toc
  - tags
title: Hayate — Web-standards-first Python
description: One Fetch-style Python application across ASGI, Cloudflare Workers, and AWS Lambda.
---

<section class="hayate-hero">
  <div class="hayate-hero__inner">
    <div class="hayate-hero__copy">
      <p class="hayate-kicker">WEB-STANDARDS-FIRST PYTHON</p>
      <h1>One application.<br>Every serious runtime.</h1>
      <p class="hayate-lede">
        Build typed HTTP, MCP, authentication, and checked data access once.
        Run it on ASGI, Cloudflare Workers, or AWS Lambda.
      </p>
      <div class="hayate-actions">
        <a class="md-button md-button--primary" href="get-started/first-app/">Build the first app</a>
        <a class="md-button" href="ecosystem/">Explore the family</a>
      </div>
    </div>
    <img class="hayate-hero__mark" src="assets/images/hayate-mark.png" alt="">
  </div>
</section>

<section class="hayate-section hayate-section--intro">
  <p class="hayate-kicker">THE MODEL</p>
  <h2>Fetch at the center. Adapters at the edge.</h2>
  <p>
    Hayate keeps WHATWG-style <code>Request</code>, <code>Response</code>,
    <code>URL</code>, and <code>URLPattern</code> semantics in the application
    core. Deployment adapters stay explicit, so Cloudflare does not require
    ASGI and conventional Python does not inherit Workers constraints.
  </p>
</section>

<section class="hayate-runs" aria-labelledby="runs-heading">
  <p class="hayate-kicker">THREE RUNTIME CONTRACTS</p>
  <h2 id="runs-heading">Choose the boundary. Keep the application.</h2>
  <div class="hayate-runs__grid">
    <div>
      <h3>ASGI</h3>
      <p>Uvicorn and the existing Python server ecosystem for conventional deployments.</p>
      <a href="deploy/asgi/">Deploy on ASGI →</a>
    </div>
    <div>
      <h3>Workers</h3>
      <p>Native Python Workers, D1 bindings, RPC-capable class entrypoints, and no ASGI layer.</p>
      <a href="deploy/workers/">Deploy on Workers →</a>
    </div>
    <div>
      <h3>Lambda</h3>
      <p>API Gateway v2 and Function URLs, including a native response-streaming runtime.</p>
      <a href="deploy/lambda/">Deploy on Lambda →</a>
    </div>
  </div>
</section>

<section class="hayate-section hayate-section--family">
  <p class="hayate-kicker">COMPOSE ONLY WHAT YOU NEED</p>
  <h2>A small core. A deliberate family.</h2>
  <p>
    Auth, MCP, OpenAPI, checked SQL, outbound fetch, admin, and hypermedia are
    maintained as explicit packages—not hidden framework weight.
  </p>
  <div class="hayate-family-links">
    <a href="ecosystem/#hayate-auth"><span>Identity</span><strong>hayate-auth</strong></a>
    <a href="ecosystem/#hayate-mcp"><span>Agents</span><strong>hayate-mcp</strong></a>
    <a href="ecosystem/#hayate-openapi"><span>Contracts</span><strong>hayate-openapi</strong></a>
    <a href="ecosystem/#hayate-sql"><span>Data</span><strong>hayate-sql</strong></a>
    <a href="ecosystem/#hayate-admin"><span>Operations</span><strong>hayate-admin</strong></a>
    <a href="ecosystem/#hayate-htmx"><span>Hypermedia</span><strong>hayate-htmx</strong></a>
  </div>
</section>

<section class="hayate-proof">
  <div>
    <p class="hayate-kicker">EVIDENCE, NOT A UNIVERSAL WINNER</p>
    <h2>Current claims are dated, reproducible, and bounded.</h2>
  </div>
  <p>
    The published baseline records startup, dependencies, payload, throughput,
    and a shared HTTP contract. Compatibility is backed by real ASGI,
    Workerd/D1, downstream package runs, and a generated zero-runtime
    TypeScript client executed against real ASGI.
  </p>
  <a class="md-button" href="evidence/">Read the evidence</a>
</section>

<section class="hayate-partners" aria-labelledby="partners-heading">
  <div class="hayate-partners__inner">
    <div class="hayate-partners__copy">
      <p class="hayate-kicker">SHAPE THE V1 CONTRACT</p>
      <h2 id="partners-heading">Bring a real workload.</h2>
      <p>
        Owner-external teams receive bounded onboarding help while Hayate
        records the friction, fixes reproducible blockers, and bases v1
        decisions on measured use.
      </p>
    </div>
    <ol class="hayate-partners__tracks" aria-label="Design-partner tracks">
      <li><span>01</span><strong>CPython / ASGI API</strong></li>
      <li><span>02</span><strong>MCP or agent backend</strong></li>
      <li><span>03</span><strong>Cloudflare Workers</strong></li>
    </ol>
    <div class="hayate-partners__actions">
      <a
        class="hayate-partners__apply"
        href="https://github.com/hayatepy/.github/issues/new?template=design_partner.yml"
      >Apply as a design partner <span aria-hidden="true">→</span></a>
      <a href="contribute/#design-partners">Read the program details</a>
    </div>
  </div>
</section>

<section class="hayate-final">
  <p class="hayate-kicker">START FROM A TESTED COMPOSITION</p>
  <h2>From empty directory to passing production checks.</h2>
  <p><code>uvx --from create-hayate==0.13.1 create-hayate my-app --template workers --preset production</code></p>
  <a class="md-button md-button--primary" href="get-started/first-app/">Follow the verified path</a>
</section>
