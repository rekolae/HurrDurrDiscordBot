"""
Module init file
"""

from pathlib import Path

# Read version on startup
version_file = Path(__file__).parent.parent / "VERSION"
version = version_file.open("r").readline().strip()
