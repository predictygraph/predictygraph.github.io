# Edges and routing

## Arrow tokens

An arrow is an optional `<`, a body of `-`, `=` or `.`, and an optional `>`.

- `-` solid, `=` thick, `.` dashed
- `>` at the end puts a head on the target, `<` at the start on the source
- `a -- b` draws no heads

```pdg
--8<-- "examples/arrows.pdg"
```

![Arrow tokens](examples/arrows.svg)

## Routing styles

`route=curve|bend|ortho|straight`, per edge, per group (`default edge route=…`) or graph-wide.

```pdg
--8<-- "examples/routes.pdg"
```

![Four routing styles](examples/routes.svg)

## Diagonals

`bend` and `ortho` edges have one sideways jog. `diagonal=N` lets that jog slant
when the offset is at most N px; `diagonal-angle=45` sets the slant.

```pdg
--8<-- "examples/diagonal.pdg"
```

![Diagonal jogs](examples/diagonal.svg)

## Useful attributes

- `width=3`, `head=triangle|open|diamond|dot|bar`, `head-size=N`
- `arrow=none|end|start|both` overrides the token
- `exit=top|bottom|left|right`, `enter=…` pin a side
- `weight=N`, `constraint=false` tune the layered layout

Full details: [spec, section 3](spec.md#3-edges).
