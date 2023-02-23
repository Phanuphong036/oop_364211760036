
# employee app
from employee import Employee

if __name__ == "__main__":

    employee_list = []
    x = int(input("Enter your number of employee"))
    for i in range(x):
        print(f'employee {i + 1}')
        n = input("Enter employee name: ")
        pos = input("Enter employee position: ")
        __s = input("Enter employee __salary: ")

        std = Employee (n,pos,__s)
        employee_list.append(std)
        print(f'employee {i + 1} had been saved.')

    print("Display all employee info: ")
    for x in employee_list:
        x.employee_info()