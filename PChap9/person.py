

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName():
        return self.name
    
    def getAge():
        return self.age
    
    def setAge(self,age):
        self.age = age
        print("Age updated")

    def setName(self,name):
        self.name = name
        print("Name Updated")

    def __str__(self):
        return (f"{self.name} is my name and I am {self.age} years old")
    


Steven = Person("Steven",40)
x = str(Steven)
print(x)
