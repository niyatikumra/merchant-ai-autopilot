import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.risk_explanation import explain_risk


reasons = explain_risk(
    anomaly=-1,
    graph_weight=2
)

print("Risk Reasons:")

for reason in reasons:
    print("-", reason)