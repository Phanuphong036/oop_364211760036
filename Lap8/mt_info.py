from Teacher import Teacher
from Student import Student

if __name__ == "__main__":
    t1 = Teacher("Puriwat Lertkrai","MT")
    s1 = Student("Phanuphong","MT","MIT")

    t1.introduce()
    s1.introduce()

    person = [t1,s1]

    for x in person:
        x.introduce()

