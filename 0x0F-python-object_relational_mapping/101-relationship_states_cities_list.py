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
    """Create the engine and bind it to the session"""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]
                    ),
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = (
            session.query(State)
            .outerjoin(City).all()
            )

    if instances:
        for state in instances:
            print(f"{state.id}: {state.name}")
            for inst in state.cities:
                print(f"\t{inst.id}: {inst.name}")

    session.close()
