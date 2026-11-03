<!--
SPDX-FileCopyrightText: 2026 The predictygraph Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Annotations

Notes, numbers and keys that explain a diagram: second lines in boxes, numbered steps,
brackets, a legend and a caption. Plus two layout helpers that make diagrams read better:
equal-sized panels and boxes lined up across panels.

Everything on this page in one diagram:

=== "Picture"

    ![Annotations tour](../examples/annotations.svg)

=== "Source"

    ```pdg
    --8<-- "examples/annotations.pdg"
    ```

## Second lines

`sub="..."` puts a smaller, grey line under a box's label. It works on panels too.

```pdg
api "API gateway" sub="checks the token"
group app "Application" sub="runs in Kubernetes" { ... }
```

Style it with the `sub` selector: `node.core sub { color: #dcfce7; }`. Use `\n` for more
than one line.

## Numbered steps

`graph steps=auto` numbers every arrow in the order the file lists them. Set one by hand
with `step=N`; hand-set numbers are skipped by the automatic count.

```pdg
graph steps=auto
browser -> cdn
cdn -> api "cache miss"
```

A step sits just left of the arrow's label. Without a label it sits on the arrow a third of
the way along, or beside the arrow when the arrow is too short to hold it, so it never
covers a box. Gaps in a column grow to fit it. Style it with `step`: `step { fill: var(--green); }`.

## Brackets

`bracket a, d "note"` draws a curly bracket on the right, from the top of the highest box
listed to the bottom of the lowest, with the note beside it. Overlapping brackets stack
outwards, shortest nearest the diagram. Style with `bracket`.

```pdg
bracket api, db "runs in our\ncluster"
```

## Legend and caption

```pdg
legend "Key"                     # names the key box
legend .green "our services"     # one entry, drawn like a box with class .green
graph caption="Figure 1: ..."    # a line of text under everything
```

Style them with `legend` and `caption`.

## Side titles, side strips, title bands

These are CSS properties:

- `label-position: left` turns a panel's title sideways down its left edge.
- `accent-bar: 4px #16a34a` draws a coloured strip on a box's left side;
  `accent-side: right` moves it. It follows the box's rounded corners.
- `title-fill: #dbeafe` fills a band behind a panel's title.

## Equal sizes

`align=stretch` on a row or column makes every child as big as the largest: equal-width
layers in a column, equal-height panels in a row.

```pdg
graph layout=column align=stretch
```

## Lining up boxes across panels

Each panel centres its own boxes, so a box rarely ends up straight above the one it
connects to in the next panel. `align-x=ID` moves a box (or a whole group) sideways until
it is centred on another box:

```pdg
group data "Data" layout=row {
  db "PostgreSQL" shape=cylinder align-x=orders
}
```

The box only moves within its own panel. Boxes on the side it moves towards move with it,
so the gaps between them, and any labels in those gaps, stay as they were.
