#!/usr/bin/env bash
set -Eeuo pipefail

tag="${1:-${GITHUB_REF_NAME:-}}"
if [[ ! "${tag}" =~ ^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?$ ]]; then
  echo "Expected a semantic version tag such as v1.2.3; received: ${tag:-<empty>}" >&2
  exit 1
fi

version="${tag#v}"
echo "version=${version}"
if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
  echo "version=${version}" >> "${GITHUB_OUTPUT}"
fi
