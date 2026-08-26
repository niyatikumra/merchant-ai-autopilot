import sys
import os
import pandas as pd

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.fraud_features import build_features
from services.anomaly_detector import (
    train_anomaly_model,
    predict_anomalies
)
from services.fraud_graph import build_fraud_graph
from services.risk_engine import calculate_risk_score
from services.money_leak import calculate_money_at_risk
from services.policy_engine import decide_action
from services.autopilot import execute_action
from services.risk_explanation import explain_risk


df = pd.read_csv("data/transactions.csv")

features = build_features(df)

model_features = features.drop(columns=["customer_id"])

model = train_anomaly_model(model_features)

predictions = predict_anomalies(
    model,
    model_features
)

features["anomaly"] = predictions

graph = build_fraud_graph(df)


print("\n===== MERCHANT AI AUTOPILOT =====\n")


for customer in [
    "FRAUD_CUST_01",
    "FRAUD_CUST_02",
    "FRAUD_CUST_03"
]:

    customer_index = features[
        features["customer_id"] == customer
    ].index[0]

    anomaly = features.loc[
        customer_index,
        "anomaly"
    ]

    neighbors = list(
        graph.neighbors(customer)
    )

    max_weight = 0

    for neighbor in neighbors:

        edge = graph.get_edge_data(
            customer,
            neighbor
        )

        max_weight = max(
            max_weight,
            edge.get("weight", 0)
        )

    risk = calculate_risk_score(
        anomaly,
        max_weight
    )

    risk_reasons = explain_risk(
        anomaly,
        max_weight
    )

    customer_transactions = df[
        df["customer_id"] == customer
    ]

    transactions = customer_transactions[
        ["amount"]
    ].to_dict("records")

    money_at_risk = calculate_money_at_risk(
        transactions,
        risk
    )

    action = decide_action(risk)

    result = execute_action(
        action,
        customer
    )

    print("Customer:", customer)
    print("Risk Score:", risk)

    print("Risk Reasons:")
    for reason in risk_reasons:
        print(" -", reason)

    print("Money At Risk: ₹", money_at_risk)
    print("Action:", result["action"])
    print("Message:", result["message"])
    print("Connections:", len(neighbors))
    print("-" * 50)