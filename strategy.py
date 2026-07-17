# ==========================================
# BYBIT AI SCANNER PRO V3
# STRATEGY ENGINE
# ==========================================

def get_signal(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # =====================================
    # EMA Trend
    # =====================================

    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        score += 30
        reasons.append("Strong Uptrend")

    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        score -= 30
        reasons.append("Strong Downtrend")

    # =====================================
    # RSI
    # =====================================

    if 55 <= last["RSI"] <= 70:
        score += 15
        reasons.append("Healthy RSI")

    elif last["RSI"] > 75:
        score -= 10
        reasons