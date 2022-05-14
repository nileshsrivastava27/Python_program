# print("Statement-1")
# x=10
# print(x)
#
# try:
#     print(x/0)
# except ZeroDivisionError:
#     print(x/2)
# print("statement2")
# print(x+10)
#
#
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("The exception is raised as", msg)
#
#

# try:
#     x=int(input("Enter any number:"))
#     y=int(input("Enter any number:"))
#     print(x/y)
#     print("Yeahhh Boiiii")
# except ZeroDivisionError:
#     print("Dvision by zero h mc zero se kyu krrha divide")
# except ValueError:
#     print("Dhang se daal na lawde values")

# try:
#     x=int(input("Enter any number"))
#     y=int(input("Enter any number"))
#     print(x/y)
# except (ZeroDivisionError,ArithmeticError,ValueError)as msg:
#     print("there is an error is the program and is",msg)
# except:
#     print("Default error, pls recheck the values")

import os
try:
    print("try")
    os._exit(0)
except NameError:
    print("except")
finally:
    print("Finally")