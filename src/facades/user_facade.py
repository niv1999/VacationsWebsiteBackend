from logic.user_logic import *
from validate_email_address import validate_email

class UserFacade:
    
    def __init__(self):
        self.user_logic = UserLogic()

    # User sign up:
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
        
        # Create a User object
        user = UserModel(None, first_name, last_name, email, password, 2)
        user.user_id = self.user_logic.add_user(user)
        return user.user_id
    
    def log_in(self):
        pass

    def add_like(self):
        pass

    def delete_like(self):
        pass

    def close(self):
        self.user_logic.close()