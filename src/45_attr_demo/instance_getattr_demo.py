class Student:
    student_id=""
    student_name=""

    # initial constructor to set the values
    def __init__(self):
        self.student_id = "101"
        self.student_name = "Adam Lam"

student = Student()
# using default value option
print('Using default value : Cgpa of the student is =', getattr(student, "student_cgpa", 3.00))
# without using default value
try:
    print('Without default value : Cgpa of the student is =', getattr(student, "student_cgpa",1))
except AttributeError:
    print("Attribute is not found :(")


