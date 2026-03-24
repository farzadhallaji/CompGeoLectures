#!/usr/bin/env bash
# Push local main to GitHub using a token (not stored in git config).
# Create a fine-grained PAT with Contents: Read and write on CompGeoLectures.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
REPO="farzadhallaji/CompGeoLectures"

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "Set GITHUB_TOKEN, then run again, e.g.:"
  echo "  export GITHUB_TOKEN=ghp_...   # or fine-grained token"
  echo "  ./scripts/push-to-github.sh"
  exit 1
fi

exec git push "https://x-access-token:${GITHUB_TOKEN}@github.com/${REPO}.git" HEAD:main
