<!--
SPDX-FileCopyrightText: 2026 Reza Jelveh

SPDX-License-Identifier: CC-BY-4.0
-->

# Animation

Animation makes a diagram show *what moves where*: requests travelling to a server,
data flowing into a database, the one component that's busy.

It never changes the layout. The first frame is always the complete diagram, so
PDFs, printouts and image viewers that don't animate still show everything.

!!! info "Use SVG"
    Animated diagrams are written as SVG. They play in every modern browser, stay
    sharp at any zoom, and are tiny: every animation on this page is under 20 KB.

## Moving edges

Add `flow=` to an edge to send dots along it.

```pdg
--8<-- "examples/animation/flows.pdg"
```

![Flow directions](../examples/animation/flows.svg)

- `flow=forward`: dots travel from source to target.
- `flow=reverse`: dots travel from target to source.
- `flow=both`: two streams, one each way.
- `flow=auto`: follow the arrowheads (`->` forward, `<-` reverse, `<->` both).

## Speed

`flow-speed=` sets how long one cycle takes. Smaller is faster. The default is `1.2s`;
`ms` works too. A dashed edge (`..>`) animates its own dashes instead of dots.

```pdg
--8<-- "examples/animation/speeds.pdg"
```

![Flow speeds](../examples/animation/speeds.svg)

## Animated borders

`border=` animates the outline of a node or group. `border-speed=` sets the cycle time
(default `1.6s`).

```pdg
--8<-- "examples/animation/borders.pdg"
```

![Border styles](../examples/animation/borders.svg)

- `border=march`: a dashed outline that crawls around the box.
- `border=pulse`: the outline grows and fades.
- `border=glow`: a halo spreads out and fades behind the box.

## Animate with CSS

Every animation setting is also a CSS property, so you can mark things with a class
and animate them all at once.

```pdg
--8<-- "examples/animation/css.pdg"
```

![Animation via CSS](../examples/animation/css.svg)

## Everything together

```pdg
--8<-- "examples/animation/showcase.pdg"
```

![Showcase](../examples/animation/showcase.svg)

## Settings at a glance

- **Edges:** `flow=forward|reverse|both|auto`, `flow-speed=1.2s`
- **Nodes and groups:** `border=march|pulse|glow`, `border-speed=1.6s`
- **Where they work:** on a single item, in `default node|edge|group`, as CSS properties,
  and (`flow-speed` only) on the `graph` line.

## Static output

```sh
pdg x.pdg --static      # no animation, first frame
pdg x.pdg --at 0.4      # frozen at 0.4 s
pdg x.pdg -o x.png      # animated PNG, for places that can't show SVG (much larger)
```

## Trunkline

The `trunkline` theme pairs `flow=draw`, `flow-dot=ring`, `grid=` and `corner-marks` for a dark network-planner look.

```pdg
--8<-- "examples/animation/trunkline.pdg"
```

![Trunkline](../examples/animation/trunkline.svg)
