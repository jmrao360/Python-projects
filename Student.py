class Student:
    def __init__(self):
        self.name = "MJ"
        self.grade = "10th"
        self.__age = 14

    def display(self):
        print("Student Name: ", self.name)
        print("Student Grade: ", self.grade)


s1 = Student()
s1.display()
print(s1.__dict__)