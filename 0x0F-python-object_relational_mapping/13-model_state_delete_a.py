#!/usr/bin/python3

"""A script to delete all states containing `a` in its name SQLAlchemy ORM"""

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

    delete_states = session.query(State).filter(State.name.like('%a%')).all()

    if delete_states:
        for state in delete_states:
            session.delete(state)
        session.commit()
    session.close()
    connection.close()
