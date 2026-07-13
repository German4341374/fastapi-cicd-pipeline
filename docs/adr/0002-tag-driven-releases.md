# ADR 0002: Publish only semantic tags

- Status: Accepted
- Date: 2026-07-13

Main-branch pushes validate but do not publish. Tags matching and validating as `vMAJOR.MINOR.PATCH`
produce immutable version labels and `latest`. Rollback selects an earlier version instead of
rebuilding old source.
