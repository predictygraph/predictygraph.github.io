# Editor support

Syntax highlighting, folding, indentation and CSS highlighting inside `css { … }`
blocks come from [tree-sitter-pdg](https://github.com/predictygraph/tree-sitter-pdg).

## Neovim

With [lazy.nvim](https://github.com/folke/lazy.nvim) and nvim-treesitter:

```lua
{ "predictygraph/tree-sitter-pdg", dependencies = { "nvim-treesitter/nvim-treesitter" } }
```

Then run `:TSInstall pdg`. `*.pdg` files get the `pdg` filetype automatically.

## Helix

```toml
[[language]]
name = "pdg"
scope = "source.pdg"
file-types = ["pdg"]
comment-token = "#"

[[grammar]]
name = "pdg"
source = { git = "https://github.com/predictygraph/tree-sitter-pdg", rev = "master" }
```

Run `hx --grammar fetch && hx --grammar build`, then copy `queries/pdg/` from the
grammar repo to `~/.config/helix/runtime/queries/pdg/`.

## Others

Zed, Emacs (`treesit`) and any other tree-sitter host can load the grammar and the
queries in `queries/pdg/`.
