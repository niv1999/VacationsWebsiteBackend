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

    def delete_vacation(self, vacation_id):
        rows_affected = self.vacation_logic.delete_vacation(vacation_id)
        if rows_affected == 0:
            raise ValueError("Non-existent vacation ID")

    def close(self):
        self.vacation_logic.close()

    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()