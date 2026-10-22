from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model.orm_model import Product
from schemas.category import CategoryCreate
from schemas.product import ProductCreate


class ProductRepository:

    async def create(self, session: AsyncSession, product : ProductCreate ,category : CategoryCreate):

        product_record = Product(
            product_code = product.product_code,
            product_name = product.product_name,
            unit_price = product.unit_price,
            available_quantity = product.available_quantity,
            active = product.active,
            category_id = category.category_id,
        )

        session.add(product_record)
        await session.flush()
        return product_record

    async def get_by_product_code(self, session: AsyncSession,product_code: str):

        sql_statement = select(Product).where(Product.product_code == product_code)
        result = await session.execute(sql_statement)
        return result.scalar_one_or_none()

