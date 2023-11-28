from logic.vacation_logic import *

class VacationFacade:
    
    def __init__(self):
        self.vacation_logic = VacationLogic()

    def get_all_vacations(self):
        pass

    def add_vacation(self):
        pass

    def update_vacation(self):
        pass

    def delete_vacation(self):
        pass

    def close(self):
        self.vacation_logic.close()

    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()