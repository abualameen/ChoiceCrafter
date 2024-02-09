#!/usr/bin/python
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import relationship


class Alternative(BaseModel, Base):
    __tablename__ = 'alternative'
    criteria_name = Column(String(5000), nullable=False)
    criteria_values = Column(String(5000), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes criteria"""
        super().__init__(*args, **kwargs)
