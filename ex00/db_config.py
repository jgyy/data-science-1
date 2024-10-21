import psycopg2
from psycopg2 import sql
import configparser

# Read database configuration from a config file
config = configparser.ConfigParser()
config.read('database.ini')

# Database connection parameters
db_params = {
    'host': config['postgresql']['host'],
    'database': config['postgresql']['database'],
    'user': config['postgresql']['user'],
    'password': config['postgresql']['password']
}

def connect_to_db():
    """Establish a connection to the database."""
    try:
        conn = psycopg2.connect(**db_params)
        print("Connected to the database successfully.")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def search_by_id(conn, table_name, id_column, id_value):
    """Search for a record by ID in the specified table."""
    try:
        cursor = conn.cursor()
        query = sql.SQL("SELECT * FROM {} WHERE {} = %s").format(
            sql.Identifier(table_name),
            sql.Identifier(id_column)
        )
        cursor.execute(query, (id_value,))
        record = cursor.fetchone()
        if record:
            print(f"Record found: {record}")
        else:
            print(f"No record found with {id_column} = {id_value}")
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while searching for record:", error)

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        search_by_id(conn, "customers", "customer_id", 1)
        conn.close()
        print("Database connection closed.")
