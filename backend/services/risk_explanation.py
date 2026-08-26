def explain_risk(anomaly, graph_weight):
    reasons = []

    if anomaly == -1:
        reasons.append("Unusual transaction behavior detected")

    if graph_weight >= 1:
        reasons.append("Customer shares a device with other customers")

    if graph_weight >= 2:
        reasons.append("Customer shares a network/IP with other customers")

    if not reasons:
        reasons.append("No major risk signals detected")

    return reasons