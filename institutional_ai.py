# ==========================================
# BYBIT AI SCANNER PRO V4
# INSTITUTIONAL AI ENGINE
# ==========================================

def analyze_institutional_ai(df, trend, smart_money):

    score = 0
    reasons = []

    institutional_confidence = 0

    # ===============================
    # Trend Analysis (40 points)
    # ===============================

    if trend["trend"] == "BULLISH":
        score += 40
        institutional_confidence += 40
        reasons.append("Strong Bullish Trend")

    elif trend["trend"] == "BEARISH":
        score += 40
        institutional_confidence += 40
        reasons.append("Strong Bearish Trend")

    # ===============================
    # Smart Money (30 points)
    # ===============================

    if smart_money["score"] >= 70:
        score += 30
        institutional_confidence += 30
        reasons.append("Institutional Buying Activity")

    elif smart_money["score"] >= 40:
        score += 15
        institutional_confidence += 15
        reasons.append("Moderate Smart Money")

    # ===============================
    # Volume Confirmation (20 points)
    # ===============================

    last = df.iloc[-1]

    if last["volume"] > last["VOL_MA"]:
        score += 20
        institutional_confidence += 20
        reasons.append("High Volume Confirmation")

    # ===============================
    # ADX Confirmation (10 points)
    # ===============================

    if last["ADX"] > 25:
        score += 10
        institutional_confidence += 10
        reasons.append("Strong Trend Strength")

    return {
        "score": score,
        "confidence": institutional_confidence,
        "reasons": reasons
    }