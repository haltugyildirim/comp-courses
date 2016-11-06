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
