from logic.user_logic import *
from validate_email_address import validate_email

# Users Facade:
class UserFacade:
    
    # Ctor - create a UserLogic object:
    def __init__(self):
        self.user_logic = UserLogic()

    # Adding a new user:
    def sign_up(self, first_name, last_name, email, password):
        
        # Check if all arguments were assigned values:
        if any(arg is None or arg=='' for arg in (first_name, last_name, email, password)): 
            raise ValueError("All arguments must have values and cannot be left blank.")
        
        # Check if the email address is valid using the validate_email_address package:
        if not validate_email(email):
            raise ValueError("Invalid Email.")
        
        # Check if email address already exists:
        if self.user_logic.check_email(email):
            raise ValueError("Email already exists.")
        
        # Check if the password is at least 4 characters:
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        
        # Create a User object and return the new user ID:
        user = UserModel(None, first_name, last_name, email, password, 2)
        user.user_id = self.user_logic.add_user(user)
        return user.user_id
    
    # User log in via email and password:
    def log_in(self, email, password):

        # Check if all arguments were assigned values:
        if any(arg is None or arg=='' for arg in (email, password)):
            raise ValueError("All arguments must have values and cannot be left blank.")
        
        # Check if email is valid:
        if not validate_email(email):
            raise ValueError("Invalid Email.")
        
        # Check if password is at least 4 characters long:
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        
        # Get the user:
        user = self.user_logic.get_one_user(email, password)

        # If email+password does not exist:
        if user is None:
            raise ValueError("Something is wrong! check your email and password please.")
        
        return user
    
    # Add like:
    def add_like(self, user_id, vacation_id):
        self.user_logic.add_like(user_id, vacation_id)

    # Delete like:
    def delete_like(self, user_id, vacation_id):
        rows_affected = self.user_logic.delete_like(user_id, vacation_id)
        if rows_affected == 0:
            raise ValueError("That user did not like the vacation in the first place.")

    # Close resources:
    def close(self):
        self.user_logic.close()

    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()