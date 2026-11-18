"""News Image 18 Nov 2026 entry: copy the drawn image to the output dir.
Standard library only. Deterministic: same bytes on every run.
"""
import os
import pathlib
import shutil

src = pathlib.Path(__file__).resolve().parent / "entry.png"
out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
