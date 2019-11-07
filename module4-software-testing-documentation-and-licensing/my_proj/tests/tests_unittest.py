import unittest
import random
from src.animal import Animal

class TestAnimal(unittest.TestCase):
    
    # Do before each test.
    def setUp(self):
        self.test_age = random.randInt(0, 100)
        self.animal = Animal(age=self.test_age)

    # Do after each test.
    def tearDown(self):
        # tearDown here.

        
    def test_repr(self):
        self.assertEqual(repr(self.animal), f'Animal(age={self.test_age})')

    def test_str(self):
        self.assertEqual(str(self.animal), f"This is an animal that's {self.test_age} years old"))

    def test_age_next_year(self):
        self.assertEqual(self.animal.age_next_year(), self.test_age + 1)

    def test_add_one_year(self):
        animal.test_add_one_year()
        self.assertEqual(self.animal.age, self.test_age + 1)


if __name__ == '__main__':
    unittest.main()