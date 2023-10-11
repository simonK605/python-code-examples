import turtle
import random

def draw_starry_night():
    # Create a turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create a turtle named "vincent" (inspired by Van Gogh)
    vincent = turtle.Turtle()
    vincent.speed(0)  # Set the turtle's drawing speed to the fastest

    # Function to draw a star
    def draw_star(x, y, size):
        vincent.penup()
        vincent.goto(x, y)
        vincent.pendown()
        vincent.color("white")
        vincent.begin_fill()
        for _ in range(5):
            vincent.forward(size)
            vincent.right(144)
        vincent.end_fill()

    # Draw stars
    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(1, 3)
        draw_star(x, y, size)

    # Draw swirling patterns
    vincent.color("yellow")
    vincent.width(2)

    for _ in range(36):
        vincent.forward(150)
        vincent.right(170)

    # Close the turtle graphics window when clicked
    screen.exitonclick()

# Run the draw_starry_night function
draw_starry_night()
