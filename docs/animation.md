# Animation

Animation never changes the layout. Frame zero is always the complete diagram, so
static viewers and PDFs stay correct.

```pdg
--8<-- "examples/animation/showcase.pdg"
```

![Animation showcase](examples/animation/showcase.png)

## Edge flows

- `flow=forward|reverse|both|auto`
- `flow-speed=1.2s`

## Animated borders

- `border=march|pulse|glow`
- `border-speed=1.6s`

All keys also work in `default` statements and as CSS properties:
`edge.hot { flow: forward; flow-speed: .6s; }`.

## Output

- `pdg x.pdg`: animated SVG (SMIL, plays in browsers)
- `pdg x.pdg --static` or `--at 0.4`: frozen SVG
- `pdg x.pdg -o x.png`: animated PNG, one seamless loop. `--fps`, `--scale`, `--seconds` tune it.

## A bigger example

```pdg
--8<-- "examples/animation/blueprint_flow.pdg"
```

![HAMi blueprint flow](examples/animation/blueprint_flow.png)
