# ==========================================
# BYBIT AI SCANNER PRO V3.1
# RISK ENGINE
# ==========================================

def calculate_risk(entry, stop, tp1, account_balance=10000, risk_percent=1):

    risk_amount = account_balance * (risk_percent / 100)

    stop_distance = abs(entry - stop)

    if stop_distance == 0:
        position_size = 0
    else:
        position_size = risk_amount / stop_distance

    reward = abs(tp1 - entry)

    if stop_distance == 0:
        rr = 0
    else:
        rr = reward / stop_distance

    return {
        "risk_amount": round(risk_amount, 2),
        "position_size": round(position_size, 4),
        "risk_reward": round(rr, 2)
    }