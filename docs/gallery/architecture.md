<!--
SPDX-FileCopyrightText: 2026 The predictygraph Authors

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
