from logic.vacation_logic import *
from datetime import * 


class VacationFacade:
    
    def __init__(self):
        self.vacation_logic = VacationLogic()

    def get_all_vacations(self):
        vacations_list = self.vacation_logic.get_all_vacations()
        # add sort by dates 
        return vacations_list

    def add_vacation(self, country_id, description, start_date, end_date, price, file_name):
        
        # Check if all arguments are valid:
        if any(arg is None or arg=='' for arg in (country_id, description, start_date, end_date, price, file_name)): 
            raise ValueError("All arguments must have values and cannot be left blank.")
        
        #check if the price >0 and price <10,000
        if float(price) < 0 or float(price)> 10000: 
            raise ValueError ("The price must be between 0 and 10,000")
        
        #check the start date
        current_date = datetime.now().date()
        # formatted_current_date = datetime.strptime(current_date, "%Y-%m-%d").date()
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if current_date > formatted_start_date:
            raise ValueError ("The start date can't be in the past")
        
        #check if the end_date > start_date
        if formatted_start_date > formatted_end_date:
            raise ValueError ("The end date of the vacation can't be sooner than the start date")
        
        vacation = VacationModel (None, country_id, description, start_date, end_date, price, file_name)
        last_inserted_id = self.vacation_logic.add_vacation(vacation)
        return last_inserted_id

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