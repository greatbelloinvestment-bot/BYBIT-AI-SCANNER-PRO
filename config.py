"""
=========================================================
BYBIT AI SCANNER PRO V3
Version : 3.0.0
Author  : GREAT BELLO INVESTMENT
=========================================================
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ==========================================
# BYBIT API
# ==========================================

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

# ==========================================
# TELEGRAM
# ==========================================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ==========================================
# MARKET SETTINGS
# ==========================================

INTERVAL = 60
LIMIT = 300

# ==========================================
# SYMBOLS
# ==========================================

SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "XLMUSDT",
    "DOGEUSDT",
    "ADAUSDT",
    "LINKUSDT",
    "AVAXUSDT",
    "SUIUSDT",
    "TRXUSDT",
    "TONUSDT",
    "LTCUSDT",
    "BCHUSDT",
    "DOTUSDT",
    "APTUSDT",
    "ARBUSDT",
    "OPUSDT",
    "NEARUSDT",
    "ATOMUSDT",
    "FILUSDT",
    "INJUSDT",
    "SEIUSDT",
    "1000PEPEUSDT",
    "UNIUSDT",
    "HBARUSDT",
    "AAVEUSDT",
]

# ==========================================
# RISK SETTINGS
# ==========================================

RISK_PERCENT = 1.0
MIN_CONFIDENCE = 70
MIN_RISK_REWARD = 2.0