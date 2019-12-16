from polygon import Polygon
from shape import Shape

class Rectangle(Polygon,Shape):
    """
    Here Rectangle is inheriting Polygon class,In case of Inheritance ,there is always a relationship
    between child (subclass) and parent(Super class) called as IS-A relationship
    In this case ,Rectangle Is A Polygon, IS-A relationship is there between Polygon and Rectangle

    Here we are doing multiple inheritance means child having more than one parent
    as Rectangle IS-A Shape also
    """
    def area(self):

        return self.get_height() * self.get_width()
