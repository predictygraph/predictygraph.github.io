<!--
SPDX-FileCopyrightText: 2026 Reza Jelveh

SPDX-License-Identifier: CC-BY-4.0
-->

# Themes

A theme sets every colour in a diagram with one line:

```pdg
graph theme=nord
```

or from the command line, without touching the file:

```sh
pdg diagram.pdg --theme dracula
```

Each sample below is the same diagram. Moving edges and pulsing borders are part of the
sample, so you can see how animation looks in each theme.

## Light themes

<div class="theme-grid" markdown>

<figure markdown>
![default](../examples/themes/default.svg)
<figcaption>default</figcaption>
</figure>

<figure markdown>
![github-light](../examples/themes/github-light.svg)
<figcaption>github-light</figcaption>
</figure>

<figure markdown>
![solarized-light](../examples/themes/solarized-light.svg)
<figcaption>solarized-light</figcaption>
</figure>

<figure markdown>
![catppuccin-latte](../examples/themes/catppuccin-latte.svg)
<figcaption>catppuccin-latte</figcaption>
</figure>

<figure markdown>
![hami](../examples/themes/hami.svg)
<figcaption>hami</figcaption>
</figure>

</div>

## Dark themes

<div class="theme-grid" markdown>

<figure markdown>
![nord](../examples/themes/nord.svg)
<figcaption>nord</figcaption>
</figure>

<figure markdown>
![dracula](../examples/themes/dracula.svg)
<figcaption>dracula</figcaption>
</figure>

<figure markdown>
![gruvbox-dark](../examples/themes/gruvbox-dark.svg)
<figcaption>gruvbox-dark</figcaption>
</figure>

<figure markdown>
![solarized-dark](../examples/themes/solarized-dark.svg)
<figcaption>solarized-dark</figcaption>
</figure>

<figure markdown>
![catppuccin-frappe](../examples/themes/catppuccin-frappe.svg)
<figcaption>catppuccin-frappe</figcaption>
</figure>

<figure markdown>
![catppuccin-macchiato](../examples/themes/catppuccin-macchiato.svg)
<figcaption>catppuccin-macchiato</figcaption>
</figure>

<figure markdown>
![catppuccin-mocha](../examples/themes/catppuccin-mocha.svg)
<figcaption>catppuccin-mocha</figcaption>
</figure>

</div>

## Colour classes

Every theme provides the same classes, so a diagram keeps its meaning when you switch themes:

- **Hues:** `.red`, `.orange`, `.yellow`, `.green`, `.cyan`, `.blue`, `.purple`
- **Roles:** `.accent` (the theme's highlight colour) and `.danger`
- **Inverted:** `.solid` (text on a filled box)

On a node or group, a class gives a soft fill with a strong outline. On an edge, it colours the line and its label.

```pdg
db "Store" shape=cylinder .blue
sched -> pool .accent
```

## Your own CSS on top

A theme is applied first, then your stylesheets, so you can change single things:

```pdg
graph theme=nord
css { node.hami { font-weight: bold; } }
```

## Make your own theme

A theme is a small TOML file. Start from a copy of a built-in one:

```toml
schema = 1
name = "my-theme"
dark = true

[palette]          # every colour is #rrggbb
bg = "#2e3440"
surface = "#3b4252"
fg = "#eceff4"
muted = "#d8dee9"
border = "#81a1c1"
red = "#bf616a"
orange = "#d08770"
yellow = "#ebcb8b"
green = "#a3be8c"
cyan = "#88c0d0"
blue = "#81a1c1"
purple = "#b48ead"

[roles]            # optional: which palette colour plays which role
accent = "cyan"
edge = "cyan"

[shape]            # optional
font = "DejaVu Sans"
radius = 6
edge-width = 1.5
```

- Use it with `graph theme=my-theme.toml` (a path next to the diagram) or put it in a folder listed in `PDG_THEME_PATH`.
- `extends = "nord"` starts from another theme and changes only the colours you list.
- `css = """ ... """` (before the first `[table]`) adds your own rules after the generated
  ones, with the palette available as variables. The `hami` theme uses it for header
  bands, accent bars and grey second lines. With `extends`, both themes' rules apply,
  the parent's first.
- **Roles:** `accent`, `danger`, `node-fill`, `node-stroke`, `node-text`, `group-fill`, `group-stroke`, `group-text`, `edge`, `edge-text`.
- Soft variants (`--red-soft` and so on) and `--bg-alt` are mixed automatically.

All palette colours and roles are also CSS variables, for example `var(--accent)`.
