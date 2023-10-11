import turtle

stars = turtle.Turtle()
stars.speed(40)
stars.getscreen().bgcolor("black")
stars.color("white")

def star(turtle, size):
    if size < 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

star(stars, 300)

turtle.done()
