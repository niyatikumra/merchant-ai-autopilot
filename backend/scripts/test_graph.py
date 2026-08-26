import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.fraud_graph import build_fraud_graph


df = pd.read_csv("data/transactions.csv")

graph = build_fraud_graph(df)

print("Number of customers:", graph.number_of_nodes())
print("Number of relationships:", graph.number_of_edges())

print("\nFraud customer connections:")

for customer in [
    "FRAUD_CUST_01",
    "FRAUD_CUST_02",
    "FRAUD_CUST_03"
]:
    print(customer, "->", list(graph.neighbors(customer)))
    print("\nFraud ring edge details:")

edge_data = graph.get_edge_data(
    "FRAUD_CUST_01",
    "FRAUD_CUST_02"
)

print(edge_data)