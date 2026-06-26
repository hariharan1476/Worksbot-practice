class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Hari", 30000)
e1.show()