# ==========================================
# BYBIT AI SCANNER PRO V3.1
# MULTI-TIMEFRAME ENGINE
# ==========================================

from market import get_klines, prepare_dataframe
from indicators import calculate_indicators


def analyze_timeframe(symbol, interval):

    response = get_klines(symbol, interval)

    df = prepare_dataframe(response)

    if df.empty:
        return None

    df = calculate_indicators(df)

    last = df.iloc[-1]

    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        trend = "BULLISH"

    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        trend = "BEARISH"

    else:
        trend = "SIDEWAYS"

    return {
        "trend": trend,
        "price": last["close"]
    }


def multi_timeframe_analysis(symbol):

    tf15 = analyze_timeframe(symbol, 15)

    tf1h = analyze_timeframe(symbol, 60)

    tf4h = analyze_timeframe(symbol, 240)

    if tf15 is None or tf1h is None or tf4h is None:
        return None

    confidence = 0

    if tf15["trend"] == tf1h["trend"]:
        confidence += 30

    if tf1h["trend"] == tf4h["trend"]:
        confidence += 35

    if tf15["trend"] == tf4h["trend"]:
        confidence += 35

    return {

        "15m": tf15["trend"],

        "1h": tf1h["trend"],

        "4h": tf4h["trend"],

        "confidence": confidence

    }