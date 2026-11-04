<!--
SPDX-FileCopyrightText: 2026 Reza Jelveh

SPDX-License-Identifier: CC-BY-4.0
-->

# predictygraph

**Predictable graphs.** Diagrams as readable text, laid out the way you said, styled with plain CSS.

![A developer adds one box and the diagram turns to spaghetti. A buff guy bursts through the wall with diagram.pdg, and the diagram comes out the same way every time.](assets/brand/comic-strip.webp){ .comic }

<div class="grid cards" markdown>

-   **Start here**

    Install, write your first diagram, render it.

    [Getting started](getting-started.md)

-   **Learn the language**

    Layouts, edges, styling, annotations, themes and animation, one page each.

    [Guide](guide/index.md)

-   **See what it can do**

    Architecture diagrams, flowcharts and the usual Mermaid diagram types.

    [Gallery](gallery/index.md)

-   **Look something up**

    The full language spec, every command-line option, editor setup.

    [Reference](reference/index.md)

</div>

![HAMi scheduling flow](examples/themes/hami.svg)

Mermaid and Graphviz rearrange your whole picture when you change one box.
predictygraph doesn't: **each group picks its own layout**, so a change stays where you made it.

## A taste

```pdg
--8<-- "examples/hello.pdg"
```

![The snippet above, rendered](examples/hello.svg)

Reuse a block with `def` and `use`, and share values with `let`:

```pdg
--8<-- "examples/blocks.pdg"
```

![The snippet above, rendered](examples/blocks.svg)

## Why predictygraph

- **Readable diffs.** One statement per line. No XML, no coordinates.
- **Mix layouts.** Each box arranges its own contents. Put a grid of servers inside a step-by-step flow, and a circle of nodes inside that grid.
- **Plain CSS.** Style with the CSS you know. No browser, no JavaScript.
- **Same input, same picture.** Every viewer shows the same SVG.
- **Animated when you want it.** Moving edges and pulsing borders, in a single small SVG file.
- **Themes included.** Twelve colour themes, from Nord to Catppuccin. [See them all](guide/themes.md).
