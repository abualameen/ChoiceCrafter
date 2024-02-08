#!/usr/bin/python
import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import MEDIUMTEXT 



class Result(BaseModel, Base):
    __tablename__ = 'result'
    # id = Column(Integer, primary_key=True)
    criteria_name = Column(String(5000), nullable=False)
    best_alternative = Column(String(5000), nullable=False)
    performance_score = Column(Float, nullable=False)
    # user_id = Column(Integer, ForeignKey('alternative.id'))
    # alternative = relationship('Alternative', back_populates='user_num')

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)


