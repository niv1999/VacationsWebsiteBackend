from facades.user_facade import *
from facades.vacation_facade import *

class Test:

    def test_sign_up(self):
        try:
            with UserFacade() as user_facade:
                last_user_id = user_facade.sign_up("Bart", "Simpson", "simpbart123@gmail.com", "lisa_sucks")
                print(f"User #{last_user_id} added successfully!")
        except Exception as err:
            print(err)

    def test_log_in(self):
        try:
            with UserFacade() as user_facade:
                user = user_facade.log_in("assaffink@gmail.com", "12345678")
                print(f"Welcome {user.first_name} {user.last_name}!\nThank you for logging in 🥰")
        except Exception as err:
            print(err)

    def test_add_like(self):
        try:
            with UserFacade() as user_facade:
                user_id = 2
                vacation_id = 5
                user_facade.add_like(user_id, vacation_id)
                print(f"User #{user_id} has liked vacation #{vacation_id}!")
        except Exception as err:
            print(err)

    def test_delete_like(self):
        try:
            with UserFacade() as user_facade:
                user_id = 2
                vacation_id = 5
                user_facade.delete_like(user_id, vacation_id)
                print(f"User #{user_id} has unliked vacation #{vacation_id}!")
        except Exception as err:
            print(err)

    def test_get_all_vacations(self):
        try: 
            with VacationFacade() as vacation_facade:
                sorting_factor = "start_date"
                vacations_list = vacation_facade.get_all_vacations_sorted(sorting_factor) # You can also send reverse=True for a descending list.
                for vacation in vacations_list:
                    vacation.display()
                    print("---------------------------------\n")
        except Exception as err:
            print (err)

    def test_add_vacation(self):
        try: 
            with VacationFacade() as vacation_facade:
                last_vacation_id = vacation_facade.add_vacation(5, "Explore the historic city of Jerusalem, where ancient history and modern life intertwine. Visit the Old City, home to iconic landmarks such as the Western Wall, the Church of the Holy Sepulchre, and the bustling markets.", "2024-06-26", "2024-07-01", "6000", "jerusalem_haven.jpg")
                print (f"Vacation #{last_vacation_id} has been added!")
        except Exception as err:
            print (err)

    def test_update_vacation(self):
        try:
            with VacationFacade() as vacation_facade:
                response = vacation_facade.update_vacation(13, 2, "Explore the historic city of Athens, where ancient history and modern life intertwine. Visit the Old City, home to iconic landmarks such as the Western Wall, the Church of the Holy Sepulchre, and the bustling markets.", "2023-10-01", "2023-10-4", "5000")
                print(response)
        except Exception as err:
            print(err)

    def test_delete_vacation(self):
        try:
            with VacationFacade() as vacation_facade:
                vacation_id = 13
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