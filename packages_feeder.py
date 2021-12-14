#!/usr/bin/python

import psycopg2
from config import config

package_name = "testing_packages_feeder"
forge = "Debian"

def insert_package(package_name, forge):
    """ insert a new vendor into the packages table """
    sql = """INSERT INTO packages(package_name, forge) VALUES(%s, %s) RETURNING id"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (package_name, forge,))

        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id

if __name__ == '__main__':
    insert_package(package_name, forge)