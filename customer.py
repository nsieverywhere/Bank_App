import random
import string
from dbconnect import save_customer


# class instantiate a new cx and calls the save function immediately which then check if the cx exist or not.
class Customer:
    def __init__(self, name, age, gender, address, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.account_number = self.AccountGen()
        save_customer(self.name, self.age, self.gender,
                      self.address, self.phone_number, self.account_number)

    def AccountGen(self):
        return (''.join(random.choice(string.digits) for _ in range(8)))
