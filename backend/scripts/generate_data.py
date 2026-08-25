import csv
import random
from datetime import datetime, timedelta

random.seed(42)

customers = [f"CUST_{i:03d}" for i in range(1, 101)]
products = ["PROD_001", "PROD_002", "PROD_003", "PROD_004", "PROD_005"]

payment_methods = ["UPI", "CARD", "NETBANKING"]
coupons = ["NONE", "SAVE50", "SAVE100", "CLEAR500"]

rows = []

start_time = datetime.now() - timedelta(days=30)

for i in range(500):
    customer_id = random.choice(customers)

    row = {
        "transaction_id": f"TXN_{i+1:04d}",
        "customer_id": customer_id,
        "product_id": random.choice(products),
        "amount": random.choice([499, 799, 999, 1499, 1999, 2499]),
        "payment_method": random.choice(payment_methods),
        "coupon": random.choice(coupons),
        "device_id": f"DEV_{random.randint(1, 120):03d}",
        "ip_address": f"192.168.1.{random.randint(1, 120)}",
        "shipping_address": f"ADDR_{random.randint(1, 120):03d}",
        "timestamp": (
            start_time + timedelta(
                minutes=random.randint(0, 30 * 24 * 60)
            )
        ).isoformat(),
        "payment_status": random.choice(["success", "success", "success", "failed"])
    }

    rows.append(row)


with open("data/transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Generated 500 synthetic transactions.")