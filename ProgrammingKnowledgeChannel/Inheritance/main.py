from rectangle import Rectangle
from triangle import Triangle

rect=Rectangle()
rect.set_values(20,10)
area=rect.area()
rect.set_color("red")
r_color=rect.get_color()
print(area,r_color)

tri=Triangle()
tri.set_values(20,15)
area=tri.area()

tri.set_color("blue")
t_color=tri.get_color()
print(area,t_color)
