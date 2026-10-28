# predictygraph.github.io

Source of the [predictygraph documentation site](https://predictygraph.github.io/).

Images (`*.png`, `*.svg`) are stored with [Git LFS](https://git-lfs.com/), so the main
predictygraph repo stays free of binaries. Install git-lfs before cloning.

## Update the images

Every `.pdg` under `docs/` has its rendered SVG (and animated PNG) committed next to it.
After changing a diagram or releasing a new predictygraph, re-render and commit:

```sh
uv sync
uv run python scripts/render_examples.py docs --apng
git add docs && git commit -m "docs: re-render examples"
```

## Preview

```sh
uv run mkdocs serve
```

GitHub Actions builds `master` from the committed images and deploys it to GitHub Pages.
