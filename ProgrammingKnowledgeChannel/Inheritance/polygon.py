class Polygon:
    """
    whenever any class extends Polygon class then private variable and method will not be available
    for child class ,so in order to allow access of private variable to child class ,we need to have
    setter and getter for those variables
    """

    __width=None
    __height=None

    def set_values(self,width,height):

        self.__width=width
        self.__height=height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height




