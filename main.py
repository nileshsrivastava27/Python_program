# s1 = input()
# n = int(input())
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# s2 = ''
#
# for x in s1:
#     s2 += alpha[((alpha.index(x) + n)%25)]
#
# print(s2)



class Book:
    def __init__(self,pages):
        self.pages=pages

    def add(self,others):
        return self.pages+others.pages

b1=Book(100)
b2=Book(200)

print("hello",b1+b2)