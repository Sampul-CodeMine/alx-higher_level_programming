#!/usr/bin/python3

"""A python file that creates a class that links to a Database
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv as sysarg
    from model_state import Base, State
    from sqlalchemy import create_engine

    connection = MySQLdb.connect(
        host="localhost", port=3306, user=sysarg[1],
        password=sysarg[2], database=sysarg[3])

    engine = create_engine('mysql+mysqldb://', creator=lambda: connection,
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
