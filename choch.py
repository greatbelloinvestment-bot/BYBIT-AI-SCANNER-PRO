# ==========================================
# BYBIT AI SCANNER PRO V4
# CHANGE OF CHARACTER (CHOCH)
# ==========================================

def detect_choch(df):

    if len(df) < 6:
        return {
            "choch": False,
            "direction": "NONE",
            "strength": 0,
            "reasons": ["Not enough candles"]
        }

    highs = df["high"].tail(5).tolist()
    lows = df["low"].tail(5).tolist()

    bullish = highs[-1] > highs[-2] and lows[-1] > lows[-2]
    bearish = highs[-1] < highs[-2] and lows[-1] < lows[-2]

    if bullish:
        return {
            "choch": True,
            "direction": "BULLISH",
            "strength": 85,
            "reasons": ["Bullish CHOCH detected"]
        }

    if bearish:
        return {
            "choch": True,
            "direction": "BEARISH",
            "strength": 85,
            "reasons": ["Bearish CHOCH detected"]
        }

    return {
        "choch": False,
        "direction": "NONE",
        "strength": 0,
        "reasons": ["No CHOCH detected"]
    }