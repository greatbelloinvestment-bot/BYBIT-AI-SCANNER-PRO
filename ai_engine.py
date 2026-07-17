# ==========================================
# BYBIT AI SCANNER PRO V3.2
# AI CONFIDENCE ENGINE
# ==========================================

def calculate_ai_score(strategy, mtf, risk):

    score = 0

    # =====================================
    # Strategy Score (0-40)
    # =====================================

    strategy_conf = strategy.get("confidence", 0)
    score += strategy_conf * 0.40

    # =====================================
    # Multi-Timeframe Score (0-25)
    # =====================================

    if mtf:
        score += mtf.get("confidence", 0) * 0.25

    # =====================================
    # Risk/Reward Score (0-15)
    # =====================================

    rr = risk.get("risk_reward", 0)

    if rr >= 3:
        score += 15
    elif rr >= 2:
        score += 10
    elif rr >= 1.5:
        score += 5

    # =====================================
    # Volume Bonus (0-10)
    # =====================================

    reasons = strategy.get("reasons", [])

    if "High Volume" in reasons:
        score += 10
    elif "Low Volume" in reasons:
        score += 3

    # =====================================
    # Trend Bonus (0-10)
    # =====================================

    if "Strong Uptrend" in reasons:
        score += 10
    elif "Strong Downtrend" in reasons:
        score += 5

    # =====================================
    # Final Score
    # =====================================

    score = round(score)

    score = max(0, min(score, 100))

    # =====================================
    # Grade
    # =====================================

    if score >= 95:
        grade = "A+"

    elif score >= 90:
        grade = "A"

    elif score >= 80:
        grade = "B+"

    elif score >= 70:
        grade = "B"

    elif score >= 60:
        grade = "C+"

    elif score >= 50:
        grade = "C"

    else:
        grade = "D"

    return {
        "confidence": score,
        "grade": grade
    }