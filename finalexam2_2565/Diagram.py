class Person:
    def __init__(self,name,age,gmail):
        self.name = name
        self.age = age
        self.gmail = gmail
    def person_detail(self):
        return "".join(f'Name: {self.name} Age: {self.age} Gmail: {self.gmail}')

class Student(Person):
    def __init__(self,name,age,gmail,sid,major):
        super().__init__(name,age,gmail)
        self.sid = sid
        self.major = major

    def student_detail(self):
        return "".join(f'Student Name: {self.name} Age: {self.age} Gmail: {self.gmail} SID: {self.sid} Major: {self.major}')

class Employee(Person):
    def __init__(self,name, age, gmail,eid,position):
        super().__init__(name, age, gmail)
        self.eid = eid
        self.position = position

    def employee_detail(self):
        return "".join(f'EID: {self.eid} Position: {self.position}')

class Devices:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def devices_detail(self):
        return "".join(f'Brand: {self.brand} Model: {self.model} Peice: {self.price}')

class Tablet(Devices):
    pass

class Laptop(Devices):
    pass

class Mobile(Devices):
    pass

class Device_Report:
    Devices_Report = ""

    def Devices_Report_detail(self):
        print(self.student.student_detail())
        print(self.employee.employee_detail())

        for x in range(len(self.Devices_Report)):
            print(f'\t {x+1} student: {self.student[x]} employee: {self.employee[x]}')