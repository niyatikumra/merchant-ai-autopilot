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


df = pd.read_csv("data/transactions.csv")

# Build features
features = build_features(df)

# ML model
model_features = features.drop(columns=["customer_id"])

model = train_anomaly_model(model_features)

predictions = predict_anomalies(
    model,
    model_features
)

features["anomaly"] = predictions

# Fraud graph
graph = build_fraud_graph(df)

print("\nFraud Risk Results:\n")

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

    neighbors = list(graph.neighbors(customer))

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

    print(
        customer,
        "| Anomaly:", anomaly,
        "| Graph Weight:", max_weight,
        "| Risk:", risk
    )