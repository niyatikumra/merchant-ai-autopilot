import pandas as pd


def build_features(df):
    features = pd.DataFrame()

    features["customer_id"] = df["customer_id"]

    features["transaction_count"] = (
        df.groupby("customer_id")["transaction_id"]
        .transform("count")
    )

    features["coupon_usage_count"] = (
        df.groupby(["customer_id", "coupon"])["coupon"]
        .transform("count")
    )

    features["device_customer_count"] = (
        df.groupby("device_id")["customer_id"]
        .transform("nunique")
    )

    features["ip_customer_count"] = (
        df.groupby("ip_address")["customer_id"]
        .transform("nunique")
    )

    features["address_customer_count"] = (
        df.groupby("shipping_address")["customer_id"]
        .transform("nunique")
    )

    features["average_transaction_amount"] = (
        df.groupby("customer_id")["amount"]
        .transform("mean")
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    features["recent_transaction_count"] = (
    df.groupby("customer_id")["timestamp"]
    .transform(
        lambda x: x.apply(
            lambda t: ((x >= t - pd.Timedelta(hours=24)) & (x <= t)).sum()
        )
    )
)
    features["high_value_transaction"] = (
    df["amount"] > df["amount"].quantile(0.90)
).astype(int)
    features["coupon_used"] = (
    df["coupon"] != "NONE"
).astype(int)
    features["shared_device"] = (
    df.groupby("device_id")["customer_id"]
    .transform("nunique") > 1
).astype(int)

    features["shared_ip"] = (
    df.groupby("ip_address")["customer_id"]
    .transform("nunique") > 1
).astype(int)
    

    return features