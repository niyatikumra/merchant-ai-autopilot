import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.autopilot import execute_action


for action in ["ALLOW", "REVIEW", "BLOCK"]:
    result = execute_action(
        action,
        "FRAUD_CUST_01"
    )

    print(result)