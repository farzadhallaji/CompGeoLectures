# CompGeo lectures (MkDocs)

Static lecture notes built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

- **Published site:** [https://farzadhallaji.github.io/CompGeoLectures/](https://farzadhallaji.github.io/CompGeoLectures/) (after you enable GitHub Pages → **GitHub Actions** and push `main`)
- **Sources:** `Lectures/docs/`
- **Config:** `mkdocs.yml` (repository root)

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

## Publish to GitHub (first time)

1. **Revoke** any leaked personal access token (see [SECURITY.md](SECURITY.md)).
2. Create an empty repo `farzadhallaji/CompGeoLectures` on GitHub (no README/license if you want a clean history), or pull/merge if it already exists.
3. Authenticate and push (pick one):
   - **Token (script):** create a fine-grained PAT with **Contents: Read and write** on this repo, then:
     - `export GITHUB_TOKEN='your_token_here'`
     - `./scripts/push-to-github.sh`
   - **GitHub CLI:** `gh auth login`, then `git push -u origin main`
   - **SSH:** `git remote set-url origin git@github.com:farzadhallaji/CompGeoLectures.git` and `git push -u origin main`
4. **Before the first deploy succeeds**, open the repo on GitHub → **Settings → Pages** → under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from a branch”) and save. If you skip this, workflows that call the Pages API can fail with “Get Pages site failed / Not Found”.
5. After the workflow runs, open **https://farzadhallaji.github.io/CompGeoLectures/** (include the trailing slash; the repo name is case-sensitive in the path).

### If you see 404

- **`deploy-pages` fails with “Creating Pages deployment failed” / Not Found:** Pages is not enabled for the repo. Follow **[PAGES_SETUP.md](PAGES_SETUP.md)** (one-time **Settings → Pages → Source: GitHub Actions**).
- **Settings → Pages → Source** must be **GitHub Actions**, not “Deploy from a branch”.
- Open **Actions** and confirm the latest **Deploy MkDocs to GitHub Pages** run finished green for both **build** and **deploy**.
- The first run may ask you to **approve** the `github-pages` environment (repo **Settings → Environments**).
- Push to `main` after fixing the workflow: `git push origin main`.

## Security

If a GitHub personal access token was ever pasted into a clone URL or chat, revoke it and use SSH or `gh auth login`. See [SECURITY.md](SECURITY.md).
