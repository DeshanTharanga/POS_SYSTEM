from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.database import init_db, close_db
from routers.product_router import router as  product_router
from routers.loyalty_customer_router import router as customer_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_db()
    yield
    await close_db()

app = FastAPI(
    title="POS",
    lifespan=lifespan
)


app.include_router(product_router)
app.include_router(customer_router)