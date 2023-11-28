import mysql.connector

# Data Access Layer:
class DAL:
    
    # ctor - creating a connection:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="vacations")

    # Getting back an entire table as a list of dictionaries:
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table
    
    # Getting back a scalar dictionary:
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar
    
    # Adding a new row:
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            last_row_id = cursor.lastrowid
            return last_row_id

    # Updating existing row:    
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count
    
    # Deleting existing row:
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count
    
    # Closing the connection:
    def close(self):
        self.connection.close()
