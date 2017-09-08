import turtle
import random

c = turtle.Canvas()

gang = []
for x in range(5):
    t = turtle.Turtle()
    t.shape("turtle")
    gang.append(t)

# change all the turtles' color

for tina in gang:
    tina.color("Blue")

# move all the turtles to a random spot

for tina in gang:
    tina.penup()
    tina.goto(random.randint (-200, 200), random.randint (-200, 200))

# EXTRA: make all of the turtles with an even index write a message

for x in gang:
    t = turtle.Turtle()
    if x%2 == 0:
        t.write("Hello", move = False, align = "center", font = ("Arial", 25, "normal"))



input("Press enter to quit")