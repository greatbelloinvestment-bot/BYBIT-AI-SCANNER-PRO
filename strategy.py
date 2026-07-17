# ==========================================
# BYBIT AI SCANNER PRO V3
# STRATEGY ENGINE
# ==========================================

def score_trend(last):
    score = 0
    reasons = []

    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        score += 30
        reasons.append("Strong Uptrend")

    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        score -= 30
        reasons.append("Strong Downtrend")

    return score, reasons


def score_rsi(last):
    score = 0
    reasons = []

    if 55 <= last["RSI"] <= 70:
        score += 15
        reasons.append("Healthy RSI")

    elif last["RSI"] > 75:
        score -= 10
        reasons.append("Overbought RSI")

    elif last["RSI"] < 30:
        score += 10
        reasons.append("Oversold RSI")

    return score, reasons

def score_macd(last):
    score = 0
    reasons = []

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 20
        reasons.append("MACD Bullish")

    elif last["MACD"] < last["MACD_SIGNAL"]:
        score -= 20
        reasons.append("MACD Bearish")

    return score, reasons


def score_adx(last):
    score = 0
    reasons = []

    if last["ADX"] >= 25:
        score += 15
        reasons.append("Strong Trend (ADX)")

    else:
        reasons.append("Weak Trend")

    return score, reasons


def score_volume(last):
    score = 0
    reasons = []

    if last["volume"] > last["VOL_MA"]:
        score += 10
        reasons.append("High Volume")

    else:
        reasons.append("Low Volume")

    return score, reasons


def score_bollinger(last):
    score = 0
    reasons = []

    if last["close"] < last["BB_LOWER"]:
        score += 10
        reasons.append("Near Lower Bollinger Band")

    elif last["close"] > last["BB_UPPER"]:
        score -= 10
        reasons.append("Near Upper Bollinger Band")

    return score, reasons

def calculate_trade_levels(last):
    entry = float(last["close"])
    atr = float(last["ATR"])

    stop = entry - (2 * atr)
    tp1 = entry + (2 * atr)
    tp2 = entry + (4 * atr)
    tp3 = entry + (6 * atr)

    return entry, stop, tp1, tp2, tp3


def get_signal(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # Trend
    s, r = score_trend(last)
    score += s
    reasons.extend(r)

    # RSI
    s, r = score_rsi(last)
    score += s
    reasons.extend(r)

    # MACD
    s, r = score_macd(last)
    score += s
    reasons.extend(r)

    # ADX
    s, r = score_adx(last)
    score += s
    reasons.extend(r)

    # Volume
    s, r = score_volume(last)
    score += s
    reasons.extend(r)

    # Bollinger
    s, r = score_bollinger(last)
    score += s
    reasons.extend(r)

    # Confidence
    confidence = max(0, min(100, score + 50))

    # Signal
    if confidence >= 70:
        signal = "BUY"
    elif confidence <= 30:
        signal = "SELL"
    else:
        signal = "NO TRADE"

    entry, stop, tp1, tp2, tp3 = calculate_trade_levels(last)

    return {
        "signal": signal,
        "confidence": confidence,
        "entry": entry,
        "stop": stop,
        "tp1": tp1,
        "tp2": tp2,
        "tp3": tp3,
        "reasons": reasons
    }