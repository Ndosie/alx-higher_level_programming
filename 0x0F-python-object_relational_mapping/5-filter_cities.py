#!/usr/bin/python3
"""Lists all the cities of a state from database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cus = db.cursor()
    cus.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4]))
    recs = cus.fetchall()
    for rec in recs:
        print(rec)
    cus.close()
    db.close()i
