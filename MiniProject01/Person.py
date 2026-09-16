# This class is written by Jiaming Yu

class Person:
    def __init__(self, first_name, last_name, age, address):
        if (not isinstance(first_name, str) or not first_name.strip()
                or not isinstance(last_name, str) or not last_name.strip()
                or not isinstance(age, int)
                or not isinstance(address, str) or not address.strip()):
            raise ValueError('First name, last name and age and address cannot be empty or invalid values')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def get_details(self):
        return f'first name: {self.first_name}, last name: {self.last_name}, age: {self.age}, address: {self.address}'

    def set_first_name(self, first_name):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError('First name cannot be empty or invalid values')
        self.first_name = first_name

    def set_last_name(self, last_name):
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError('last_name cannot be empty or invalid values')
        self.last_name = last_name

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError('Age cannot be empty or invalid values')
        self.age = age

    def set_address(self, address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError('Address cannot be empty or invalid values')
        self.address = address

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address