#!/usr/bin/python

import psycopg2
from config import config

package_name = "testing_packages_feeder_return_id_3rd_test"
# this package id should be retrieved using the package_id_retriever function
package_id = 9
version = "1.0.0"
cg_generator = "CScout"

def insert_package_versions(package_id, version, cg_generator):
    """ insert a new package versions into the package versions table """
    sql = """INSERT INTO package_versions(package_id, version, cg_generator) VALUES(%s, %s, %s) RETURNING id"""
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
        cur.execute(sql, (package_id, version, cg_generator))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print("The package_version id of "+package_name+" "+version+" is: "+str(id))
    return id

if __name__ == '__main__':
    insert_package_versions(package_id, version, cg_generator)
