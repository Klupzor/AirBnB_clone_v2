#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
