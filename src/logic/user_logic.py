from utils.dal import *
from models.user_model import *
from models.vacation_model import *

# Users Business Logic:
class UserLogic:
    
    # Ctor- Create a DAL object:
    def __init__(self):
        self.dal = DAL()
    
    # Add a user
    def add_user(self, user):
        sql = "INSERT INTO users (first_name, last_name, email, password, role_id) VALUES (%s, %s, %s, %s, %s)"
        params= (user.first_name, user.last_name, user.email, user.password, user.role_id)
        last_inserted_id = self.dal.insert(sql, params)
        return last_inserted_id
    
    # Get a user by email and password:
    def get_one_user(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        result = self.dal.get_scalar(sql, (email, password))
        if result is None: return None
        user = UserModel.dictionary_to_user(result)
        return user
    
    # Check if email exists in the database, return True if it is, and False if its not:
    def check_email(self, email):
        sql = "SELECT * FROM users WHERE email = %s"
        result = self.dal.get_scalar(sql, (email, ))
        if result is None: return False
        return True
    
    # User adding a like to a vacation
    def add_like(self, user_id, vacation_id):
        sql = "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)"
        params = (user_id, vacation_id)
        self.dal.insert(sql, params)
        
    # User removing a like from a vacation
    def delete_like(self, user_id, vacation_id):
        sql = "DELETE FROM likes WHERE user_id = %s AND vacation_id = %s"
        params = (user_id, vacation_id)
        rows_affected_count = self.dal.delete(sql, params)
        return rows_affected_count
    
    # Close resources:
    def close(self):
        self.dal.close()
