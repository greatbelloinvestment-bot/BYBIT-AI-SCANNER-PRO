# ==========================================
# BYBIT AI SCANNER PRO V4
# INSTITUTIONAL SCORING ENGINE
# ==========================================

def calculate_score(
    trend_score,
    momentum_score,
    volume_score,
    risk_score,
    mtf_score,
    smart_money_score
):

    total = (
        trend_score +
        momentum_score +
        volume_score +
        risk_score +
        mtf_score +
        smart_money_score
    )

    total = max(0, min(100, total))

    if total >= 95:
        grade = "A+"
    elif total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B+"
    elif total >= 70:
        grade = "B"
    elif total >= 60:
        grade = "C+"
    elif total >= 50:
        grade = "C"
    else:
        grade = "D"

    return {
        "score": total,
        "grade": grade
    }