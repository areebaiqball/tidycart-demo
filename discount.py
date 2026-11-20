"""Discount helpers."""


def apply_discount(total: float, percent: float) -> float:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total * (1 - percent / 100), 2)
