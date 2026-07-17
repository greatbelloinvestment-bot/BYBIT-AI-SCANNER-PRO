# ==========================================
# BYBIT AI SCANNER PRO V3
# MAIN SCANNER
# ==========================================
# ==========================================
# BYBIT AI SCANNER PRO V3.2
# MAIN SCANNER
# ==========================================

from config import SYMBOLS

from market import get_klines, prepare_dataframe
from indicators import calculate_indicators
from strategy import get_signal

from multi_timeframe import multi_timeframe_analysis
from risk import calculate_risk
from ai_engine import calculate_ai_score
from ranking import rank_trade
from report import print_trade

print("\n" + "=" * 80)
print("🏦 BYBIT AI SCANNER PRO V3")
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

        # Multi-Timeframe Analysis
        mtf = multi_timeframe_analysis(symbol)

        # Risk Analysis
        risk = calculate_risk(
          trade["entry"],
          trade["stop"],
          trade["tp1"]
        )

        # AI Score
        ai = calculate_ai_score(
          trade,
          mtf,
           risk
        )

        # Update trade confidence
        trade["confidence"] = ai["confidence"]
        trade["grade"] = ai["grade"]

        # Add risk values
        trade.update(risk)

        # Add timeframe data
        if mtf:
          trade.update(mtf)

        results.append({
            "symbol": symbol,
            **trade
        })

    except Exception as e:
        print(f"{symbol}: {e}")

# ==========================================
# SORT RESULTS
# ==========================================

results.sort(
    key=lambda x: x["confidence"],
    reverse=True
)

# ==========================================
# DISPLAY RESULTS
# ==========================================

for i, trade in enumerate(results, start=1):

    print("\n" + "=" * 80)

    print(f"#{i} {trade['symbol']}")

    print(f"Signal      : {trade['signal']}")
    print(f"Confidence  : {trade['confidence']}%")

    print(f"Entry       : {trade['entry']:.4f}")
    print(f"Stop Loss   : {trade['stop']:.4f}")

    print(f"TP1         : {trade['tp1']:.4f}")
    print(f"TP2         : {trade['tp2']:.4f}")
    print(f"TP3         : {trade['tp3']:.4f}")

    print("\nReasons:")

    for reason in trade["reasons"]:
        print(f"  ✓ {reason}")

print("\n" + "=" * 80)
print("✅ Scan Complete")
print("=" * 80)