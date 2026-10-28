<!--
SPDX-FileCopyrightText: 2026 The predictygraph Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Getting started

## Install

```sh
uv tool install "predictygraph @ git+https://github.com/predictygraph/predictygraph"
```

This gives you two commands: `predictygraph` and its short alias `pdg`. They are the same.

!!! note "PyPI"
    Once predictygraph is on PyPI, `pip install predictygraph` or `uvx --from predictygraph pdg` will work too.

## Your first diagram

Save this as `hello.pdg`:

```pdg
--8<-- "examples/hello.pdg"
```

Render it:

```sh
pdg hello.pdg
```

That writes `hello.svg` next to it. Open it in a browser:

![hello.pdg, rendered](examples/hello.svg)

## The five things to know

1. **One statement per line.** `;` puts several on one line. `#` followed by a space starts a comment.
2. **Nodes:** `id "Label" .class key=value`. The label is optional.
3. **Edges:** `a -> b "label"`. Chains (`a -> b -> c`) and fan-out (`a -> b, c`) work.
4. **Groups** choose their own layout: `group id "Title" layout=grid cols=2 { … }`.
5. **Styling** is CSS: `css "theme.css"`, `css { node.db { fill: #e0f2fe; } }`, or a built-in theme with `graph theme=nord`.

## Next steps

- [Layouts](guide/layouts.md): how boxes are arranged
- [Themes](guide/themes.md): pick a colour scheme
- [Animation](guide/animation.md): make edges flow
- [Editor support](reference/editors.md): syntax highlighting in Neovim and Helix
