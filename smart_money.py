# ==========================================
# BYBIT AI SCANNER PRO V4
# SMART MONEY ENGINE
# ==========================================

def analyze_smart_money(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # ===============================
    # High Volume
    # ===============================

    if last["volume"] > last["VOL_MA"]:
        score += 30
        reasons.append("High Volume")

    # ===============================
    # EMA Trend
    # ===============================

    if last["EMA20"] > last["EMA50"]:
        score += 20
        reasons.append("EMA Bullish")

    elif last["EMA20"] < last["EMA50"]:
        score += 20
        reasons.append("EMA Bearish")

    # ===============================
    # RSI
    # ===============================

    if 50 <= last["RSI"] <= 70:
        score += 20
        reasons.append("Healthy RSI")

    # ===============================
    # MACD
    # ===============================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 30
        reasons.append("MACD Bullish")

    return {
        "score": score,
        "reasons": reasons
    }