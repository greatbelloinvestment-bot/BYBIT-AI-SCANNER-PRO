# ==========================================
# BYBIT AI SCANNER PRO V4
# RISK SCORING ENGINE
# ==========================================

def calculate_risk_score(risk):

    score = 0
    reasons = []

    rr = risk.get("risk_reward", 0)

    # ==========================
    # Risk / Reward Analysis
    # ==========================

    if rr >= 4:
        score = 10
        reasons.append("Excellent Risk/Reward")

    elif rr >= 3:
        score = 8
        reasons.append("Very Good Risk/Reward")

    elif rr >= 2:
        score = 6
        reasons.append("Good Risk/Reward")

    elif rr >= 1.5:
        score = 4
        reasons.append("Acceptable Risk/Reward")

    else:
        score = 1
        reasons.append("Poor Risk/Reward")

    return {
        "score": score,
        "reasons": reasons
    }