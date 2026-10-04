# Paper Trading Simulator

A Python portfolio project built incrementally, with tests for the accounting rules.
It is also a learning project: each milestone keeps the core decisions small enough
to understand, test, and explain before more features are added.

## Current status: milestone 1

Implemented: opening cash balance, whole-share purchases, holdings, weighted
average purchase cost, input validation, and automated tests. This is an in-memory
backend with a fixed-price demonstration. It does not fetch market data or persist
accounts yet. It cannot sell shares or calculate profit and loss yet.

## Run locally

Requires Python 3.11 or later. From this project folder, on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m paper_trading
```

The example starts with $1,000, buys two AAPL shares at $100 and one at $130,
then reports $670 cash, three shares, $330 total cost, and $110 average cost.
These are example prices, not live quotes. The demo resets every time it runs.

## How the first milestone works

- `src/paper_trading/portfolio.py`: account rules and immutable position snapshots.
- `src/paper_trading/__main__.py`: a small runnable example.
- `tests/test_portfolio.py`: successful purchases and rejection cases.

Money enters the public API as `Decimal("100.00")`, avoiding binary floating-point
errors. Cash and purchase calculations use integer cents internally for exact
addition and multiplication. Average cost is derived from total cost divided by
shares; a repeating decimal may require rounding, so it is never used to reconstruct
the total cost. Display values are rounded to two decimal places.

For this milestone, trades use USD, whole shares, positive prices in whole cents,
and no fees or borrowing. The caller supplies the execution price. Symbol syntax
is checked, but existence on an exchange is not yet verified. Holdings snapshots
are read-only so callers cannot bypass the purchase rules. Each trade validates
before changing cash or holdings. The account currently assumes one caller at a time.

## Next milestones

1. Sell shares; track realized and unrealized P&L and transaction history.
2. Save accounts and trades in SQLite, with atomic transactions and rollback tests.
3. Add a market-data adapter, quote timestamps, and API failure handling; keep tests
   independent of the network. Revisit price precision for the chosen provider.
4. Add an interactive interface and a repeatable demo.
5. Publish setup documentation, screenshots, and verified feature claims on GitHub.

Each milestone should be small enough to explain and review before the next one.
