# ==========================================
# BYBIT AI SCANNER PRO V4
# VOLUME SCORING ENGINE
# ==========================================

def calculate_volume_score(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    current_volume = last["volume"]
    average_volume = last["VOL_MA"]

    # ==========================
    # Volume Analysis
    # ==========================

    if current_volume >= average_volume * 2:
        score = 15
        reasons.append("Exceptional Volume")

    elif current_volume >= average_volume * 1.5:
        score = 12
        reasons.append("Very High Volume")

    elif current_volume >= average_volume:
        score = 8
        reasons.append("Above Average Volume")

    else:
        score = 3
        reasons.append("Low Volume")

    return {
        "score": score,
        "reasons": reasons
    }