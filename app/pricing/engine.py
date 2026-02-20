from __future__ import annotations

from statistics import median


def compute_median_price(prices: list[float]) -> float | None:
    """Compute median asking/sold price."""
    if not prices:
        return None
    return float(median(prices))


def compute_floor_price(prices: list[float]) -> float | None:
    """Compute floor price (minimum) from listings."""
    if not prices:
        return None
    return min(prices)
