# fname = "Tony"
# lname = "Stark"
# age = "51"
#
# print("Ironman is "+fname+" "+lname)
# print(fname+"'s"+" age is "+age)
# print("Tony Stark is a genius")
#
# # name = input("What is your name?? ")
# # print(name)
# #
# # superhero= input("What is your superhero name??")
# # print(superhero)
#
# old_age = input("Enter your age")
# new_age = int(old_age)+2
# print(new_age)


# first = input("Enter the first number to be added :")
# second = input("Enter the second number to be added :")
#
# sum= int(first)+int(second)
# print(sum)
#
# print("The sum of two numbers are : "+ str(sum))
#
# name = "Tony Stark"
# print(name.upper())
# print(name.find('S'))
# print(name.replace("Tony Stark", "Iron Man"))
# print('T' in name)
# print('Iron man' in name)
#
# print(3<2)
# print(3==2)
# print(3!=2)
# print(not 2 < 3)



        #MAKING A PYTHON CALCULATOR

# first= input("Enter first number :")
# second= input("Enter second number :")
# first= int(first)
# second= int(second)
#
# operator= input("Enter operator (+,-*,/,%) :")
#
# if operator == "+":
#     print(first + second)
# elif operator == "-":
#     print(first - second)
# elif operator == "*":
#     print(first * second)
# elif operator == "/":
#     print(first / second)
# elif operator == "%":
#     print(first % second)
# else:
#     print("NOT a Valid Operation")


#
# numbers=range(5)
# print(numbers)



#
# i=10
# while i>1:
#     print(i*"Nilesh")
#     i=i-1

#
# for i in range(6):
#     print(i)


# marks=[98,97,96]
# print(marks[1:3])
#
# for score in marks:
#     print(marks)

#
# def f1(*s,n1):
#     for s1 in s:
#         print(s1)
#     print(n1)
#
# f1("A","B",n1=10)
#


# a=  int(input("Enter a number"))
# b= int(input("enter a number"))
# min=a if a<b else b
# print("minimum value is :", min)

s=input("Enter a string")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)
