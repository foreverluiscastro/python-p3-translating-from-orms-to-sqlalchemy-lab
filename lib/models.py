#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    pass
    __tablename__ = 'dogs'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'
        ),   
    )
    
    id = Column(Integer())
    name = Column(String())
    breed = Column(String())
    
    def __repr__(self):
        return f"Dog {self.id}:" \
            + f"{self.name}, " \
            + f"Breed {self.breed}"