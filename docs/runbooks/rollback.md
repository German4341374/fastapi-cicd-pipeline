# Rollback runbook

1. Identify the last healthy semantic image version from release evidence and deployment records.
2. Confirm its CI run, SBOM, and vulnerability scan passed when it was built.
3. Dispatch `Deployment Simulation` with the failing version in `version` and the healthy version
   in `rollback_to`.
4. Review the health check and downloaded deployment record.
5. In a real platform, update the immutable image reference to the healthy version and monitor.
6. Never move or delete the original semantic tag during incident response.
7. Document cause, impact, selected version, operator, timestamps, and follow-up tests.

This repository performs steps 1–4 only and never changes real infrastructure.
