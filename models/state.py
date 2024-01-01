#!/usr/bin/python3
""" HBNB project """
import models
from models.city import City
from models.place import Place
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        """
        getter cities that returns
        the list of City instances with state_id
        """
        list_cities = []
        dict_cities = models.storage.all(City)
        for key, city in dict_cities.items():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
