# predictygraph

**Predictable graphs.** Diagrams as readable text, laid out the way you said, styled with plain CSS.

![HAMi scheduling flow](examples/animation/blueprint_flow.png)

Tired of AI-generated diagrams that come out as uneditable HTML or XML? Tired of Mermaid
rearranging your whole graph when you move one box? predictygraph is a small, line-based
language where **each group picks its own layout**. Change one group and nothing else moves.

```pdg
--8<-- "examples/hello.pdg"
```

![The snippet above, rendered](examples/hello.svg)

## Why

- **Readable diffs.** One statement per line. No XML, no coordinates.
- **Local layouts.** A layered flow can contain a grid, which can contain a radial cluster.
- **Plain CSS.** A documented CSS subset, resolved by the tool. No browser, no JavaScript.
- **Same input, same picture.** Deterministic SVG that looks the same in every viewer.
- **Animated when you want it.** Flowing edges and animated borders, as SVG or APNG.

## Install

```sh
pip install predictygraph            # or: uv tool install predictygraph
pdg diagram.pdg                      # -> diagram.svg
```

`pdg` is the short alias of the `predictygraph` command. Continue with
[Getting started](getting-started.md).
