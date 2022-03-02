# Dependencies
import sqlite3
from sqlite3 import Error
from config import DB_FILE
from helpers import dict_factory


# SQLite database class
class Database:
    # Constructor method
    def __init__(self) -> None:
        # Public properties
        self.conn = None
        self.cur = None

        # Try to create a database Connection
        try:
            # Create a database connection (also create it if not exists)
            self.conn = sqlite3.connect(DB_FILE)

            # Convert rows to list of dictionaries
            self.conn.row_factory = dict_factory

            # Create the connection cursor
            self.cur = self.conn.cursor()

            # Test the connection
            # print("Database connection created")

        # Catch error
        except Error as e:
            # Raise error
            raise Exception(e)


    #  Destructor method
    def __del__(self):
        # Check the database connection
        if self.conn:
            # Commit query result
            self.conn.commit()

            # Close the connection
            self.conn.close()

            # For test
            # print("Database Connection Closed!")


    ##
    # @desc query method
    #
    # @param sql: str -- *Required SQL statement (ex. "SELECT * FROM users")
    # @param data_bind: list -- Optional data to bind to the sql safely
    #
    # @var result: object -- Database query
    #
    # @return any
    ##
    def query(self, sql: str, data_bind: list = []):

        # Check required params
        if not sql:
            # Raise error
            raise Exception(
                "You must provide the required parameters: ['sql']")

        # Try to query to the database
        try:
            # Return the query result
            self.cur.execute(sql, data_bind)

            return self.cur

        # Catch error
        except Error as e:
            # Raise error
            raise Exception(e)
