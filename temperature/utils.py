from datetime import datetime

import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from city.models import CityModel
from settings import get_settings

settings = get_settings()


async def fetch_weather(city: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            settings.BASE_WEATHER_URL,
            params={"key": settings.WEATHER_API_KEY, "q": city},
        )
        data = response.json()
        localtime = datetime.strptime(data["location"]["localtime"], "%Y-%m-%d %H:%M")
        return {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "date_time": localtime,
        }


async def get_cities_id_and_name(db: AsyncSession) -> list[tuple[int, str]]:
    query = select(CityModel.id, CityModel.name)
    result = await db.execute(query)
    return result.all()
