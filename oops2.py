class Employee:
    no_of_employee=10

    def function_details(self):
        return f"Name is {self.name} , the salary is {self.salary} and the rollno is {self.rollno}"

    def __init__(self, aname, asalary, arollno):
        self.name=aname
        self.salary=asalary
        self.rollno=arollno

    @classmethod
    def change_leaves(cls,new_employee):
        cls.no_of_employee=new_employee


# harry=Employee()
# larry=Employee()
#
# harry.name="Nilesh"
# harry.salary=100000
# harry.rollno= 47
#
# larry.name="Sehul"
# larry.salary=99999
# larry.rollno=32
#
# print(harry.function_details())
# print(larry.function_details())
# print(larry.no_of_employee)

harry=Employee('Nilesh', 100000, 47)
print(harry.salary)
Employee.change_leaves(80)
print(harry.no_of_employee)