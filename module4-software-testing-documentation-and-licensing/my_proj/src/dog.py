import datetime as dt

from src.animal import Animal


class Dog(Animal):
    num_legs = 4

    def __init__(self, age, weight, last_time_fed=None):
        if age < 0:
            raise ValueError('age value must be greater than 0')
        if weight < 0:
            raise ValueError('weight value must be greater than 0')
        super().__init__(age)
        self.weight = weight
        if last_time_fed is None:
            self.last_time_fed = dt.datetime.now()

    @staticmethod
    def bark():
        print('woof-woof')

    def is_puppy(self):
        if self.age <= 1:
            return True
        else:
            return False

    def eat(self):
        self.weight = 1.01 * self.weight

    def get_time_last_fed(self):
        time_sec_since_last_time_fed = (dt.datetime.now() - self.last_time_fed).total_seconds()
        return time_sec_since_last_time_fed

    def is_hungry(self):
        if self.get_time_last_fed() > 10:  # seconds
            return True
        else:
            return False

    def __repr__(self):
        return f'Dog(age={self.age}, weight={self.weight})'

    def __str__(self):
        return f"This is an dog that's {self.age} old"

    def __eq__(self, other):
        return (self.age == other.age) and (self.weight == other.weight)

    def __lt__(self, other):
        return self.weight < other.weight
