#!/usr/bin/python3
"""
This module contains the class definition of a State
and an Base instance
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition for state instances"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
                'City',
                backref='state',
                cascade='all, delete-orphan'
                )
