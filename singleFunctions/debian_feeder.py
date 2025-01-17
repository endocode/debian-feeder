import pprint
#from kafka import KafkaConsumer
import psycopg2
import json
import traceback
import random
import time
import pprint

# example taken from Giorgos

packageName = "0xffff"
packageVersion = "0.9-1"

def main():
    try:
        start = time.time()
        conn = psycopg2.connect(
        host="127.0.0.1",
        database="fasten_c",
        user="fasten",
        password="fasten1234")
        cur = conn.cursor()
        #query = "SELECT * FROM packages"
        #query = "INSERT INTO packages(package_name, forge, project_name, repository, created_at) VALUES(%s, %s, %s, %s, %s )"
        query = "INSERT INTO packages(package_name, forge) VALUES(%s, %s)"
        #val = (str(packageName))
        package_name = ("0xffff")
        forge = ("Debian")
        #project_name = ("unknown")
        #repository = ("Debian")
        #created_at = ("1999-01-08")
        cur.execute(query,(package_name, forge,))
        """
        result = cur.fetchall()
        for row in result:
            print(row[0])
        """
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("ERROR:")
        traceback.print_exc()
    finally:
        end = time.time()
        print(end - start)
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
