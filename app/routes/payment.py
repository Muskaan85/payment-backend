from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Payment
from app.services.cashfree import create_cashfree_order

router = APIRouter(prefix="/payment", tags=["Payments"])

@router.post("/create-order")
def create_order(amount: float, email: str, db: Session = Depends(get_db)):
    try:
        cashfree_response = create_cashfree_order(amount, email)
    except Exception as e:
        return {"error": str(e)}

    payment = Payment(
        order_id=cashfree_response["order_id"],  # safe now
        amount=amount,
        currency="INR",
        status="PENDING",
        customer_email=email
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return {"order_id": payment.order_id, "status": payment.status}
