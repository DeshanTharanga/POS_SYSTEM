from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class LoyaltyCustomerCreate(BaseModel):

    customer_id : int
    mobile_number : str
    full_name : str
    email : Optional[str]
    registered_at : datetime

    @field_validator("mobile_number")
    @classmethod
    def validate(cls, v, info):
        data = info.data

        if data["mobile_number"] != 'r"(07\d{8}|\+947\d{8})$':
            raise ValueError("Invalid mobile number")
        return v


class LoyaltyCustomerResponse(BaseModel):
    mobile_number: str
    full_name: str
    email: Optional[str]
    loyalty_points: float
    registered_at: datetime

    class Config:
        from_attributes = True
