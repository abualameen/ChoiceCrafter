#!/usr/bin/python
import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship



class Result(BaseModel, Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    criteria_name = Column(String(100), nullable=False)
    best_alternative = Column(Float, nullable=False)
    performance_score = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('alternative.id'))
    alternative = relationship('Alternative', back_populates='user_num')

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)


