
# class Student:
#     """Developed by Nilesh in python class"""
#     def __init__(self,name, age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#
#     def talk(self):
#         print("Hello myself", self.name)
#         print("my age is", self.age)
#         print("marks scored are",self.marks)
#
# s1=Student("Nilesh", 20, 99)
# s1.talk()


class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Name:{}\nRollNo:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

s1=Student("Nilesh",20,99)
s1.display()

s2=Student("Mansi",20,99)
s2.display()