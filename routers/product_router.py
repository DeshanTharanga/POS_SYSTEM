from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_session
from schemas.category import CategoryCreate
from schemas.product import ProductResponse, ProductCreate
from services.product_service import ProductService


router = APIRouter(prefix="/products", tags=["Products"])

product_service = ProductService()

@router.post("/product", status_code=201, response_model=ProductResponse)
async def create_product(product: ProductCreate,category:CategoryCreate, session: AsyncSession = Depends(get_session)) -> ProductResponse:
    return await product_service.create_product(session, product, category)