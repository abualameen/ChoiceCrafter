#!/usr/bin/python

import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


# Base = declarative_base()

class Criteria(BaseModel, Base):
    __tablename__ = 'criteria'
    # id = Column(Integer, primary_key=True)
    criteriaName = Column(String(5000), nullable=False)
    criteriaType = Column(String(5000), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)