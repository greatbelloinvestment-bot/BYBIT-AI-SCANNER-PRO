# ==========================================
# BYBIT AI SCANNER PRO V3.1
# REPORT ENGINE
# ==========================================

def print_trade(rank, trade):

    print("\n" + "=" * 80)

    print(f"#{rank} {trade['symbol']}")

    if "stars" in trade:
        print(f"\n{trade['stars']}")

    if "grade" in trade:
        print(f"Grade       : {trade['grade']}")

    if "quality" in trade:
        print(f"Quality     : {trade['quality']}")

    print(f"\nSignal      : {trade['signal']}")
    print(f"Confidence  : {trade['confidence']}%")

    if "15m" in trade:
        print(f"\n15m Trend   : {trade['15m']}")

    if "1h" in trade:
        print(f"1H Trend    : {trade['1h']}")

    if "4h" in trade:
        print(f"4H Trend    : {trade['4h']}")

    print(f"\nEntry       : {trade['entry']:.4f}")
    print(f"Stop Loss   : {trade['stop']:.4f}")

    print(f"\nTP1         : {trade['tp1']:.4f}")
    print(f"TP2         : {trade['tp2']:.4f}")
    print(f"TP3         : {trade['tp3']:.4f}")

    print("\nReasons:")

    for reason in trade["reasons"]:
        print(f" ✓ {reason}")