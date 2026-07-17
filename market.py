# ==========================================
# BYBIT AI SCANNER PRO V3.1
# MARKET DATA ENGINE
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

def get_klines(symbol, interval=None):

    # Use default interval from config if none is supplied
    if interval is None:
        interval = INTERVAL

    response = session.get_kline(
        category="linear",
        symbol=symbol,
        interval=interval,
        limit=LIMIT
    )

    return response


# ==========================================
# PREPARE DATAFRAME
# ==========================================

def prepare_dataframe(response):

    try:
        candles = response["result"]["list"]
    except (KeyError, TypeError):
        return pd.DataFrame()

    if not candles:
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

    # Convert numeric columns
    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "turnover"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"].astype("int64"),
        unit="ms"
    )

    # Sort oldest → newest
    df = df.sort_values("timestamp").reset_index(drop=True)

    return df