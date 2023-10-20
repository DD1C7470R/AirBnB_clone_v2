#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        name = Column('name', String(128), nullable=False)
        cities = relationship("City", back_populates="state")

    else:
        name = ""

        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City

            obj_list = []
            strg = storage.all(City)
            for key, value in strg.items():
                if self.id == value.state_id:
                    obj_list.append(value)
            return obj_list
