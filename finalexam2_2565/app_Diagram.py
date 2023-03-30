from finalexam2_2565.Diagram import Person,Student,Employee,Devices,Tablet,Laptop,Mobile

std_name = input("Enter student name:")
std_age = input("Enter student age:")
std_gmail = input("Enter student gmail:")
std_brand = input("Enter student brand:")
std_model = input("Enter student model:")
std_price = input("Enter student price:")
#std_major = input("Enter student major:")
#std_vaccine = input("Enter student vaccine:")
#std_date = input("Enter student date:")

std1 = Student(std_name,std_age,std_gmail,std_brand,std_model,std_price)
print(std1.student_detail())

D = Devices()

std1_Devices = Devices()
std1_Devices.student = std1
