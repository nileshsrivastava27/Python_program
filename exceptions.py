class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("ENter your age:"))
if age>60:
    raise TooOldException('Your age is already crossed the marriage age')
elif age<18:
    raise TooYoungException('Your age is not sufficient for marriage... wait for time to come')
else:
    print("you will get the details via email")
