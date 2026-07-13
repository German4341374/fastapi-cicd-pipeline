# Pipeline reference

The README table is the authoritative job inventory. PR runs use cancellation because superseded
commits have no deployment value. Releases and deployment simulations use non-cancelling
concurrency because partially completed publication or rollback evidence is operationally confusing.

Coverage and JUnit XML support review and diagnostics. The image archive demonstrates artifact
handling, while the CycloneDX SBOM describes components. Trivy identifies known vulnerabilities;
Hadolint evaluates Dockerfile practices; pip-audit evaluates Python dependencies; Gitleaks searches
history for credential patterns. None alone is a security guarantee.
