import math


class Circle:

    def __init__(self,radius):
        self.__radius=radius

    def setRadius(self,radius):

        self.__radius=radius

    def getRadius(self):

        return self.__radius

    def area(self):

        return math.pi * self.__radius ** 2

    def __str__(self):

        return "Circle Area => " + str(self.area())
    def __add__(self, circle_object):

        print(id(self),'--->address<--',id(circle_object))
        print(self.__radius,circle_object.__radius)
        return Circle(self.__radius + circle_object.__radius)

    def __lt__(self,circle_object):
        return self.__radius < circle_object.__radius

    def __gt__(self,circle_object):
        return self.__radius > circle_object.__radius

c1 = Circle(10)
c2 = Circle(11)
c3 = Circle(2)
c4=c1+ c2+c3

 # __add__ overloaded
print(c1.area(),c1.area(),c3.area())
print(c1.getRadius())
print(c2.getRadius())
print(c3.getRadius())
print(c4.getRadius())

# __lt__ and __gt__ overloaded

print(c1>c2)
print(c1<c2)
print(c3>c2)
print(c4>c2)

print(dir(c1))
# ['_Circle__radius', '__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'getRadius', 'setRadius']
#all these methods we can implement in our class

print(c1)