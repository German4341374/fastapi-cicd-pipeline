# Security Policy

Report vulnerabilities using GitHub private security advisories. Do not open public issues with
exploit details or secrets. The pull request workflow is read-only; GHCR write permission exists
only in the tag-gated publish job. Gitleaks, pip-audit, Hadolint, Trivy, and SBOM generation provide
defense in depth but do not prove the absence of vulnerabilities. Rotate any exposed secret even
if it is later removed from Git history.
