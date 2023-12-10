from utils.dal import *
from models.vacation_model import *

# Vacations Business Logic:
class VacationLogic:
    
    # Ctor- Create a DAL object:
    def __init__(self):
        self.dal = DAL()

    # Return all vacations:
    def get_all_vacations(self):
        sql = "SELECT * FROM vacations"
        result = self.dal.get_table(sql)
        vacation_list = VacationModel.dictionaries_to_vacations(result)
        return vacation_list
    
    # Return one vacation by ID:
    def get_one_vacation(self, vacation_id):
        sql = "SELECT * FROM vacations WHERE vacation_id = %s"
        result = self.dal.get_scalar(sql, (vacation_id, ))
        if not result: return None # If the dictionary is empty (meaning vacation ID does not exist) return None.
        vacation = VacationModel.dictionary_to_vacation(result)
        return vacation
    
    # Check if the country exists in the database, return True if it is, and False if its not:
    def check_country(self, country_id):
        sql = "SELECT * FROM countries WHERE country_id = %s"
        result = self.dal.get_scalar(sql, (country_id, ))
        if result is None: return False
        return True
    
    # Add a new vacation:
    def add_vacation(self, vacation):
        sql = "INSERT INTO vacations (country_id, description, start_date, end_date, price, file_name) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, vacation.file_name)
        last_inserted_id = self.dal.insert(sql, params)
        return last_inserted_id
    
    # Update an existing vacation:
    def update_vacation(self, vacation):
        sql = "UPDATE vacations SET country_id=%s, description=%s, start_date=%s, end_date=%s, price=%s, file_name=%s WHERE vacation_id=%s"
        params = (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, vacation.file_name, vacation.vacation_id)
        rows_affected_count = self.dal.update(sql, params)
        return rows_affected_count
    
    # Deleting an existing vacation:
    def delete_vacation(self, vacation_id):
        sql = "DELETE FROM vacations WHERE vacation_id=%s"
        rows_affected_count = self.dal.delete(sql, (vacation_id, ))
        return rows_affected_count
    
    # Close resources:
    def close(self):
        self.dal.close()