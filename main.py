#!/usr/bin/env python3
"""news-image-20261119 entry, v2 "Solemn Verdict" (Python 3.13, standard library only).

The entry is the infographic in entry.png: six labelled story cards
summing up the world news of Thursday 19 November 2026. This program
copies that file to the output directory byte for byte, so the two
grading runs produce identical output.

Local check:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    # The gate only reads /output/entry.png, so keep that exact name.
    destination = destination_dir / "entry.png"
    shutil.copyfile(ENTRY, destination)
    written = destination.stat().st_size
    expected = ENTRY.stat().st_size
    if written != expected:
        raise RuntimeError(f"entry.png copy is incomplete: {written} != {expected}")
    if _sha256(destination) != _sha256(ENTRY):
        raise RuntimeError("entry.png copy differs from the source image")


if __name__ == "__main__":
    main()
