# papertradingsim

A Python paper-trading simulator built incrementally with tested portfolio accounting and clean backend architecture.

## Phase 0

The project currently provides:

- a Python package using the `src` layout;
- a Flask application factory;
- environment-based configuration;
- a `GET /health` endpoint; and
- a small pytest suite.

## Setup

Create and activate a virtual environment, then install the project and its
development dependencies:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Copy `.env.example` to `.env` and replace the placeholder API key when a market
data provider is introduced. The health endpoint does not require an API key.

## Run

```powershell
python -m flask --app papertradingsim.app run --debug
```

Then open `http://127.0.0.1:5000/health`.

## Test

```powershell
python -m pytest
```
