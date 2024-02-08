#!/usr/bin/python
import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Alternative(BaseModel, Base):
    __tablename__ = 'alternative'
    # id = Column(Integer, primary_key=True)
    criteria_name = Column(String(5000), nullable=False)
    criteria_values = Column(String(5000), nullable=False)
   
    # alternative_values = relationship('AlternativeValue', back_populates='alternative')
    # user_num = relationship('Result', back_populates='alternative')

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)


