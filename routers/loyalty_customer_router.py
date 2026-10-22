from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_session
from schemas.loyality_customer import LoyaltyCustomerResponse, LoyaltyCustomerCreate
from services.loyalti_customer_service import LoyaltyCustomerService

router = APIRouter(prefix="/customers", tags=["Customers"])

customer_service = LoyaltyCustomerService()

@router.post("/", response_model=LoyaltyCustomerResponse, status_code=201)
async def create_customer(customer: LoyaltyCustomerCreate,  session: AsyncSession = Depends(get_session)):
    return await customer_service.create(session,customer)