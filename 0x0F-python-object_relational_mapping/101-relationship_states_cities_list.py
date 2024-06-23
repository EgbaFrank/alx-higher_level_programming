#!/usr/bin/python3
"""
Creates the State “California”
with the City “San Francisco”
"""

import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Usage check
    if len(sys.argv) != 4:
        print(
                "Usage: {} <mysql username> <mysql password> <database name>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    # Create the engine and bind it to the session
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]
                    ),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
