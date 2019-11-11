class Person:
    def __init__(self, name, age=21, gender='unspecified',
                 occupation='unspecified'):
        self.name = name
        self.gender = gender
        self.occupation = occupation

        if age >= 0 and age <= 120:
            self.age = age
        else:
            self.age = 21

    def greets(self, greeter):
        return f'Hello, {greeter}! My name is {self.name}, nice to meet you!'

    def had_birthday(self):
        self.age += 1

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender