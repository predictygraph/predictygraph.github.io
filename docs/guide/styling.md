<!--
SPDX-FileCopyrightText: 2026 The predictygraph Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Styling

Styling is a small, documented subset of CSS. predictygraph resolves it itself and
writes plain presentation attributes, so the SVG looks the same everywhere.

```pdg
graph theme=nord
css "theme.css"                       # external stylesheet, next to the .pdg file
css {
  node.db  { fill: #e0f2fe; stroke: #0284c7; }
  edge.hot { stroke: #dc2626; stroke-width: 3; flow: forward; }
  #k8s node { font-weight: 600; }
}
```

## Selectors

`node`, `edge`, `group`, `graph`, `label`, `.class`, `#id`, compounds (`node.db`) and
group descendants (`#cluster node`). Specificity and source order follow CSS.

Text parts have their own selectors: `sub` (the `sub=` second line), `step` (numbered
circles on edges), `legend`, `caption` and `bracket` (side brackets). Scope them like
descendants: `node.core sub { color: #dcfce7; }`.

Precedence: built-in defaults < stylesheets < `default` statements < inline attributes.

## Properties

- **Box:** `fill`, `stroke`, `stroke-width`, `stroke-dasharray`, `border-radius`, `padding`,
  `min-width`, `min-height`, `opacity`, `shadow`, `accent-bar` (`4px #16a34a`, a strip
  inside the left edge), `accent-side`, `title-fill` (groups: a band behind the title),
  `label-position: top|bottom|left` (groups; `left` turns the title vertical)
- **Text:** `color`, `font-family`, `font-size` (`em` and `%` are relative to the owner),
  `font-weight`, `font-style`, `text-align`
- **Edge:** `stroke`, `stroke-width`, `stroke-dasharray`, `arrow`, `head`, `route`
- **Variables:** `--name: value` and `var(--name, fallback)`

## Themes

For ready-made colour schemes, set `graph theme=NAME`. See [Themes](themes.md) for all eleven, side by side.
Your own CSS is applied on top of the theme.

## Example stylesheet

```css
--8<-- "examples/theme.css"
```
