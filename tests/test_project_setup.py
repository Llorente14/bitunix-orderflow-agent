from pathlib import Path

import yaml


def test_config_contains_prd_pairs() -> None:
    config = yaml.safe_load(Path("config.yaml").read_text(encoding="utf-8"))

    assert config["pairs"] == [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "ADAUSDT",
        "AVAXUSDT",
        "LINKUSDT",
        "DOTUSDT",
    ]


def test_required_runtime_files_exist() -> None:
    required_paths = [
        Path("requirements.txt"),
        Path("config.yaml"),
        Path("state.json"),
        Path("src/main.py"),
        Path("src/__init__.py"),
    ]

    for path in required_paths:
        assert path.exists(), f"{path} is missing"
