# Agent Guidelines

- Use English and never add credentials, tokens, personal data, or cloud resources.
- Preserve read-only permissions in reusable and pull request workflows.
- Grant `packages: write` only to the approved tag publication job.
- Pin tools and images, and update documentation when pipeline behavior changes.
- Do not weaken scanners to obtain a green build; update or document the dependency.
- Test semantic version parsing, rollback instructions, artifacts, and concurrency changes.
- Run `make lint`, `make test`, and `make audit`; run container checks when Docker is available.
