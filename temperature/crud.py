from datetime import datetime
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from temperature.models import TemperatureModel


async def get_temperatures(db: AsyncSession) -> List[TemperatureModel]:
    query = select(TemperatureModel)
    temperatures = await db.execute(query)
    return temperatures.scalars().all()


async def get_temperature_by_city(
    db: AsyncSession, city_id: int
) -> Optional[TemperatureModel]:
    query = select(TemperatureModel).where(TemperatureModel.city_id == city_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def update_temperatures(
    db: AsyncSession, city_id: int, temperature: float, date_time: datetime
) -> None:
    temp = await get_temperature_by_city(db, city_id)
    if temp:
        temp.temperature = temperature
        temp.date_time = date_time
        await db.commit()
        return
    return
