import datetime as dt
import json
import uuid
from pathlib import Path

from src.animal import Animal


class Dog(Animal):
    num_legs = 4

    def __init__(self, age, weight, last_time_fed=None):
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

    def save_to_json(self, out_path):
        unique_id = str(uuid.uuid4())
        f_path = Path(out_path)/f'dog_{unique_id}.json'
        json_data = {'age': self.age,
                     'weight': self.weight}
        with open(f_path, 'w') as f:
            json.dump(json_data, f)
        return f_path

    @classmethod
    def load_from_json(cls, f_path):
        with open(f_path) as f:
            json_data = json.load(f)
        age = json_data['age']
        weight = json_data['weight']
        return cls(age, weight)

    def __repr__(self):
        return f'Dog(age={self.age}, weight={self.weight})'

    def __str__(self):
        return f"This is an dog that's {self.age} old"

    def __eq__(self, other):
        return (self.age == other.age) and (self.weight == other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


# dog = Dog(age=5, weight=20)
# f_path = dog.save_to_json('/tmp')
# print(f_path)

# dog = Dog.load_from_json(f_path='/tmp/dog_190d3159-fab3-4d8c-8d39-aaff14963860.json')
# print(dog)