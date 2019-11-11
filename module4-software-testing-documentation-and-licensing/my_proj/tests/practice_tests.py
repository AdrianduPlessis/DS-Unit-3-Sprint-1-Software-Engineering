from src.person import Person
from src.worker import Worker
import random
import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.test_age = random.randint(0, 120)
        self.test_name = 'Jon Doe'
        self.test_gender = 'Male'
        self.test_occupation = 'Teacher'
        self.person = Person(self.test_name, self.test_age, self.test_gender, self.test_occupation)

    def test_name(self):
        self.assertEqual(self.person.gender, 'Male')

    def test_greets(self):
        greeter = 'Elon Musk'
        self.assertEqual(self.person.greets(greeter), f'Hello, {greeter}! My name is {self.person.name}, nice to meet '
                                                      f'you!')
