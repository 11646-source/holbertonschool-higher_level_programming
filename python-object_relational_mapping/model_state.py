#!/usr/bin/python3
"""
Defines the State class and links it to the MySQL table 'states'
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()

class State(Base):
    """
    State class:
    - Inherits from Base
    - Links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine("mysql+mysqldb://username:password@localhost:3306/databasename")

    # Import all classes inheriting from Base BEFORE calling create_all
    Base.metadata.create_all(engine)
