<!--
SPDX-FileCopyrightText: 2026 Reza Jelveh

SPDX-License-Identifier: CC-BY-4.0
-->

# Getting started

![Your diagram called. It wants its boxes back where you left them.](assets/brand/diagram-called.webp){ .comic .meme loading=lazy }

## Install

```sh
uv tool install "predictygraph[apng]"     # or: pipx install "predictygraph[apng]"
```

This gives you two commands: `predictygraph` and its short alias `pdg`. They are the same.
`[apng]` adds PNG output; leave it out if you only need SVG.

To try it without installing: `uvx --from predictygraph pdg hello.pdg`.

## Let your AI agent draw diagrams

predictygraph ships an [agent skill](https://github.com/predictygraph/predictygraph/tree/master/skills/predictygraph):
instructions, a syntax summary and examples that teach an AI agent to write `.pdg` files,
render them and check the result.

- **Hermes Agent:**

    ```sh
    hermes skills install https://raw.githubusercontent.com/predictygraph/predictygraph/master/skills/predictygraph/SKILL.md
    ```

- **Claude Code and other agents that read `SKILL.md` folders:** copy the
  [`skills/predictygraph`](https://github.com/predictygraph/predictygraph/tree/master/skills/predictygraph)
  folder into the agent's skills directory (for Claude Code: `~/.claude/skills/`).

Then ask for a diagram, for example "draw our request path from the browser to the
database as a predictygraph diagram".

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
