#!/usr/bin/python3
"""
Lists all State objects,
and corresponding City objects
"""
import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Create the engine and bind it to the session"""

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

    for state in session.query(State):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
