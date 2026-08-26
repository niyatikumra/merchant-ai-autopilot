import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.risk_engine import calculate_risk_score

risk = calculate_risk_score(
    anomaly=-1,
    graph_weight=2
)

print("Risk Score:", risk)