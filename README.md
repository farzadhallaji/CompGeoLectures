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
3. Authenticate (pick one):
   - `gh auth login`, then `git push -u origin main`
   - or SSH: `git remote set-url origin git@github.com:farzadhallaji/CompGeoLectures.git` and `git push -u origin main`
4. In the repo on GitHub: **Settings → Pages → Build and deployment → Source:** choose **GitHub Actions** (required for the included workflow).
5. After the workflow runs, open **https://farzadhallaji.github.io/CompGeoLectures/**

## Security

If a GitHub personal access token was ever pasted into a clone URL or chat, revoke it and use SSH or `gh auth login`. See [SECURITY.md](SECURITY.md).
