# Five-minute employer demonstration

## Preparation

Run local checks and keep a successful GitHub Actions run open. Never claim a command passed unless
you ran it. Open the workflow graph, reusable workflow, release workflow, and rollback runbook.

## 0:00–1:00 — purpose and architecture

Show the README diagram. Explain that the workload is intentionally small and PR/release callers
share one read-only workflow, preventing policy drift.

## 1:00–2:00 — pipeline evidence

Open a successful run. Show formatting, tests, 90% coverage, dependency audit, Gitleaks, Hadolint,
image smoke test, Trivy, SBOM, image archive, and uniquely named artifacts.

## 2:00–3:00 — permission and release policy

Compare workflow permission blocks. Point out that only the semantic-tag publish job has
`packages: write`; PRs cannot publish. Show caching and concurrency differences.

## 3:00–4:00 — local workload

Run `make up`, `curl http://localhost:8000/health`, and `docker compose ps`. Show the non-root user,
health check, read-only filesystem, and capability dropping.

## 4:00–5:00 — deployment and rollback

Open the manual simulation workflow and rollback runbook. Explain immutable semantic versions,
health verification, deployment record artifacts, and why no cloud credentials are required.
