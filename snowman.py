import turtle
import random

# the screen 
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Snowman with Snowfall")
screen.tracer(0)

# set up the turtle to draw 
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

# def to draw a circle to use it in our build 
def draw_circle(t, radius, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# teh body 
draw_circle(pen, 60, 0, -150, "white")   # السفلي
draw_circle(pen, 45, 0, -40, "white")    # الأوسط
draw_circle(pen, 30, 0, 40, "white")     # الرأس

# eyes
draw_circle(pen, 3, -10, 75, "black")
draw_circle(pen, 3, 10, 75, "black")

# mouse (small circles )
mouth_positions = [(-12, 60), (-6, 57), (0, 56), (6, 57), (12, 60)]
for pos in mouth_positions:
    draw_circle(pen, 1.5, pos[0], pos[1], "black")

# nose 
pen.penup()
pen.goto(0, 65)
pen.pendown()
pen.color("orange")
pen.begin_fill()
pen.goto(20, 63)
pen.goto(0, 60)
pen.goto(0, 65)
pen.end_fill()

# the pens 
for y in [30, 10, -10]:
    draw_circle(pen, 3, 0, y, "black")

# the hat 
pen.penup()
pen.goto(-20, 95)
pen.pendown()
pen.color("black")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.right(90)
    pen.forward(10)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-15, 105)
pen.pendown()
pen.begin_fill()
for _ in range(2):
    pen.forward(30)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
pen.end_fill()

# color of the hands 
pen.color("brown")

# left hand 
pen.penup()
pen.goto(-30, -20)
pen.pendown()
pen.goto(-80, 20)

# right hand 
pen.penup()
pen.goto(30, -20)
pen.pendown()
pen.goto(80, 20)

# scarf
pen.penup()
pen.goto(-22, 42)
pen.pendown()
pen.color("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(44)
    pen.right(90)
    pen.forward(10)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(-5, 32)
pen.setheading(-90)
pen.pendown()
pen.begin_fill()
for _ in range(2):
    pen.forward(20)
    pen.right(90)
    pen.forward(10)
    pen.right(90)
pen.end_fill()

# falling snow 
snowflakes = []
for _ in range(70):
    flake = turtle.Turtle()
    flake.hideturtle()
    flake.shape("circle")
    flake.color("white")
    flake.penup()
    flake.speed(0)
    flake.goto(random.randint(-300, 300), random.randint(100, 300))
    flake.shapesize(0.1)
    flake.showturtle()
    snowflakes.append(flake)

# infinite snow move
def move_snow():
    for flake in snowflakes:
        y = flake.ycor()
        y -= random.uniform(1, 3)
        if y < -250:
            y = random.randint(200, 300)
            flake.setx(random.randint(-300, 300))
        flake.sety(y)

    screen.update()
    screen.ontimer(move_snow, 30)  # make a new ice every 30 seconds 

move_snow()  # start the move of the snow from here

turtle.done()
