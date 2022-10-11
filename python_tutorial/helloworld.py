from ast import main
from fnmatch import fnmatch
from mimetypes import init
import numpy as np

def hello_world():
    print("hello world")
    return 'hello world'


x = hello_world()

print(x, type(x))

# birth_year = input("Enter birth year: ")
# print(birth_year)

class HelloWorld:
    
    def __init__(self, fn, ln):
        # super(HelloWorld, self).__init__(*args, **kwargs)
        self.fn = fn
        self.ln = ln
    
    n = 5
    
class Yes:
    
    def __init__(self, *args, **kwargs):
        self.a = "a"
        self.b = "b"
        super(Yes, self).__init__(*args, **kwargs)
        
x = Yes()
print(x.__dict__)        

    
n = HelloWorld("Tony", "Guo")
print(n.n, n.fn, n.ln)

  
class Person:
    
    
    def __init__(self, name, age):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        self.age = age
        self.name = name
    def printnameage(self):
        print(self.name, self.age)
    
x = Person("Tony Guo", 24)
x = Person("Calvin", "25")
x.printnameage()
    
class HR(Person):
    
    def __init__(self, name, age, experiencelevel):
        super().__init__(name, age)
        self.experiencelevel = experiencelevel
    
    def printeverything(self):
        print(f"hi {self.name} of age {self.age} with experience level: {self.experiencelevel}")

y = HR("Na Thao", 23, "Associate")
y.printnameage()
y.printeverything()

