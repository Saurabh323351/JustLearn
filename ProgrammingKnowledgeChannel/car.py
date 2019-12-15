class Car:

    def __init__(self,speed,color):

        self.speed=speed
        self.color=color

    def set_speed(self,value):

        self.speed=value

    def get_speed(self):

        return self.speed


ford = Car(200,'red')
honda= Car(201,'redis')
audi = Car(202,'blue')

ford.set_speed(300)
print(ford.get_speed())


# honda.speed=220
# audi.speed=250
#
# ford.color = "red"
# honda.color = "blue"
# audi.color = "black"
#
# print(ford.speed)
# print(ford.color)
#
#
# ford.speed=300
# ford.color = "blue"
#
# print(ford.speed)
# print(ford.color)
#
# print(id(ford))