from fastapi import APIRouter
from models.transaction import Transaction
from services.transaction_service import save_transaction, get_all_transactions
from datetime import datetime
router = APIRouter()


@router.post("/transactions")
def create_transaction(transaction: Transaction):
    transaction.timestamp = datetime.now().isoformat()
    saved_transaction = save_transaction(transaction)

    return {
        "message": "Transaction saved",
        "transaction": saved_transaction
    }


@router.get("/transactions")
def get_transactions():
    return {
        "count": len(get_all_transactions()),
        "transactions": get_all_transactions()
    }