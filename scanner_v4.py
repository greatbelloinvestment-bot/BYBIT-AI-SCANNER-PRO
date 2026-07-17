# ==========================================
# BYBIT AI SCANNER PRO V4
# INSTITUTIONAL SCANNER
# ==========================================

from config import SYMBOLS

from market import get_klines, prepare_dataframe
from indicators import calculate_indicators

from strategy import get_signal
from risk import calculate_risk

from multi_timeframe import multi_timeframe_analysis

from trend_score import calculate_trend_score
from momentum_score import calculate_momentum_score
from volume_score import calculate_volume_score
from risk_score import calculate_risk_score
from mtf_score import calculate_mtf_score
from smart_money_score import calculate_smart_money_score

from scoring import calculate_score

from ranking import rank_trade
from report import print_trade

print("\n" + "=" * 80)
print("🏦 BYBIT AI SCANNER PRO V4")
print("=" * 80)

results = []

for symbol in SYMBOLS:

    try:

        response = get_klines(symbol)

        df = prepare_dataframe(response)

        if df.empty:
            print(f"{symbol}: No market data")
            continue

        df = calculate_indicators(df)

        trade = get_signal(df)

        last = df.iloc[-1]

        # ==========================================
# TREND SCORE
# ==========================================

trend = calculate_trend_score(df)

trend_score = trend["score"]

reasons = []
reasons.extend(trend["reasons"])

# ==========================================
# MOMENTUM SCORE
# ==========================================

momentum = calculate_momentum_score(df)

momentum_score = momentum["score"]

reasons.extend(momentum["reasons"])

# ==========================================
# VOLUME SCORE
# ==========================================

volume = calculate_volume_score(df)

volume_score = volume["score"]

reasons.extend(volume["reasons"])

# ==========================================
# RISK SCORE
# ==========================================

risk = calculate_risk(
    trade["entry"],
    trade["stop"],
    trade["tp1"]
)

risk_engine = calculate_risk_score(risk)

risk_score = risk_engine["score"]

reasons.extend(risk_engine["reasons"])

# ==========================================
# MULTI-TIMEFRAME SCORE
# ==========================================

mtf = multi_timeframe_analysis(symbol)

mtf_engine = calculate_mtf_score(mtf)

mtf_score = mtf_engine["score"]

reasons.extend(mtf_engine["reasons"])

# ==========================================
# SMART MONEY SCORE
# ==========================================

smart_money = calculate_smart_money_score()

smart_money_score = smart_money["score"]

reasons.extend(smart_money["reasons"])