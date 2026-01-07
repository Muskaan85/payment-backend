from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(String(50), unique=True, index=True)
    amount = Column(Float)
    currency = Column(String(10))
    status = Column(String(20))
    customer_email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
