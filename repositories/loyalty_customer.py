from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model.orm_model import LoyaltyCustomer
from schemas.loyality_customer import LoyaltyCustomerCreate


class LoyaltyCustomerRepo:

    async def create(self, session: AsyncSession, loyalty_customer: LoyaltyCustomerCreate):

        customer_record = LoyaltyCustomer(
            customer_id = loyalty_customer.customer_id,
            mobile_number=loyalty_customer.mobile_number,
            full_name=loyalty_customer.full_name,
            email=loyalty_customer.email,
            registered_at=loyalty_customer.registered_at
        )

        session.add(customer_record)
        await session.flush()
        return customer_record

    async def get_by_customer_id(self, session: AsyncSession, customer_id: int) -> LoyaltyCustomer:

        sql_statement = select(LoyaltyCustomer).where(LoyaltyCustomer.customer_id == customer_id)
        result = await session.execute(sql_statement)
        return result.scalar_one_or_none()


