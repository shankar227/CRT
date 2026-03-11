a=int(input("enter a"))









'''
try:
    a =int(input("enter a"))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero")
except ValueError:
    print("Invalid input")
    '''
import pdb
def add(a,b):
    pdb.seet_trace()
    return a+b
a =int(input("enter a"))
b =int(input("enter b"))
print(add(a,b))
