from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from redirect_manager.core.database import get_session
from redirect_manager.models.redirect import Redirect, RedirectCreate

router = APIRouter(prefix="/redirect", tags=["Redirect"])


@router.get("/")
async def get_all_redirects(
    session: AsyncSession = Depends(get_session),
):
    """Get all redirects."""
    result = await session.exec(select(Redirect))
    return result.all()


@router.post("/")
async def create_redirect(
    redirect: RedirectCreate, session: AsyncSession = Depends(get_session)
):
    db_redirect = Redirect.from_orm(redirect)
    session.add(db_redirect)
    await session.commit()
    session.refresh(db_redirect)
    return db_redirect
