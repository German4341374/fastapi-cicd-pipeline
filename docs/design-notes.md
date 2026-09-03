# Design notes

## 1. Why is the application small?

Minimal business logic keeps attention on the pipeline evidence and policy.

## 2. Why use a reusable workflow?

PR and release pipelines execute identical checks without copying YAML that can drift.

## 3. Why is reusable CI read-only?

Untrusted or ordinary validation should not mutate repository, package, or deployment state.

## 4. Why can only tags publish?

Semantic tags represent an explicit release decision and provide an immutable rollback identifier.

## 5. How is semantic versioning enforced?

A script validates `vMAJOR.MINOR.PATCH` with optional prerelease text and emits the stripped version.

## 6. Why separate PR and release workflows?

They have different trust, concurrency, mutation, and evidence requirements.

## 7. What does concurrency control solve?

It cancels stale PR work while preventing overlapping or cancelled release/deployment operations.

## 8. What is cached?

Python packages use setup-python caching, while GHCR builds use GitHub Actions BuildKit cache.

## 9. Why upload coverage and JUnit XML?

They provide inspectable evidence and help diagnose failures after runner logs expire.

## 10. Why generate an SBOM?

It records image components for incident response, policy review, and vulnerability correlation.

## 11. How does pip-audit differ from Trivy?

pip-audit focuses on Python dependencies; Trivy scans OS and application packages in the final image.

## 12. Why use Gitleaks with full history?

Deleting a secret from the current tree does not remove it from earlier commits.

## 13. What does Hadolint add?

It detects Dockerfile reliability and security anti-patterns before runtime scanning.

## 14. Why smoke-test the built image?

A successful build does not prove the process starts or its health endpoint responds.

## 15. What is least privilege here?

Read-only defaults, job-scoped package write, no cloud credentials, and a non-root runtime container.

## 16. Why retain image archives only seven days?

They are large demonstration artifacts; semantic registry images are the long-term release unit.

## 17. How is rollback performed?

Select a previously verified immutable version, simulate its health, then update the real platform reference.

## 18. Why not publish on every main push?

It would turn ordinary integration into a release and increase registry noise and mutation risk.

## 19. What does Dependabot cover?

Python packages, Docker base images, and GitHub Actions receive weekly reviewable update PRs.

## 20. Why no real deployment?

The design demonstrates gates, evidence, health checks, concurrency, and rollback without paid resources.

## 21. How would you harden releases further?

Signed protected tags, required reviewers, digest-pinned Actions, provenance, and keyless image signing.

## 22. Why use a coverage threshold?

It makes test erosion visible, while review still determines whether tests are meaningful.

## 23. What happens for a fork PR?

Read-only validation works, while package publishing remains unreachable and receives no write token.

## 24. What is an artifact collision?

Parallel jobs uploading the same artifact name can conflict; run IDs make names unique.

## 25. What would you add next?

Multi-architecture builds, signing, provenance verification, protected environments, and policy-as-code.
