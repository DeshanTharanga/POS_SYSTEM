from datetime import datetime

from pydantic import BaseModel


class OderCreate(BaseModel):

    order_id: int
    customer_id: int
    order_date_time: datetime
    order_status: str
    total_amount: int

class OderResponse(BaseModel):
    customer_id: int
    order_date_time: datetime
    order_status: str
    total_amount: int
    loyalty_points: int


