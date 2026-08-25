from pydantic import BaseModel


class Transaction(BaseModel):
    customer_id: str
    product_id: str
    amount: float
    payment_method: str
    coupon: str
    device_id: str
    ip_address: str
    shipping_address: str
    timestamp: str