class Employee:
    no_of_leaves=8
    pass

harry= Employee()
larry= Employee()

harry.name="Nilesh"
harry.std=14
harry.rollno=47

larry.name= "Sehul"
larry.std=15
larry.rollno=32

Employee.no_of_leaves=9

larry.no_of_leaves=1
harry.no_of_leaves=10
print(larry.__dict__)
print(harry.__dict__)
print(larry.no_of_leaves)
print(harry.name, larry.std, harry.no_of_leaves)
print(Employee.__dict__)

