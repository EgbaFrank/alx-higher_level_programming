#!/usr/bin/python3
"""
This module contains a script that lists all
State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect usage")
        exit(1)

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

    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")

    session.close()
