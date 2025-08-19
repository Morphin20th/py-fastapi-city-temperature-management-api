from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql.sqltypes import Integer, String

from database.database import Base


class CityModel(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False,)
    additional_info: Mapped[str] = mapped_column(String, nullable=False)

    temperature = relationship("TemperatureModel", back_populates="city")