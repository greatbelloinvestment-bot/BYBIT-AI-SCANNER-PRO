# ==========================================
# BYBIT AI SCANNER PRO V3
# MARKET DATA
# ==========================================

from pybit.unified_trading import HTTP
import pandas as pd

from config import (
    API_KEY,
    API_SECRET,
    INTERVAL,
    LIMIT
)

# ==========================================
# CREATE SESSION
# ==========================================

session = HTTP(
    testnet=False,
    api_key=API_KEY,
    api_secret=API_SECRET
)

# ==========================================
# GET KLINES
# ==========================================

def get_klines(symbol):

    response = session.get_kline(
        category="linear",
        symbol=symbol,
        interval=INTERVAL,
        limit=LIMIT
    )

    return response

# ==========================================
# PREPARE DATAFRAME
# ==========================================

def prepare_dataframe(response):

    candles = response["result"]["list"]

    if len(candles) == 0:
        return pd.DataFrame()

    df = pd.DataFrame(
        candles,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "turnover"
        ]
    )

    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "turnover"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    df["timestamp"] = pd.to_datetime(
        df["timestamp"].astype(int),
        unit="ms"
    )

    # Oldest candle first
    df = df.iloc[::-1].reset_index(drop=True)

    return df