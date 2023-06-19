#!/usr/bin/python3

"""A script to update the state with id of 2 using SQLAlchemy ORM"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv as sysarg
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base

    connection = MySQLdb.connect(
        host="localhost", port=3306, user=sysarg[1],
        password=sysarg[2], database=sysarg[3])

    engine = create_engine('mysql+mysqldb://', creator=lambda: connection,
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    session.close()
    connection.close()
