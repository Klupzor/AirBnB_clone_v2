#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Review(BaseModel, Base):
    """This is the class for Review
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
