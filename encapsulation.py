"""#Class creation
class myClass:
    #private variable
    __privateVar = 27;
    #private mathod
    def __privMeth(self):
        print("I'm inside class myClass")
    #Function to print value of private variable
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)

# Object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth()"""

"""#2.Computer price
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using the setter function
c.setMaxPrice(2000)
c.sell()"""

#3.point
# Create class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Metod to print points in coordinate format
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
# Create Object
p1 = Point(2, 3)
print(p1)