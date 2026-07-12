#!/usr/bin/env python3
"""Fetch extra test data from the ``data-extra`` branch.

Extra datasets (agilent, jeol, bruker_3d, simpson, tecmag) are stored on a
separate branch to keep the main download lightweight.  This script performs
a shallow clone of that branch into a local directory.

Usage (CLI)
-----------
    python scripts/fetch_extra.py
    python scripts/fetch_extra.py --target /custom/path

Usage (Python)
--------------
    from scripts.fetch_extra import fetch_extra
    fetch_extra()
    fetch_extra(target=Path("/custom/path"))
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

_REPO_URL = "https://github.com/spectrochempy/spectrochempy_data.git"
_BRANCH = "data-extra"
_DEFAULT_MARKER = "__downloaded_extra__"
_DEFAULT_TARGET = Path.home() / ".spectrochempy" / "testdata-extra"


def fetch_extra(
    target: Path | str | None = None,
    force: bool = False,
) -> Path:
    """Clone the ``data-extra`` branch into *target* (shallow, idempotent).

    Parameters
    ----------
    target : Path or str, optional
        Destination directory.  Defaults to ``~/.spectrochempy/testdata-extra/``.
    force : bool, optional
        If True, re-download even if the marker file already exists.

    Returns
    -------
    Path
        The path to the downloaded extra test data.
    """
    target = Path(target) if target else _DEFAULT_TARGET
    marker = target / _DEFAULT_MARKER

    if marker.exists() and not force:
        return target

    target.mkdir(parents=True, exist_ok=True)

    # Remove partial clone if marker is missing (incomplete previous attempt)
    if not marker.exists() and any(target.iterdir()):
        shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)

    cmd = [
        "git",
        "clone",
        "--branch",
        _BRANCH,
        "--depth",
        "1",
        "--single-branch",
        _REPO_URL,
        str(target),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        msg = f"git clone failed (exit {result.returncode}):\n{result.stderr}"
        raise RuntimeError(msg)

    # Remove .git directory — we only need the data files
    git_dir = target / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)

    # Write marker
    marker.write_text("spectrochempy-testdata-extra-v1\n", encoding="utf-8")

    return target


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch extra test data from the data-extra branch.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=None,
        help="Destination directory (default: ~/.spectrochempy/testdata-extra/)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even if already present",
    )
    args = parser.parse_args()

    path = fetch_extra(target=args.target, force=args.force)
    print(f"Extra test data available at: {path}")


if __name__ == "__main__":
    main()
