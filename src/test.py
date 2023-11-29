from facades.user_facade import *
from facades.vacation_facade import *

class Test:

    def test_sign_up(self):
        try:
            with UserFacade() as user_facade:
                user_id = user_facade.sign_up("Efrat", "Gosh", "efgefg@outlook.com", "1234")
                print(f"User #{user_id} added successfully!")
        except Exception as err:
            print(err)

    def test_log_in(self):
        try:
            with UserFacade() as user_facade:
                user = user_facade.log_in("simpbart1@outlook.com", "12345678")
                print(f"Welcome {user.first_name} {user.last_name}!\nThank you for logging in 🥰")
        except Exception as err:
            print(err)

    def test_add_like(self):
        try:
            with UserFacade() as user_facade:
                user_id = 3
                vacation_id = 3
                user_facade.add_like(user_id, vacation_id)
                print(f"User #{user_id} has liked vacation #{vacation_id}!")
        except Exception as err:
            print(err)

    def test_delete_like(self):
        try:
            with UserFacade() as user_facade:
                user_id = 3
                vacation_id = 3
                user_facade.delete_like(user_id, vacation_id)
                print(f"User #{user_id} has unliked vacation #{vacation_id}!")
        except Exception as err:
            print(err)

    def test_get_all_vacations(self):
        pass

    def test_add_vacation(self):
        pass

    def test_update_vacation(self):
        pass

    def test_delete_vacation(self):
        try:
            with VacationFacade() as vacation_facade:
                vacation_id = 12
                vacation_facade.delete_vacation(vacation_id)
                print(f"Vacation #{vacation_id} has been successfully deleted.")
        except Exception as err:
            print(err)

    def test_all(self):
        self.test_sign_up()
        self.test_log_in()
        self.test_add_like()
        self.test_delete_like()
        self.test_get_all_vacations()
        self.test_add_vacation()
        self.test_update_vacation()
        self.test_delete_vacation()