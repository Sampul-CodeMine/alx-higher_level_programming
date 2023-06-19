#!/usr/bin/python3

"""A script to print all cities from the DB using SQLAlchemy ORM"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv as sysarg
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    connection = MySQLdb.connect(
        host="localhost", port=3306, user=sysarg[1],
        password=sysarg[2], database=sysarg[3])

    engine = create_engine('mysql+mysqldb://', creator=lambda: connection,
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State, City).filter(State.id ==
                                                   City.state_id).all()

    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    connection.close()
