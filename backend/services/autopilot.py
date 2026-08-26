def execute_action(action, customer_id):
    if action == "BLOCK":
        return {
            "customer_id": customer_id,
            "action": "BLOCK",
            "message": "Transaction blocked due to high risk"
        }

    if action == "REVIEW":
        return {
            "customer_id": customer_id,
            "action": "REVIEW",
            "message": "Transaction sent for merchant review"
        }

    return {
        "customer_id": customer_id,
        "action": "ALLOW",
        "message": "Transaction allowed"
    }