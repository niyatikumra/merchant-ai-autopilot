DEFAULT_POLICY = {
    "review_threshold": 40,
    "block_threshold": 70
}


def decide_action(risk_score, policy=DEFAULT_POLICY):
    if risk_score >= policy["block_threshold"]:
        return "BLOCK"

    if risk_score >= policy["review_threshold"]:
        return "REVIEW"

    return "ALLOW"