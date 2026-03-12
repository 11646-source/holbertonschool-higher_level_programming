#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments: username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Bind session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a', ordered by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
