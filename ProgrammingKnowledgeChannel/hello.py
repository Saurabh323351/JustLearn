class Hello:

    def __init__(self):

        self.a=10
        self._b=20

        """ " _ " (underscore) it is just a convention to denote private variable but actually it does not 
            make its variable private ,we can easily access it from outside using object of
            class 
            
        """

        self.__c=30 # Private variable
        """
        double underscore actually makes variable private ,we can not access it from outside of class
        """



hello = Hello()

print(hello.a)
print(hello._b)
print(hello._c)