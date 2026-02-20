from __future__ import annotations


def compute_liquidity_score(days_on_market: float, listing_count: int) -> float:
    """Simple placeholder liquidity score on a 0-100 scale."""
    velocity_component = max(0.0, 100.0 - days_on_market)
    depth_component = min(100.0, listing_count * 2.0)
    return round((velocity_component * 0.6) + (depth_component * 0.4), 2)
