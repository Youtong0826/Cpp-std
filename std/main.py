from type import *

class cout:
    def __lshift__(self, value):
        print(value, end="")
        return value

class cin:
    def __rshift__(self, var: variable):
        var.value = input()

class endl:
    def __str__(self) -> str:
        return str("\n")

    def __lshift__(self, var):
        print(var, end="")
        return str("\n" + var)

class std:
    cout = cout()
    cin = cin()
    endl = endl()