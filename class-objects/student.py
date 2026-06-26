class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)


s1 = Student("Hari", 21)
s1.display()