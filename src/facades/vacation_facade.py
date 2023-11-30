from logic.vacation_logic import *
from datetime import * 

class VacationFacade:
    
    def __init__(self):
        self.vacation_logic = VacationLogic()

    def get_all_vacations(self):
        vacations_list = self.vacation_logic.get_all_vacations()
        sorted_vacations_list = sorted(vacations_list, key=lambda vacation: vacation.start_date)
        return sorted_vacations_list

    def add_vacation(self, country_id, description, start_date, end_date, price, file_name):
        
        # Check if all arguments have values:
        if any(arg is None or arg=='' for arg in (country_id, description, start_date, end_date, price, file_name)): 
            raise ValueError("All arguments must have values and cannot be left blank.")
        
        # Check if price is between 0 to 10,000:
        if float(price) < 0 or float(price) > 10000: 
            raise ValueError("The price must be between 0 and 10,000.")
        
        # Check the current date and convert the date strings into date format:
        current_date = datetime.now().date()
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Check if the given starting date is not in the past:
        if current_date > formatted_start_date:
            raise ValueError("The start date can't be in the past")
        
        # Check that the start date is before the end date:
        if formatted_start_date > formatted_end_date:
            raise ValueError("The end date of the vacation can't be sooner than the start date")
        
        # Create a vacation object:
        vacation = VacationModel(None, country_id, description, start_date, end_date, price, file_name)
        vacation.vacation_id = self.vacation_logic.add_vacation(vacation)
        return vacation.vacation_id

    def update_vacation(self, vacation_id, country_id, description, start_date, end_date, price, file_name=None):
        
        # Check if the vacation exists:
        existing_vacation = self.vacation_logic.get_one_vacation(vacation_id)
        if existing_vacation is None:
            raise ValueError("The vacation doesn't exist in the database.")
        
        # Check if all arguments have values:
        if any(arg is None or arg=='' for arg in (country_id, description, start_date, end_date, price)): 
            raise ValueError("All arguments must have values and cannot be left blank.")
        
        # Check if price is between 0 to 10,000:
        if float(price) < 0 or float(price) > 10000: 
            raise ValueError("The price must be between 0 and 10,000.")
        
        # Convert the start and end dates from string to a date type:
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Check that the start date is before the end date:
        if formatted_start_date > formatted_end_date:
            raise ValueError("The end date of the vacation can't be sooner than the start date")
        
        # If no file name was sent, extract the file name from the existing vacation:
        if file_name is None:
            file_name = existing_vacation.file_name
    
        vacation = VacationModel(vacation_id, country_id, description, start_date, end_date, price, file_name)
        rows_affected = self.vacation_logic.update_vacation(vacation)
        if rows_affected == 0:
            return f"No changes have been committed to vacation #{vacation_id}"
        return f"Vacation #{vacation_id} has been updated successfully!"

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