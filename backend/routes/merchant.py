from fastapi import APIRouter
import pandas as pd

from services.fraud_features import build_features
from services.anomaly_detector import (
    train_anomaly_model,
    predict_anomalies
)
from services.fraud_graph import build_fraud_graph
from services.risk_engine import calculate_risk_score


router = APIRouter()


@router.get("/merchant/summary")
def merchant_summary():

    df = pd.read_csv("../data/transactions.csv")

    features = build_features(df)

    model_features = features.drop(
        columns=["customer_id"]
    )

    model = train_anomaly_model(
        model_features
    )

    predictions = predict_anomalies(
        model,
        model_features
    )

    features["anomaly"] = predictions

    graph = build_fraud_graph(df)

    suspicious_customers = 0
    total_risk = 0
    blocked_transactions = 0
    risky_scores = []
    money_at_risk = 0
    for customer in features["customer_id"].unique():

        index = features[
            features["customer_id"] == customer
        ].index[0]

        anomaly = features.loc[
            index,
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

        if risk >= 70:
          risky_scores.append(risk)

        customer_amount = df[
        df["customer_id"] == customer
    ]["amount"].sum()

        money_at_risk += int (customer_amount)
    if risk >= 70:
            suspicious_customers += 1
            blocked_transactions += 1

    average_risk = (
    sum(risky_scores) / len(risky_scores)
    if risky_scores
    else 0
)

    return {
        "suspicious_customers": suspicious_customers,
        "money_at_risk": money_at_risk,
        "blocked_transactions": blocked_transactions,
        "average_risk_score": round(
            average_risk,
            2
        )
    }