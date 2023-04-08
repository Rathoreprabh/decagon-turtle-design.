import turtle
import random

# Create a Turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Set the starting position of the turtle
x = 0
y = 0
t.penup()
t.goto(x, y)
t.pendown()

# Set the number of sides of the Decagon
sides = 10

# Set the size of the Decagon
size = 100

# Set the number of repetitions
repetitions = 120

# Set the colors
colors = ["red", "orange", "brown", "green", "blue", "purple"]

# Draw the design
for i in range(repetitions):
    t.color(random.choice(colors))
    for j in range(sides):
        t.forward(size)
        t.right(360 / sides)
    t.right(360 / repetitions)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is manually closed
turtle.done()
