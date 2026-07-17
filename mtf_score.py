# ==========================================
# BYBIT AI SCANNER PRO V4
# MULTI-TIMEFRAME SCORING ENGINE
# ==========================================

def calculate_mtf_score(mtf):

    score = 0
    reasons = []

    if mtf is None:
        return {
            "score": 0,
            "reasons": ["No MTF Data"]
        }

    confidence = mtf.get("confidence", 0)

    if confidence >= 100:
        score = 15
        reasons.append("Perfect Multi-Timeframe Alignment")

    elif confidence >= 65:
        score = 10
        reasons.append("Strong Multi-Timeframe Alignment")

    elif confidence >= 30:
        score = 5
        reasons.append("Partial Multi-Timeframe Alignment")

    else:
        score = 0
        reasons.append("Weak Multi-Timeframe Alignment")

    return {
        "score": score,
        "reasons": reasons
    }