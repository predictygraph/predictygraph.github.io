# Layouts

Every container (the whole graph, or a `group`) chooses its own layout. Groups are laid
out inside-out, then treated as one box by their parent. That is what makes the output
predictable: changing a group never reshuffles its siblings.

```pdg
--8<-- "examples/layouts.pdg"
```

![Four layouts side by side](examples/layouts.svg)

## Options

- `layout=layered` (default when a group has edges): rank-based flow.
    - `dir=TB|BT|LR|RL`
    - `balance=center|start|end|median`: `median` pulls nodes toward their neighbours.
    - `rank-gap=60 node-gap=30`
    - `order=source|auto`: `source` keeps file order (most stable); `auto` minimises crossings.
- `layout=grid`: `cols=N` or `rows=N`, `align=center|start|end`, `gap=24`.
- `layout=row` / `layout=column`: a single line, with `align=` and `gap=`.
- `layout=radial`: `center=ID` (default: first child), `radius=auto|N`.
- `layout=fixed`: children use `at=x,y`.

Pin individual nodes with `rank=N` (layered) or `row=R col=C` (grid).

See the [spec](spec.md#5-layouts-balancing-styles) for the full rules.
