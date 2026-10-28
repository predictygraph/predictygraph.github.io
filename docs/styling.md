# Styling and themes

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

Precedence: built-in defaults < stylesheets < `default` statements < inline attributes.

## Properties

- **Box:** `fill`, `stroke`, `stroke-width`, `stroke-dasharray`, `border-radius`, `padding`,
  `min-width`, `min-height`, `opacity`, `shadow`
- **Text:** `color`, `font-family`, `font-size`, `font-weight`, `font-style`, `text-align`
- **Edge:** `stroke`, `stroke-width`, `stroke-dasharray`, `arrow`, `head`, `route`
- **Variables:** `--name: value` and `var(--name, fallback)`

## Built-in themes

Pick one with `graph theme=NAME`:

`default`, `nord`, `dracula`, `github-light`, `gruvbox-dark`, `solarized-light`,
`solarized-dark`, `catppuccin-latte`, `catppuccin-frappe`, `catppuccin-macchiato`,
`catppuccin-mocha`.

Example stylesheet used throughout these docs:

```css
--8<-- "examples/theme.css"
```
