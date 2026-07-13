# ADR 0001: Centralize read-only CI

- Status: Accepted
- Date: 2026-07-13

Pull request and release workflows call one reusable workflow. This prevents quality and security
policy drift. It receives only `contents: read`; package publication stays in a separate tag-gated
job with `packages: write`.
