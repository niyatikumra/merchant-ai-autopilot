import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.fraud_features import build_features
from services.anomaly_detector import train_anomaly_model, predict_anomalies


df = pd.read_csv("data/transactions.csv")

features = build_features(df)

model_features = features.drop(columns=["customer_id"])

model = train_anomaly_model(model_features)

predictions = predict_anomalies(model, model_features)

features["anomaly"] = predictions

print(features[["customer_id", "anomaly"]].tail(10))