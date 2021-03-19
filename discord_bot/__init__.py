"""
Module init file
"""

from pathlib import Path

# Read version on startup
version = (Path(__file__).parent.parent / "VERSION").open("r").readline().strip()
github_url = "https://github.com/rekolae/HurrDurrDiscordBot"
