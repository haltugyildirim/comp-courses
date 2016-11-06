class Vehicle:
    def __init__(self, speed, maxSpeed):
        self .speed = speed
        self.maxSpeed = maxSpeed
        print("You have just created a vehicle.")

    def accelerate(self,x):
        self.speed = self.speed + x
        if(self.speed > self.maxSpeed):
            self.speed = self.maxSpeed

    def status(self):
        print("The speed of the vehicle is", self.speed, " km/h.")

class Motorcycle(Vehicle):
    #aditional attributes
    widthFrontTire = 95
    widthRearTire = 95

    def setWidthTires(self, front, rear):
        self.widthFrontTire = front
        self.widthRearTire = rear
        print("You have just put on some tires.")

    def printTireInfo(self):
        print("Width of front tire:", self.widthFrontTire, "mm.")
        print("Width of rear tire:", self.widthRearTire, "mm.")
'''
m = Motorcycle(0, 70)
m.status()
m.accelerate(50)
m.status()
m.accelerate(30)
m.status()
m.accelerate(-80)
m.status()
m.printTireInfo()
m.status()
m.setWidthTires(92,108)
m.printTireInfo()
'''

class Automobile(Vehicle):
    #attributes
    gear = 1
    color = 'blue'

    def setGear(self, gearnumber):
        self.gear = gearnumber
        print "You set to new gear"

    def setColor(self, colorcode):
        self.color = colorcode
        print "You set a new color"

    def getColor(self):
        print "The New Color is", self.color

    def status(self):
        print "The speed of the vehicle is", self.speed, " km/h."
        print "The gear number of the vehicle is ", self.gear

a = Automobile(0,150)
a.status()
a.accelerate(40)
a.setColor('red')
a.setGear(2)
a.status()
a.getColor()
