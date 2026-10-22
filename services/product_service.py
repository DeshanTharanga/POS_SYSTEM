from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from repositories.product import ProductRepository
from schemas.category import CategoryCreate
from schemas.product import ProductResponse, ProductCreate


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    async def create_product(self, session: AsyncSession, product: ProductCreate,category : CategoryCreate) -> ProductResponse:
        try:
            existing = await self.repository.get_by_product_code(session, product.product_code)

            if existing:
                raise HTTPException(status_code=409,
                                    detail=f"product with product number {product.product_code} already exists")

            db_product = await self.repository.create(session, product, category)
            await session.commit()
            await session.refresh(db_product)

            return ProductResponse.model_validate(db_product)

        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")










