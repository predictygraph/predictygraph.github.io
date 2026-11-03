<!--
SPDX-FileCopyrightText: 2026 Reza Jelveh

SPDX-License-Identifier: CC-BY-4.0
-->

# Architecture

## HAMi scheduling

Three layouts in one file: a step-by-step control plane, a grid of GPU nodes and a
monitoring column. Each group arranges itself, so changing one never moves the others.

=== "Picture"

    ![HAMi scheduling](../examples/hami_flow.svg)

=== "Source"

    ```pdg
    --8<-- "examples/hami_flow.pdg"
    ```

### Same file, square corners

Only the `graph` line changes: `route=ortho` draws edges with right angles.

=== "Picture"

    ![HAMi scheduling, right-angle edges](../examples/hami_flow_ortho.svg)

=== "Source"

    ```pdg
    --8<-- "examples/hami_flow_ortho.pdg"
    ```

## GPU box to GPU cloud

A layered stack from hardware to platform, converted from a Graphviz diagram.

=== "Picture"

    ![GPU box to GPU cloud](../examples/blueprint/blueprint.svg)

=== "Source"

    ```pdg
    --8<-- "examples/blueprint/blueprint.pdg"
    ```

## Animated blueprint

The same idea with moving edges showing where requests go.

=== "Picture"

    ![Animated blueprint](../examples/animation/blueprint_flow.svg)

=== "Source"

    ```pdg
    --8<-- "examples/animation/blueprint_flow.pdg"
    ```

## Edges to groups

An edge can end on a whole group instead of a single node.

=== "Picture"

    ![Edges to groups](../examples/square.svg)

=== "Source"

    ```pdg
    --8<-- "examples/square.pdg"
    ```

## HAMi documentation figures

Three figures from the HAMi docs, redrawn with the `hami` theme. They use second lines
(`sub=`), numbered steps, header bands, accent bars, a legend and a caption.

### A Pod's path to a shared GPU

Two panels with their own column layouts, numbered steps, and a notes panel.

=== "Picture"

    ![Pod to GPU](../examples/hami/pod_to_gpu.svg)

=== "Source"

    ```pdg
    --8<-- "examples/hami/pod_to_gpu.pdg"
    ```

### The GPU stack

`align=stretch` gives five tiers of equal width; the HAMi component is highlighted
and named in the legend.

=== "Picture"

    ![GPU stack](../examples/hami/gpu_stack.svg)

=== "Source"

    ```pdg
    --8<-- "examples/hami/gpu_stack.pdg"
    ```

### NVIDIA kernel modules

Three stacked panels with vertical titles (`label-position: left`), a dashed box marking
the compute modules, an edge that goes around the display modules
(`exit=left enter=left`), and two side brackets (`bracket nvidia, drm "..."`).

=== "Picture"

    ![NVIDIA kernel modules](../examples/hami/kernel_modules.svg)

=== "Source"

    ```pdg
    --8<-- "examples/hami/kernel_modules.pdg"
    ```
