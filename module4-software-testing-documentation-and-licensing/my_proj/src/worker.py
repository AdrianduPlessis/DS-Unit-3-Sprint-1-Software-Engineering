from src.person import Person

class Worker(Person):
    def __init__(self, name, age=21, gender='unspecified',
                 occupation='unspecified', company='unspecified',
                 job_title='unspecified', personal_title='unspecified'):
        super().__init__(name, age, gender, occupation)
        self.company = company
        self.job_title = job_title
        self.personal_title = personal_title

    def __repr__(self):
        return f'Worker: {self.company}'

    def greets(self, title, greeter):
        return f'Hello {title} {greeter}! My name is {self.name}, I work for {self.company}.'
