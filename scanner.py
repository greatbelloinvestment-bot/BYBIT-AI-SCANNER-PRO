# ==========================================
# BYBIT AI SCANNER PRO V3
# MAIN SCANNER
# ==========================================

from config import SYMBOLS
from market import get_klines, prepare_dataframe
from indicators import calculate_indicators
from strategy import get_signal

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