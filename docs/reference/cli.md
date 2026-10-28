<!--
SPDX-FileCopyrightText: 2026 The predictygraph Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Command line

`pdg` and `predictygraph` are the same command.

```sh
pdg FILE.pdg [options]
```

## Output

- `pdg x.pdg`: writes `x.svg`. If the diagram uses animation, the SVG is animated.
- `pdg x.pdg -o out.svg`: choose the output file.
- `pdg x.pdg --static`: SVG without animation (the first frame).
- `pdg x.pdg --at 0.4`: SVG frozen 0.4 seconds into the animation.
- `pdg x.pdg -o x.png`: animated PNG. Needs `predictygraph[apng]`.

!!! tip "Prefer SVG"
    An animated SVG is usually a few kilobytes; the same animation as PNG can be several megabytes.
    Use PNG only where SVG isn't supported.

## Options

- `--css FILE`: extra stylesheet, applied after the file's own. Repeatable.
- `--theme NAME`: use a built-in theme (or a `.toml` path), overriding `graph theme=`.
- `--list-themes`: print the built-in theme names.
- `--check`: parse, lay out and route only, then report errors. Good for CI.
- `--allow-outside`: let `image=` and `css "…"` read files outside the diagram's folder.
- `--fps 20`, `--scale 2`, `--seconds N`: animated PNG settings.

## Safety

Diagrams are often shared, so by default `image=` and `css "…"` can only read files inside
the folder of the `.pdg` file. Use `--allow-outside` only for files you trust.

## Environment

- `PDG_THEME_PATH`: extra folders to search for theme `.toml` files, separated by `:`.
