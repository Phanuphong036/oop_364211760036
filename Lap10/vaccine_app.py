from Lap10.Model import Person,Student,Vaccine,GetVaccineted

std_name = input("Enter student name:")
std_age = input("Enter student age:")
std_weight = input("Enter student weight:")
std_major = input("Enter student major:")
std_vaccine = input("Enter student vaccine:")
std_date = input("Enter student date:")

std1 = Student(std_name,std_age,std_weight,std_major,std_vaccine,std_date)
print(std1.student_detail())

v = Vaccine()

std1_vaccine = GetVaccineted()
std1_vaccine.student = std1



#1
#std1_vaccine.add_vaccine(v.vaccine_name[0])
#std1_vaccine.add_date("1/1/2566")
#2
#std1_vaccine.add_vaccine(v.vaccine_name[0])
#std1_vaccine.add_date("1/3/2566")

std1_vaccine.Vaccineted_detail()

