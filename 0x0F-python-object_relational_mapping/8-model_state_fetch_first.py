#!/usr/bin/python3

"""A script to list the first state in the DB using SQLAlchemy ORM"""

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

    state = session.query(State).order_by(State.id).first()

    print("{}: {}".format(state.id, state.name) if state else "Nothing")

    session.close()
    connection.close()
