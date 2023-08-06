"""pkdb_data - Python utilities for PK-DB."""

from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "1.0.3"

program_name: str = "pkdb_data"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
CACHE_USE: bool = True
CACHE_PATH: Path = RESOURCES_DIR / "cache"
