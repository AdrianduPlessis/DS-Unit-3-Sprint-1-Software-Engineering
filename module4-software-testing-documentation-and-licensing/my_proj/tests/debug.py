from src.dog import Dog
from src.person import Person

barker = Dog(4, 74)
print(barker.age)

greeter = 'Elon Musk'
test = Person('test', 23)
test.greets(greeter)

print(f'Hello, {greeter}! My name is {test.name}, nice to meet '\
f'you!')