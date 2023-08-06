from decimal import Decimal, ROUND_HALF_UP


def mathematicalRound(value: float, decimalPlaces: int) -> float:
    decimal = Decimal(str(value))
    places = Decimal(10) ** -decimalPlaces

    return float(decimal.quantize(places, rounding = ROUND_HALF_UP))
