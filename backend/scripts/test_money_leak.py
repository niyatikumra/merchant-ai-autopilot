import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.money_leak import calculate_money_at_risk


fraud_transactions = [
    {"amount": 4999},
    {"amount": 4999},
    {"amount": 4999}
]

risk_score = 90

money_at_risk = calculate_money_at_risk(
    fraud_transactions,
    risk_score
)

print("Risk Score:", risk_score)
print("Money At Risk: ₹", money_at_risk)