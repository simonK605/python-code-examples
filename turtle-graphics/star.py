import turtle

star = turtle.Turtle()
star.speed(50)

star.color("red")

for i in range(80):
    star.forward(300)
    star.left(168.5)

turtle.done()