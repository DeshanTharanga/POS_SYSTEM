from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from repositories.loyalty_customer import LoyaltyCustomerRepo
from schemas.loyality_customer import LoyaltyCustomerCreate, LoyaltyCustomerResponse


class LoyaltyCustomerService:

    def __init__(self):
        self.repository = LoyaltyCustomerRepo()

    async def create(self, session: AsyncSession, customer: LoyaltyCustomerCreate) -> LoyaltyCustomerResponse:
        try:
            existing = await self.repository.get_by_customer_id(session, customer.customer_id)

            if existing:
                raise HTTPException(status_code=409,
                            detail=f"customer with customer id {customer.customer_id} already exists")

            db_customer = await self.repository.create(session,customer)
            await session.commit()
            await session.refresh(db_customer)

            return LoyaltyCustomerResponse.model_validate(db_customer)

        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to create customer: {str(e)}")