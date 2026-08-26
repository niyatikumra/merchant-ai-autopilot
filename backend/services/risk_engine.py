def calculate_risk_score(anomaly, graph_weight):
    score = 0

    # ML anomaly signal
    if anomaly == -1:
        score += 50

    # Graph relationship signal
    if graph_weight >= 1:
        score += 20

    if graph_weight >= 2:
        score += 20

    return min(score, 100)