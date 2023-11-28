from facades.user_facade import *
from facades.vacation_facade import *

class Test:

    def __init__(self):
        self.user_facade = UserFacade()
        self.vacation_facade = VacationFacade()

    def test_sign_up(self):
        try:
            user_id = self.user_facade.sign_up("Bart", "Simpson", "simpbart1@outlook.com", "1234")
            print(f"User #{user_id} added successfully!")
        except Exception as err:
            print(err)

    def test_log_in(self):
        pass

    def test_add_like(self):
        pass

    def test_delete_like(self):
        pass

    def test_get_all_vacations(self):
        pass

    def test_add_vacation(self):
        pass

    def test_update_vacation(self):
        pass

    def test_delete_vacation(self):
        pass

    def test_all(self):
        self.test_sign_up()
        self.test_log_in()
        self.test_add_like()
        self.test_delete_like()
        self.test_get_all_vacations()
        self.test_add_vacation()
        self.test_update_vacation()
        self.test_delete_vacation()

    def close(self):
        self.user_facade.close()
        self.vacation_facade.close()

    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
