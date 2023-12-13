# Vacation Model:
class VacationModel:

    # Ctor:
    def __init__(self, vacation_id, country_id, description, start_date, end_date, price, file_name):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.file_name = file_name
        self.country_name = self.get_country_name(country_id)

    # Display the vacation:
    def display(self):
        print(f"Vacation ID: {self.vacation_id}, Country ID: {self.country_id}, Country Name: {self.country_name}")
        print(f"Description: {self.description}")
        print(f"Dates: {self.start_date} - {self.end_date}")
        print(f"Price: ${self.price}")

    # Get country name using country_id:
    def get_country_name(self, country_id):

        # Import within the function to resolve circular import error (VacationLogic is importing from VacationModel, causing an endless loop of importing)
        from logic.vacation_logic import VacationLogic
        vacation_logic = VacationLogic()
        country = vacation_logic.get_country(country_id)
        return country["country_name"]

    # Convert dictionary to a Vacation Model:
    @staticmethod
    def dictionary_to_vacation(dict):
        vacation = VacationModel(
            dict["vacation_id"], dict["country_id"], dict["description"], dict["start_date"], dict["end_date"], dict["price"], dict["file_name"])
        return vacation
    
    # Convert a list of dictionaries to a list of Vacation Models:
    @staticmethod
    def dictionaries_to_vacations(list):
        vacations = []
        for item in list:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
