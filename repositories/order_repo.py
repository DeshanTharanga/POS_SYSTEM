from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model.orm_model import Oder
from schemas.order import OderCreate, OderResponse


class OrderRepository:

    async def create(self, session: AsyncSession, order: OderCreate):
        order_record = Oder(
            id= order.order_id,
            customer_id=order.customer_id,
            order_date_time=order.order_date_time,
            order_status=order.order_status,
            total_amount=order.total_amount,
        )

        session.add(order_record)
        await session.flush()
        return order_record

    async def get(self, session: AsyncSession, order_id: int) -> OderResponse:
        sql_statement = select(Oder).where(Oder.id == order_id)
        result = await session.execute(sql_statement)
        return result.scalar_one_or_none()