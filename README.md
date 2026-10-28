# predictygraph.github.io

Source of the [predictygraph documentation site](https://predictygraph.github.io/).

Images are not committed. Every `.pdg` file under `docs/` is rendered to SVG (and animated
PNG) at build time, so the pictures always match the current release.

```sh
uv sync
uv run python scripts/render_examples.py docs --apng
uv run mkdocs serve
```

GitHub Actions builds and deploys `master` to GitHub Pages. A push to the
predictygraph repo can trigger a rebuild with a `predictygraph-updated` repository dispatch.
