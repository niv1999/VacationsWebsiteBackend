from logic.vacation_logic import *
from datetime import *
from operator import attrgetter

# Vacations Facade:


class VacationFacade:

    # Ctor - create a VacationLogic object.
    def __init__(self):
        self.vacation_logic = VacationLogic()

    # Get all the vacations sorted by a sorting factor (with an option for a reversed list, default is False):
    def get_all_vacations_sorted(self, sorting_factor, *, reverse=False):

        # Check if "sorting_factor" is in fact a Vacation Model attribute:
        if not sorting_factor.lower() in ("vacation_id", "country_id", "description", "start_date", "end_date", "price", "file_name"):
            raise ValueError(
                "The sorting factor sent is not a vacation attribute.")

        # Get all vacations:
        vacations_list = self.vacation_logic.get_all_vacations()

        # Sort the vacations list by the sorting factor sent (using the "operator" module to convert the string to a Vacation Model attribute):
        sorted_vacations_list = sorted(vacations_list, key=attrgetter(
            sorting_factor.lower()), reverse=reverse)
        return sorted_vacations_list

    # Add a new vacation:
    def add_vacation(self, role_id, country_id, description, start_date, end_date, price, file_name):

        # Check if all arguments were assigned values:
        if any(arg is None or arg == '' for arg in (role_id, country_id, description, start_date, end_date, price, file_name)):
            raise ValueError(
                "All arguments must have values and cannot be left blank.")

        # Check that the role ID corresponds to an Admin:
        if role_id != 1:
            raise PermissionError(
                "You don't have permission to execute this action. Admin role required.")

        # Check if the country ID exists in the database:
        if self.vacation_logic.get_country(country_id) is None:
            raise ValueError("There's no such country ID in the database")

        # Check if price is between 0 to 10,000:
        if not 0 <= float(price) <= 10000:
            raise ValueError("The price must be between $0 and $10,000.")

        # Check the current date and convert the date strings into date format by using the "datetime" module:
        current_date = datetime.now().date()
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Check if the given starting date is not in the past:
        if current_date > formatted_start_date:
            raise ValueError("The start date can't be in the past")

        # Check that the start date is before the end date:
        if formatted_start_date > formatted_end_date:
            raise ValueError(
                "The end date of the vacation can't be before the start date")

        # Create a vacation object and return its automatically generated ID:
        vacation = VacationModel(
            None, country_id, description, start_date, end_date, price, file_name)
        vacation.vacation_id = self.vacation_logic.add_vacation(vacation)
        return vacation.vacation_id

    # Update an existing vacation (does not require a file name to be sent):
    def update_vacation(self, role_id, vacation_id, country_id, description, start_date, end_date, price, file_name=None):

        # Check if all arguments were assigned values (except file name):
        if any(arg is None or arg == '' for arg in (country_id, description, start_date, end_date, price, role_id)):
            raise ValueError(
                "All arguments must have values and cannot be left blank.")

        # Check that the role ID corresponds to an Admin:
        if role_id != 1:
            raise PermissionError(
                "You don't have permission to execute this action. Admin role required.")

        # Check if the vacation exists:
        existing_vacation = self.vacation_logic.get_one_vacation(vacation_id)
        if existing_vacation is None:
            raise ValueError("The vacation doesn't exist in the database.")

        # Check if the country ID exists in the database:
        if self.vacation_logic.get_country(country_id) is None:
            raise ValueError("There's no such country ID in the database")

        # Check if price is between 0 to 10,000:
        if not 0 <= float(price) <= 10000:
            raise ValueError("The price must be between $0 and $10,000.")

        # Convert the start and end dates from string to a date type using the "datetime" module:
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Check that the start date is before the end date:
        if formatted_start_date > formatted_end_date:
            raise ValueError(
                "The end date of the vacation can't be before the start date")

        # If no file name was sent, extract the file name from the existing vacation:
        if file_name is None:
            file_name = existing_vacation.file_name

        # Create the new vacation module and send it to the BLL update_vacation function:
        vacation = VacationModel(
            vacation_id, country_id, description, start_date, end_date, price, file_name)
        rows_affected = self.vacation_logic.update_vacation(vacation)

        # If no rows were affected, then no new data was inserted:
        if rows_affected == 0:
            return f"No changes have been committed to vacation #{vacation_id}"

        return f"Vacation #{vacation_id} has been updated successfully!"

    # Delete an existing vacation:
    def delete_vacation(self, role_id, vacation_id):

        # Check that the role ID corresponds to an Admin:
        if role_id != 1:
            raise PermissionError(
                "You don't have permission to execute this action. Admin role required.")

        # Attempt to delete the vacation:
        rows_affected = self.vacation_logic.delete_vacation(vacation_id)

        # If 0 vacations were affected, then nothing was deleted meaning the vacation ID does not exist:
        if rows_affected == 0:
            raise ValueError("Non-existent vacation ID")

    # Close resources:
    def close(self):
        self.vacation_logic.close()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
