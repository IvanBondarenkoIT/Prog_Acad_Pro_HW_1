class Customer:
    def __init__(self, full_name: tuple, phone_number: str, other_information: dict):
        self.full_name = full_name
        self.phone_number = phone_number
        self.other_information = other_information

    def __str__(self):
        fio = self.full_name[1] + ' ' + self.full_name[0] + ' ' + self.full_name[2]
        return f"{fio}, phone number:{self.phone_number}"
