from fastapi import APIRouter

from core.routers.endpoints.category_endpoints import router as category_router
from core.routers.endpoints.product_endpoints import router as product_router
from core.routers.endpoints.order_endpoints import router as order_router
from core.routers.endpoints.user_endpoints import router as user_router

router = APIRouter()
router.include_router(category_router)
router.include_router(order_router)
router.include_router(product_router)
router.include_router(user_router)
