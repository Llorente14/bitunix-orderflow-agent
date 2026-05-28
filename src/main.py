"""Entry point placeholder for the Bitunix Order Flow Analyzer."""

from __future__ import annotations

from pathlib import Path

import yaml
from dotenv import load_dotenv


def main() -> None:
    """Load local config and print a setup smoke message."""
    load_dotenv()

    config_path = Path("config.yaml")
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    pairs = config.get("pairs", [])

    print(f"Bitunix Order Flow Analyzer setup ready. pairs={len(pairs)}")


if __name__ == "__main__":
    main()

