# ==========================================
# BYBIT AI SCANNER PRO V3.1
# RANKING ENGINE
# ==========================================

def rank_trade(confidence):

    if confidence >= 95:
        return {
            "grade": "A+",
            "stars": "★★★★★",
            "quality": "Institutional"
        }

    elif confidence >= 90:
        return {
            "grade": "A",
            "stars": "★★★★★",
            "quality": "Excellent"
        }

    elif confidence >= 80:
        return {
            "grade": "B+",
            "stars": "★★★★☆",
            "quality": "Very Good"
        }

    elif confidence >= 70:
        return {
            "grade": "B",
            "stars": "★★★★☆",
            "quality": "Good"
        }

    elif confidence >= 60:
        return {
            "grade": "C",
            "stars": "★★★☆☆",
            "quality": "Average"
        }

    else:
        return {
            "grade": "D",
            "stars": "★☆☆☆☆",
            "quality": "Weak"
        }