# Security

## If a GitHub token was ever shared

Personal access tokens (`ghp_...`) must never appear in chat, clone URLs, or committed files.

If a token was exposed:

1. Revoke it immediately: GitHub **Settings → Developer settings → Personal access tokens**.
2. Generate a new token only if needed, and store it in a password manager or use **SSH keys** / **`gh auth login`** instead.
3. Use remotes without embedded credentials, for example: `git@github.com:farzadhallaji/CompGeoLectures.git`.

This repository’s CI uses the default `GITHUB_TOKEN` for Pages deployment; you do not need a PAT in the repo for that.
