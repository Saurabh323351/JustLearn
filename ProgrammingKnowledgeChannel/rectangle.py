class Rectangle:

    def __init__(self,height,width):
        self.height=height
        self.width=width


rect1 = Rectangle(20,60)
rect2 = Rectangle(20,70)

rect1.height=20
rect2.height=30

rect1.width=40
rect2.width=10


print(rect1.height * rect1.width)
print(rect2.height * rect2.width)

