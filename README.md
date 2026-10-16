# Quiche Math

Quiche custard honesty. The recipe says bake until just set, and the ratio decided that before the oven did. Quiche Math does the ratio, batch and pan arithmetic a quiche depends on, with every norm labeled.

## What it computes

- **The ratio truth** - eggs and dairy read against the classic 1 egg to half a cup (a labeled kitchen norm): cups per egg rounded to tenths, then judged firmer and richer, right at the classic ratio, or loose enough to risk weeping.
- **The batch truth** - total custard volume with a large egg counted as about a fifth of a cup (a labeled kitchen norm).
- **The pan truth** - a 9-inch pie dish holds about 4 cups at the same depth and capacity scales with pan area (a labeled kitchen norm): your custard fits with cups to spare, fills it exactly, or overflows by a counted amount.

## Boundary

Illustrative arithmetic only. Every norm is a labeled kitchen norm; your recipe and your actual dish depth win every tie. Quiche Math never judges doneness or food safety - follow your recipe's bake guidance.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (28 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/quichemath/
Repo: https://github.com/iLanis-agent/quichemath
