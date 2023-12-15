from logic.user_logic import *
from logic.vacation_logic import *
from validate_email_address import validate_email

# Users Facade:


class UserFacade:

    # Ctor - create a UserLogic object:
    def __init__(self):
        self.user_logic = UserLogic()

    # Adding a new user:
    def sign_up(self, first_name, last_name, email, password):

        # Check if all arguments were assigned valid values (more than 1 character):
        if any(arg is None or len(arg.strip()) < 2 for arg in (first_name, last_name, email, password)):
            raise ValueError(
                "All arguments must have a value of at least 2 characters.")

        # Check if the email address is valid using the validate_email_address package:
        if not validate_email(email):
            raise ValueError("Invalid Email.")

        # Check if email address already exists:
        if self.user_logic.check_email(email):
            raise ValueError(
                "Email already exists! Can't sign up with an existing Email.")

        # Check if the password is at least 4 characters:
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")

        # Create a User object and return the new user ID:
        # The 2 stands for the Role ID of the user which is by default a "user" and not an "admin"
        user = UserModel(None, first_name, last_name, email, password, 2)
        user.user_id = self.user_logic.add_user(user)
        return user.user_id

    # User log in via email and password:
    def log_in(self, email, password):

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
            raise ValueError(
                "Something is wrong! check your Email and password please.")

        return user

    # Add like:
    def add_like(self, user_id, vacation_id):

        # Check if the user and the vacation exist in the database:
        check_user = self.user_logic.get_one_user_by_id(user_id)
        vacation = VacationLogic()
        check_vacation = vacation.get_one_vacation(vacation_id)
        if check_user is None or check_vacation is None:
            raise ValueError(
                "The user and/or vacation does not exist in the database.")

        # Check that the role ID corresponds to a User:
        if check_user.role_id != 2:
            raise PermissionError(
                "You don't have permission to execute this action. User role required.")

        # Check if the user already liked this vacation before:
        if self.user_logic.check_like(user_id, vacation_id):
            raise ValueError("The user already liked this vacation.")

        # After checking that both the user and vacation exist, and the user didn't like this vacation before, then add the like:
        self.user_logic.add_like(user_id, vacation_id)

    # Delete like:
    def delete_like(self, user_id, vacation_id):

        # Check if the user and the vacation exist in the database:
        check_user = self.user_logic.get_one_user_by_id(user_id)
        vacation = VacationLogic()
        check_vacation = vacation.get_one_vacation(vacation_id)
        if check_user is None or check_vacation is None:
            raise ValueError(
                "The user and/or vacation does not exist in the database.")

        # Check that the role ID corresponds to a User:
        if check_user.role_id != 2:
            raise PermissionError(
                "You don't have permission to execute this action. User role required.")

        # Make sure the user already liked the vacation before, if not raise and exception:
        if not self.user_logic.check_like(user_id, vacation_id):
            raise ValueError(
                "That user did not like the vacation in the first place.")

        # After checking that both the user and vacation exist, and that the user already liked this vacation, then delete the like:
        self.user_logic.delete_like(user_id, vacation_id)

    # Close resources:
    def close(self):
        self.user_logic.close()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
