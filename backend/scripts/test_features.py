import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.fraud_features import build_features


df = pd.read_csv("data/transactions.csv")

features = build_features(df)

print(features.head(10))