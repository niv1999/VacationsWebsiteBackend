# Vacation Model:
class VacationModel:

    # Ctor (country_name is optional):
    def __init__(self, vacation_id, country_id, description, start_date, end_date, price, file_name, country_name=None):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.file_name = file_name
        self.country_name = country_name

    # Display the vacation:
    def display(self):
        print(f"Vacation ID: {self.vacation_id}, Country ID: {self.country_id}, Country Name: {self.country_name}")
        print(f"Description: {self.description}")
        print(f"Dates: {self.start_date} - {self.end_date}")
        print(f"Price: ${self.price}")

    # Convert dictionary to a Vacation Model:
    @staticmethod
    def dictionary_to_vacation(dict):
        vacation = VacationModel(
            dict["vacation_id"], dict["country_id"], dict["description"], dict["start_date"], dict["end_date"], dict["price"], dict["file_name"], dict["country_name"])
        return vacation
    
    # Convert a list of dictionaries to a list of Vacation Models:
    @staticmethod
    def dictionaries_to_vacations(list):
        vacations = []
        for item in list:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
