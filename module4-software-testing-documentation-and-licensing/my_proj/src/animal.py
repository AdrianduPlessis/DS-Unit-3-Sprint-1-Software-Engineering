class Animal:
    def __init__(self, age):
        if age < 0:
            raise ValueError('age value must be greater than 0')
        self.age = age

    def __repr__(self):
        return f'Animal(age={self.age})'

    def __str__(self):
        return f"This is an animal that's {self.age} years old"

    def age_next_year(self):
        return self.age + 1

    def add_one_year(self):
        self.age = self.age + 1