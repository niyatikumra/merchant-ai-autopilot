from sklearn.ensemble import IsolationForest


def train_anomaly_model(features):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(features)

    return model
def predict_anomalies(model, features):
    predictions = model.predict(features)

    return predictions