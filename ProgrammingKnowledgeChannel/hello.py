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
# print(hello.__c) # will get error
                    #AttributeError: 'Hello' object has no attribute '_c'



class Parent:

    def add(self):
        print('add')

    def __init__(self,name):
        print(id(self),'--->parent')
        print('parent __init__',name)

class Parent2:

    def add(self):
        print('add2')

    def __init__(self,name):
        print(id(self),'--->parent2')
        print('parent2 __init__',name)

class Child(Parent,Parent2):

    def __init__(self):
        print('child __init__')
        proxy_obj=super()

        super().__init__("saurabh try to call parent init method using super() method that actually gives proxy object\
        By using that proxy object ,child is used to call parent method")

        print(id(proxy_obj),id(self))
        proxy_obj.add()

        """
        Another way to call parent init methods below 
        """
        Parent2.__init__(self,"rajat")
        Parent.__init__(self,"saurabh2")

        Parent2.add(self)
child=Child()

print(Child.__mro__) # means method resolution order
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)
# first child will execute then parent will execute


"""
composition example is given below
define: delegating your responsibility to other class is called composition

here there is no IS-A relationship between Employee and Salary class so we can not go for 
inheritance ,because Every Employee salary is actually different 
but we Employee class does not want to calculate salary ,it want to delegate responsibility 
of calculating salary to Salary class ,this is nothing but composition
Here Employee act as Container and Salary act as content

Here Employee class is delegating some part of responsibility to Salary class i.e composition
In Composition ,the relationship between classes which have some association is represented by a keyword
 part-of 
 
 Salary is a part-of Employee
 
 difference points : 
        1) here association is denoted by keyword part-of
        2)when we delete Employee object then Salary is automatically deleted
        3)Salary object is dependent on Employee class
        4)here Salary object and Class object are inter-dependent of each other

"""

class Salary:

    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:

    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)

    def total_salary(self):

        return self.obj_salary.annual_salary()

emp=Employee('saurabh',23,80000,30000)
print(emp.total_salary())



"""
Abstract class started
abc -> abstract base class
"""
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):pass

    @abstractmethod
    def perimeter(self):pass

class Square(Shape):

    def __init__(self,side):
        self.__side=side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):

        return 4 * self.__side

square=Square(10)
area=square.area()
per=square.perimeter()
print(area)
print(per)

