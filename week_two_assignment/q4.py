class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_to_database(self):
        user_database.update(
            {self.name: {'name': self.name, 'score': self.score}})

    def print_database(self):
        print(user_database)


user_database = {}

while True:
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    current_student = Student(name, score)
    current_student.add_to_database()
    current_student.print_database()

    print('----------------')
