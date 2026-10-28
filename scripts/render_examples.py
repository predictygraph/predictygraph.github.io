#!/usr/bin/env python3
"""Render every .pdg under docs/ to SVG (static) and APNG (animated) next to its source."""
import argparse
import sys
from pathlib import Path

from predictygraph import scene_from_file, write_apng, write_svg


class ExampleRenderer:
    def __init__(self, root: Path, apng: bool):
        self.root, self.apng = root, apng
        self.failed: list[str] = []

    def render(self, src: Path) -> None:
        try:
            scene = scene_from_file(src)
            src.with_suffix(".svg").write_text(write_svg(scene, None), encoding="utf-8")
            if self.apng:
                write_apng(scene, src.with_suffix(".png"), 20, 2.0, None)
            print(f"ok   {src.relative_to(self.root)}")
        except Exception as exc:  # report every broken example, not just the first
            self.failed.append(f"{src.relative_to(self.root)}: {exc}")
            print(f"FAIL {src.relative_to(self.root)}: {exc}", file=sys.stderr)

    def run(self) -> int:
        for src in sorted(self.root.rglob("*.pdg")):
            self.render(src)
        return 1 if self.failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", type=Path, default=Path("docs"))
    ap.add_argument("--apng", action="store_true", help="also write animated PNGs")
    args = ap.parse_args()
    return ExampleRenderer(args.root, args.apng).run()


if __name__ == "__main__":
    sys.exit(main())
