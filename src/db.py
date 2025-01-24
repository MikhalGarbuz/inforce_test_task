import os
import time
from dotenv import load_dotenv

import psycopg2
from psycopg2.extensions import connection as PgConnection  # for type hinting

# Load the .env file
load_dotenv()


def connect_to_db():
    """Connect to the database
        
    To fix the issue that container with DB is not ready when the ETL starts
    added a trivial retry loop, probaly not the best solution but it works
    """
    
    for _ in range(5):
        try:
            connection = psycopg2.connect(
                host="db",
                user=os.getenv("DB_USER"),
                dbname=os.getenv("DB_NAME"),
                password=os.getenv("DB_PASSWORD")
            )
            return connection
        except psycopg2.OperationalError as e:
            print(f"Connection failed: {e}, retrying...")
            time.sleep(5)
    raise Exception("Failed to connect to the DB after several attempts.")


def setup_db(connection: PgConnection) -> None:
    """Sets up the database by creating necessary tables"""
    
    try:
        with open('sql_queries/create_table.sql', 'r') as file:
            create_table_query = file.read()
    except FileNotFoundError:
        print("SQL file not found.")
        return
    
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
    
    connection.commit()
    print("Database setup completed.")
