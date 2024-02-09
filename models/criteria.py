#!/usr/bin/python
""" this model contains the criteria class """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import relationship


class Criteria(BaseModel, Base):
    """ this is the criteria class """
    __tablename__ = 'criteria'
    criteriaName = Column(String(5000), nullable=False)
    criteriaType = Column(String(5000), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)
