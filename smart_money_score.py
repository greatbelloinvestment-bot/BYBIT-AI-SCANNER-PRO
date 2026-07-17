# ==========================================
# BYBIT AI SCANNER PRO V4
# SMART MONEY SCORING ENGINE
# ==========================================

def calculate_smart_money_score(sm_data=None):

    score = 0
    reasons = []

    if sm_data is None:
        return {
            "score": 0,
            "reasons": ["Smart Money Not Available"]
        }

    if sm_data.get("bos", False):
        score += 5
        reasons.append("Break of Structure")

    if sm_data.get("choch", False):
        score += 3
        reasons.append("Change of Character")

    if sm_data.get("order_block", False):
        score += 3
        reasons.append("Order Block")

    if sm_data.get("fvg", False):
        score += 2
        reasons.append("Fair Value Gap")

    if sm_data.get("liquidity_sweep", False):
        score += 2
        reasons.append("Liquidity Sweep")

    score = min(score, 15)

    return {
        "score": score,
        "reasons": reasons
    }