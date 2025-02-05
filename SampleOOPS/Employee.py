class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display_info(self):
        return f"{self.name} {self.age}"
        
p1=Person("nivi", 22)
print(p1.display_info())

class Employee(Person):
    def __init__(self, name, age, empId):
        super().__init__(name, age)
        self.empId=empId

    def display_info(self):
        return f"{super().display_info()} with {self.empId} as employee id"
    
e1=Employee("nivi", 22, 142)
print(e1.display_info())