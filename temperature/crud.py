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
    return result.scalars().all()


async def create_temperature(
    db: AsyncSession, city_id: int, temperature: float
) -> TemperatureModel:
    temperature = TemperatureModel(city_id=city_id, temperature=temperature)
    db.add(temperature)
    await db.commit()
    await db.refresh(temperature)
    return temperature
