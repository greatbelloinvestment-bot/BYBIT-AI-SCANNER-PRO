# ==========================================
# BYBIT AI SCANNER PRO V4
# MOMENTUM SCORING ENGINE
# ==========================================

def calculate_momentum_score(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # ==========================
    # RSI
    # ==========================

    if 55 <= last["RSI"] <= 70:
        score += 8
        reasons.append("Healthy RSI")

    elif last["RSI"] < 30:
        score += 6
        reasons.append("Oversold RSI")

    elif last["RSI"] > 75:
        score -= 4
        reasons.append("Overbought RSI")

    # ==========================
    # MACD
    # ==========================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 8
        reasons.append("MACD Bullish")

    else:
        score += 2
        reasons.append("MACD Bearish")

    # ==========================
    # ADX
    # ==========================

    if last["ADX"] >= 30:
        score += 4
        reasons.append("Strong Trend")

    elif last["ADX"] >= 20:
        score += 2
        reasons.append("Moderate Trend")

    else:
        reasons.append("Weak Trend")

    score = max(0, min(score, 20))

    return {
        "score": score,
        "reasons": reasons
    }