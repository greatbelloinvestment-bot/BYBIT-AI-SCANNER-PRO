# ==========================================
# BYBIT AI SCANNER PRO V4
# BREAK OF STRUCTURE (BOS)
# ==========================================

import pandas as pd


def detect_bos(df, lookback=20):

    if len(df) < lookback + 5:
        return {
            "bos": False,
            "direction": "NONE",
            "strength": 0,
            "level": None,
            "reasons": ["Not enough candles"]
        }

    highs = df["high"].tail(lookback)
    lows = df["low"].tail(lookback)

    highest_high = highs.max()
    lowest_low = lows.min()

    last_close = df.iloc[-1]["close"]
    previous_close = df.iloc[-2]["close"]

    # ==========================
    # Bullish BOS
    # ==========================

    if previous_close <= highest_high and last_close > highest_high:

        return {
            "bos": True,
            "direction": "BULLISH",
            "strength": 90,
            "level": highest_high,
            "reasons": [
                "Price closed above previous structure high"
            ]
        }

    # ==========================
    # Bearish BOS
    # ==========================

    if previous_close >= lowest_low and last_close < lowest_low:

        return {
            "bos": True,
            "direction": "BEARISH",
            "strength": 90,
            "level": lowest_low,
            "reasons": [
                "Price closed below previous structure low"
            ]
        }

    return {
        "bos": False,
        "direction": "NONE",
        "strength": 0,
        "level": None,
        "reasons": [
            "No confirmed Break of Structure"
        ]
    }