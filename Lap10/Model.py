class Person:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def person_detail(self):
        return "".join(f'Name: {self.name} Age: {self.age} Weight: {self.weight}')

class Student(Person):
    def __init__(self,name,age,weight,major,vaccine,date):
        super().__init__(name,age,weight)  #call init() at super-class
        self.major = major
        self.vaccine = vaccine
        self.date = date
    def student_detail(self):
        return "".join(f'Student Name: {self.name} Age: {self.age} Weight: {self.weight} Major: {self.major} Vaccine: {self.vaccine} Date: {self.date}')

class Vaccine:
        vaccine_name = ["sinovac, astrazeneca, moderna,pfizer"]


        def get_vaccine_name(self,index):
            return self.vaccine_name[index+1]
        def get_all_vaccine_name(self):
            for x in self.vaccine_name:
                print(x)

class GetVaccineted:
    student = ""
    vaccineted = ""
    date = ""

    def add_vaccine(self,vaccine):
        self.vaccineted.append(vaccine)
    def add_date(self,date):
        self.date.append(date)
    def Vaccineted_detail(self):
        print(self.student.student_detail())

        for x in range(len(self.vaccineted)):
            print(f'\t {x+1} vaccine name: {self.vaccineted[x]} Date: {self.date[x]}')
