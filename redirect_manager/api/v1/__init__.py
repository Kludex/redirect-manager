from fastapi import APIRouter

from redirect_manager.api.v1.redirect import router as redirect_router

router = APIRouter(prefix="/v1")
router.include_router(redirect_router)
