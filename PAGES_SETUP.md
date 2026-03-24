# Fix: “Creating Pages deployment failed” / HttpError 404

The Actions log means GitHub has **no Pages site configured for this repo yet** (or it is not set to **GitHub Actions**). `deploy-pages` cannot create a deployment until you turn that on once.

## Do this (repo admin required)

1. Open: **https://github.com/farzadhallaji/CompGeoLectures/settings/pages**
2. Under **Build and deployment** → **Source**, choose **GitHub Actions** (not “Deploy from a branch”).
3. Save if there is a save control; wait ~1 minute.
4. In **Actions**, open the failed workflow run → **Re-run all jobs**.

Until step 2 is done, **every** `deploy-pages` run can fail with `Not Found` and a link to Settings → Pages.

## If you do not see “GitHub Actions” as a source

- You need **admin** access to the repository.
- For **private** repos on a **free** personal account, GitHub Pages may be restricted; try making the repo **public** or use a plan that includes private Pages (see [GitHub Pages docs](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)).

## After it works

Your site should be available at:

**https://farzadhallaji.github.io/CompGeoLectures/**
