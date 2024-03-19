#!/usr/bin/python3
"""

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """"""


username = argv[1]
password = argv[2]
database = argv[3]
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
