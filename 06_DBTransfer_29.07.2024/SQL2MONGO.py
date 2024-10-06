import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient
from pymongo.errors import ConnectionError

def fetch_data_from_mysql():
    connection = None
    cursor = None
    try:
        # Establishing the MySQL connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='insta'
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Creating a cursor object
            cursor = connection.cursor()

            # SQL query to fetch data
            query = "SELECT * FROM userdata"
            cursor.execute(query)

            # Fetching all rows
            rows = cursor.fetchall()

            # Column names for MongoDB
            column_names = [desc[0] for desc in cursor.description]

            # Prepare data for MongoDB
            data = [dict(zip(column_names, row)) for row in rows]

            return data

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
        print("MySQL connection is closed")

def insert_data_into_mongodb(data):
    try:
        # Establishing the MongoDB connection
        client = MongoClient('127.0.0.1', 27017)
        db = client['instaa']
        collection = db['userdaata']

        # Inserting data into MongoDB
        if data:
            result = collection.insert_many(data)
            print(f"Data inserted into MongoDB with ids: {result.inserted_ids}")
        else:
            print("No data to insert into MongoDB")

    except ConnectionError as e:
        print(f"Error while connecting to MongoDB: {e}")

    except Exception as e:
        print(f"Error during MongoDB operation: {e}")

    finally:
        client.close()
        print("MongoDB connection is closed")

if __name__ == "__main__":
    data = fetch_data_from_mysql()
    insert_data_into_mongodb(data)
