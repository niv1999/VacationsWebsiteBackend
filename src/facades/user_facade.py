from logic.user_logic import *

class UserFacade:
    
    def __init__(self):
        self.user_logic = UserLogic()

    # Work in progress- need to add validity check
    def sign_up(self, first_name, last_name, email, password):
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