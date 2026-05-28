# Bitunix Order Flow Analyzer

Automated order flow analyzer for Bitunix Futures. It monitors configured
USDT perpetual pairs, detects bid/ask imbalance, and sends Discord alerts.

No auto-trading. Analysis and portfolio project only.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python -m src.main
```

## Configuration

- `config.yaml` stores pairs, thresholds, Bitunix API settings, and runtime settings.
- `.env` stores local secret values and is ignored by git.
- `state.json` stores runtime signal state for cooldown and deduplication.

## PRD Baseline

Target pairs:

- BTCUSDT
- ETHUSDT
- BNBUSDT
- SOLUSDT
- XRPUSDT
- DOGEUSDT
- ADAUSDT
- AVAXUSDT
- LINKUSDT
- DOTUSDT
