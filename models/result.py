#!/usr/bin/python
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, ForeignKey, JSON
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import relationship


class Result(BaseModel, Base):
    __tablename__ = 'result'
    criteria_name = Column(String(5000), nullable=False)
    best_alternative = Column(String(5000), nullable=False)
    performance_score = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)
