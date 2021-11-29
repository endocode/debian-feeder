import pprint
#from kafka import KafkaConsumer
import psycopg2
import json
import traceback
import random
import time
import pprint

# example taken from Giorgos

def main():
    try:
        start = time.time()
        conn = psycopg2.connect(
        host="127.0.0.1",
        database="fasten_c",
        user="fasten",
        password="fasten1234")
        cur = conn.cursor()
        query = "SELECT * FROM dependencies"
        cur.execute(query)
        result = cur.fetchall()
        for row in result:
            print(row[0])
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
