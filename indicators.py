# ==========================================
# BYBIT AI SCANNER PRO V3
# INDICATOR ENGINE
# ==========================================

import ta

def calculate_indicators(df):

    if df.empty:
        return df

    # ==========================
    # EMA
    # ==========================

    df["EMA20"] = ta.trend.ema_indicator(
        df["close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        df["close"],
        window=50
    )

    df["EMA200"] = ta.trend.ema_indicator(
        df["close"],
        window=200
    )

    # ==========================
    # RSI
    # ==========================

    df["RSI"] = ta.momentum.rsi(
        df["close"],
        window=14
    )

    # ==========================
    # MACD
    # ==========================

    macd = ta.trend.MACD(df["close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()
    df["MACD_HIST"] = macd.macd_diff()

    # ==========================
    # ATR
    # ==========================

    atr = ta.volatility.AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    df["ATR"] = atr.average_true_range()

    # ==========================
    # ADX
    # ==========================

    adx = ta.trend.ADXIndicator(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    df["ADX"] = adx.adx()

    # ==========================
    # Bollinger Bands
    # ==========================

    bb = ta.volatility.BollingerBands(
        close=df["close"],
        window=20,
        window_dev=2
    )

    df["BB_UPPER"] = bb.bollinger_hband()
    df["BB_MIDDLE"] = bb.bollinger_mavg()
    df["BB_LOWER"] = bb.bollinger_lband()

    # ==========================
    # Volume Average
    # ==========================

    df["VOL_MA"] = df["volume"].rolling(20).mean()

    return df
