import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.policy_engine import decide_action


default_policy = {
    "review_threshold": 40,
    "block_threshold": 70
}

strict_policy = {
    "review_threshold": 30,
    "block_threshold": 60
}

print("Default policy:")
print("Risk 65 →", decide_action(65, default_policy))

print("\nStrict policy:")
print("Risk 65 →", decide_action(65, strict_policy))