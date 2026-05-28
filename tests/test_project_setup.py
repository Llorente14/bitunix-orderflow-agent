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


def test_manual_github_actions_workflow_has_pip_cache() -> None:
    workflow = Path(".github/workflows/analyze.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch:" in workflow
    assert "actions/setup-python@v5" in workflow
    assert 'default: "3.11"' in workflow
    assert '          - "3.12"' in workflow
    assert "Cache pip dependencies" in workflow
    assert "actions/cache@v4" in workflow
    assert "~/.cache/pip" in workflow
    assert "hashFiles('requirements.txt')" in workflow
    assert "python -m src.main" in workflow
