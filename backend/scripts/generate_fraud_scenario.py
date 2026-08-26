import pandas as pd
from datetime import datetime, timedelta


def create_fraud_scenario():
    file_path = "data/transactions.csv"

    df = pd.read_csv(file_path)

    base_time = datetime.now()

    fraud_rows = [
        {
            "transaction_id": "FRAUD_001",
            "customer_id": "FRAUD_CUST_01",
            "product_id": "PROD_001",
            "amount": 4999,
            "payment_method": "UPI",
            "coupon": "CLEAR500",
            "device_id": "SHARED_DEVICE_01",
            "ip_address": "10.10.10.50",
            "shipping_address": "ADDR_FRAUD_01",
            "timestamp": (base_time - timedelta(minutes=5)).isoformat(),
            "payment_status": "success"
        },
        {
            "transaction_id": "FRAUD_002",
            "customer_id": "FRAUD_CUST_02",
            "product_id": "PROD_001",
            "amount": 4999,
            "payment_method": "UPI",
            "coupon": "CLEAR500",
            "device_id": "SHARED_DEVICE_01",
            "ip_address": "10.10.10.50",
            "shipping_address": "ADDR_FRAUD_02",
            "timestamp": (base_time - timedelta(minutes=4)).isoformat(),
            "payment_status": "success"
        },
        {
            "transaction_id": "FRAUD_003",
            "customer_id": "FRAUD_CUST_03",
            "product_id": "PROD_001",
            "amount": 4999,
            "payment_method": "UPI",
            "coupon": "CLEAR500",
            "device_id": "SHARED_DEVICE_01",
            "ip_address": "10.10.10.50",
            "shipping_address": "ADDR_FRAUD_03",
            "timestamp": (base_time - timedelta(minutes=3)).isoformat(),
            "payment_status": "success"
        }
    ]

    fraud_df = pd.DataFrame(fraud_rows)

    df = pd.concat([df, fraud_df], ignore_index=True)

    df.to_csv(file_path, index=False)

    print("Added 3 controlled fraud-ring transactions.")


if __name__ == "__main__":
    create_fraud_scenario()