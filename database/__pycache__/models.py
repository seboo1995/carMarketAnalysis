from typing import Any
from base import Base
from sqlalchemy import Column, String, Integer, Date


class CarTable(Base):
    __tablename__ = 'CarTable'
    title_selector = Column(String)
    additional_info_selector = Column(String)
    year_selector = Column(String)
    horsepower_selector = Column(String)
    mileage_selector = Column(String)
    price_selector = Column(String)
    handler_selector  = Column(String)
    car_id = Column(Integer,primary_key=True)