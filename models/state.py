#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    cities = relationship('City',
                          cascade='all, delete', backref='state.id')
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
