#!/usr/bin/env bash
set -Eeuo pipefail

url="${1:-http://127.0.0.1:8000/health}"
for attempt in {1..20}; do
  if curl --fail --silent --show-error "${url}"; then
    echo
    echo "Smoke test passed on attempt ${attempt}."
    exit 0
  fi
  sleep 1
done
echo "Smoke test failed: ${url} did not become healthy." >&2
exit 1
