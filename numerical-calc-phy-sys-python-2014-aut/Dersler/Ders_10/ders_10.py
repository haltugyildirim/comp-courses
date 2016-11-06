'''
class Person:
    # attributes (properties)
    name = "No name yet"
    age = 0

    # methods
    def setName(self, x):
        self.name = x
    
    def setAge(self, x):
        self.age = x

    def talk(self):
        print("Hi! My name is", self.name, "and I am", self.age, "years old.")

myObject = Person()
myObject.setName("Peter")
myObject.setAge(22)
myObject.talk()
'''

'''
#Quiz 6
class Car:
    #attributes
    maxSpeed = "200 km/h"
    brand = "Anadol"

    #methods
    def setBrand(self, x):
        self.brand = x

    def setMaxSpeed(self, x):
        self.maxSpeed = x

    def printData(self):
        print "an", self.brand, "with maximum speed", self.maxSpeed,"."

#calling the object
myObject = Car()
myObject.setBrand("Audi")
myObject.setMaxSpeed("300 km/h")
myObject.printData()
'''

'''
class Person2:
    #attributes
    name = "No name yet"
    age = 0

    #methods
    def __init__(self,x,y):
        self.name = x
        self.age = y
        print "You have just created a Person Object."

    def talk(self):
        print "Hi! My name is", self.name, "and I am", self.age, "years old."

p = Person2("Sandy", "34")
p.talk()
'''

'''
class Person2:
    #attributes
    name = "No name yet"
    age = 0
    food = "No favorite food yet"
    music = "No favorite music yet"

    #methods
    def __init__(self,x,y):
        self.name = x
        self.age = y
        print "You have just created a Person Object."

    def talk(self):
        print "Hi! My name is", self.name, "and I am", self.age, "years old."

    def setFoodAndMusic(self, x,y):
        self.food = x
        self.music = y

    def tellMore(self):
        print("I like eating", self.food, "and I love listening to", self.music)

q = Person2("Sandy", "34")
q.setFoodAndMusic("TOFU BEEF","BLACK METAL")
q.talk()
q.tellMore()
'''

'''
class Car:
    #attributes
    maxSpeed = "200 km/h"
    brand = "Anadol"

    #methods
    def __init__(self,x,y):
        self.brand = x
        self.maxSpeed = y

    def printData(self):
        print "an", self.brand, "with maximum speed", self.maxSpeed,"."

#calling the object
q = Car("Audi", "100000 km/h")
q.printData()
'''

'''
class Fruit:
    #method
    def __init__(self,name,color,flavor):
        #set values for attributes
        self.name = name 
        self.color = color
        self.flavor = flavor
        print "The", self.name, "is", self.color, "and taste",self.flavor, "."

first = Fruit("strawberry", "red", "sweet")
second = Fruit("lemon", "yellow", "sour")
'''

