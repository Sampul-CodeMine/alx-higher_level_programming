#!/usr/bin/python3

"""A python file that creates a class that links to a Database
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], password=sys.argv[2],
                                 database=sys.argv[3])

    engine = create_engine('mysql+mysqldb://', creator=lambda: connection,
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
