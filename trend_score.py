# ==========================================
# BYBIT AI SCANNER PRO V4
# TREND SCORING ENGINE
# ==========================================

def calculate_trend_score(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # Strong Bullish Trend
    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        score = 25
        reasons.append("Strong Bullish Trend")

    # Strong Bearish Trend
    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        score = 20
        reasons.append("Strong Bearish Trend")

    # Mixed Trend
    else:
        score = 10
        reasons.append("Mixed Trend")

    return {
        "score": score,
        "reasons": reasons
    }