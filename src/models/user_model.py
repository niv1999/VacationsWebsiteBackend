# User Model: for the use of any user- both regular and admin.
class UserModel:

    # Ctor:
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name= last_name
        self.email = email
        self.password = password
        self.role_id = role_id
    
    # Display the user:
    def display(self):
        print(f"ID: {self.user_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Password: {self.password}, Role ID: {self.role_id}")
    
    # Convert dictionary to User Model:
    @staticmethod
    def dictionary_to_user(dictionary):
        user = UserModel(
            dictionary["user_id"], dictionary["first_name"], dictionary["last_name"], dictionary["email"], dictionary["password"], dictionary["role_id"])
        return user
        
    # Convert a list of dictionaries to a list of User Models:
    @staticmethod
    def dictionaries_to_users(list):
        users_list = []
        for item in list:
            user = UserModel.dictionary_to_user(item)
            users_list.append(user)
        return users_list