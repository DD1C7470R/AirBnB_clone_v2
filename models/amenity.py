#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ """
    __tablename__ = 'amenities'
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column('name', String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary='place_amenity',
            back_populates='amenities',
            viewonly=False
        )
    else:
        name = ""
