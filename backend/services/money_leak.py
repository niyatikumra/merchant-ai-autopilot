def calculate_money_at_risk(transactions, risk_score):
    if risk_score < 70:
        return 0

    total_amount = sum(
        transaction["amount"]
        for transaction in transactions
    )

    return total_amount