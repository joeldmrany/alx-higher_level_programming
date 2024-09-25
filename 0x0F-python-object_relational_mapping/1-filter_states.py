#!/usr/bin/python3
""" states """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    q_rows = cur.fetchall()
    for row in q_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    conn.close()
