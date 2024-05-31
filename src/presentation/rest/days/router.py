from fastapi import APIRouter, Query

from src.domain.days.service import days_left
from src.domain.days.schema import DaysCounterResponse

days_counter_router = APIRouter(prefix="/days", tags=["Days counter"])

@days_counter_router.get("/", response_model=DaysCounterResponse)
async def days_counter(
    year: int = Query(..., description="Год"),
    month: int = Query(..., description="Месяц"),
    day: int = Query(..., description="День")
) -> DaysCounterResponse:
    result = days_left(year, month, day)
    return DaysCounterResponse(**result)
