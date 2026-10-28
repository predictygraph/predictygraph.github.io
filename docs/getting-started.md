# Getting started

## Install

```sh
pip install "predictygraph[apng]"    # [apng] adds animated PNG output
```

or run it without installing:

```sh
uvx --from predictygraph pdg diagram.pdg
```

Until the first PyPI release, install from GitHub:

```sh
uv tool install "predictygraph[apng] @ git+https://github.com/predictygraph/predictygraph"
```

## Your first diagram

Save this as `hello.pdg`:

```pdg
--8<-- "examples/hello.pdg"
```

Render it:

```sh
pdg hello.pdg                 # -> hello.svg (animated if the diagram uses flows)
pdg hello.pdg --static        # SVG frozen at t=0
pdg hello.pdg -o hello.png    # animated PNG
pdg hello.pdg --check         # validate only
```

![hello.pdg](examples/hello.svg)

## The five things to know

1. **One statement per line.** `;` separates statements on one line. `#` plus a space starts a comment.
2. **Nodes:** `id "Label" .class key=value`. The label is optional.
3. **Edges:** `a -> b "label"`. Chains (`a -> b -> c`) and fan-out (`a -> b, c`) work.
4. **Groups** have their own `layout=`: `group id "Title" layout=grid cols=2 { … }`.
5. **Styling** is CSS: `css "theme.css"` or `css { node.db { fill: #e0f2fe; } }`.

## Safety

Diagrams are often shared, so `image=` and `css "…"` may only read files inside the
folder of the `.pdg` file. Use `--allow-outside` to lift that for trusted input.

Next: [Layouts](layouts.md), [Edges and routing](edges.md), [Styling](styling.md).
