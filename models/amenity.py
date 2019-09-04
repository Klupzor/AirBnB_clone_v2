#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base, os_type_storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    if os_type_storage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
