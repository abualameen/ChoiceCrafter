# #!/usr/bin/python
# import models
# from models.base_model import BaseModel, Base
# from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
# from sqlalchemy.orm import relationship



# class AlternativeValue(BaseModel, Base):
#     __tablename__ = 'alternative_value'
#     id = Column(Integer, primary_key=True)
#     # user_id = Column(Integer, ForeignKey('alternative.id'))
#     alternative_value = Column(Integer, nullable=False)
#     criteria_name = Column(String(100), nullable=False)
#     # alternative = relationship('Alternative', back_populates='alternative_values')

#     def __init__(self, *args, **kwargs):
#         """initializes criteria"""
#         super().__init__(*args, **kwargs)

        