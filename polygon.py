import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")

t = turtle.Turtle()
t.speed(3)

# --------- EQUILATERAL TRIANGLE ---------
t.penup()
t.goto(-100, 0)
t.pendown()

t.fillcolor("blue")
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# --------- RECTANGLE ---------
t.penup()
t.goto(100, 0)
t.pendown()

t.fillcolor("orange")
t.begin_fill()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

# Finish
t.hideturtle()
turtle.done()




