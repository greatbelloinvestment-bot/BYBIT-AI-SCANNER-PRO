# ==========================================
# BYBIT AI SCANNER PRO V4
# INSTITUTIONAL AI ENGINE
# ==========================================
from bos import detect_bos
from choch import detect_choch

def calculate_institutional_score(
    df,
    trade,
    mtf,
    risk
):
    """
    Returns:
        score (0-100)
        grade
        reasons
    """

    score = 0
    reasons = []

    last = df.iloc[-1]

    # ======================================
    # TREND (25)
    # ======================================

    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        score += 25
        reasons.append("Strong Bullish Trend")

    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        score += 20
        reasons.append("Strong Bearish Trend")

    # ======================================
    # MOMENTUM (20)
    # ======================================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 20
        reasons.append("MACD Bullish")

    elif last["MACD"] < last["MACD_SIGNAL"]:
        score += 15
        reasons.append("MACD Bearish")

    # ======================================
    # VOLUME (15)
    # ======================================

    if last["volume"] > last["VOL_MA"]:
        score += 15
        reasons.append("High Volume")

    else:
        score += 5
        reasons.append("Low Volume")

    # ======================================
    # RISK (10)
    # ======================================

    rr = risk["risk_reward"]

    if rr >= 3:
        score += 10
        reasons.append("Excellent Risk Reward")

    elif rr >= 2:
        score += 8
        reasons.append("Good Risk Reward")

    elif rr >= 1.5:
        score += 5
        reasons.append("Acceptable Risk Reward")

    # ======================================
    # MULTI TIMEFRAME (15)
    # ======================================

    if mtf:

        if mtf["confidence"] >= 90:
            score += 15
            reasons.append("Perfect MTF Alignment")

        elif mtf["confidence"] >= 60:
            score += 10
            reasons.append("Good MTF Alignment")

    # ======================================
    # SMART MONEY (15)
    # ======================================

    bos = detect_bos(df)
    choch = detect_choch(df)

    # BOS
    if bos["bos"]:
      score += 10
      reasons.extend(bos["reasons"])
    else:
      reasons.append("No BOS Confirmed")

    # CHOCH
    if choch["choch"]:
      score += 5
      reasons.extend(choch["reasons"])
    else:
      reasons.append("No CHOCH Detected")

    # ======================================
    # FINAL SCORE
    # ======================================

    score = max(0, min(score, 100))

    if score >= 95:
        grade = "A+"

    elif score >= 90:
        grade = "A"

    elif score >= 80:
        grade = "B+"

    elif score >= 70:
        grade = "B"

    elif score >= 60:
        grade = "C"

    else:
        grade = "D"

    return {
    "score": score,
    "grade": grade,
    "reasons": reasons,
    "bos": bos,
    "choch": choch
}