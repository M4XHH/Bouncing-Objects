from turtle import *
import random

# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
# Creates the rectangular game boundary
def playing_area():
    t = Turtle()
    t.speed(0)
    t.color("teal")
    t.penup()
    t.goto(250,250)
    t.pendown()
    t.begin_fill()
    t.goto(250,-250)
    t.goto(-250,-250)
    t.goto(-250,250)
    t.goto(250,250)
    t.end_fill()


def move_with_heading(t):
    t.forward(5)
    if t.xcor() > 250 or t.xcor() < -250:
        t.setheading(180 - t.heading())
        t.forward(10)
    if t.ycor() > 250 or t.ycor() < -250:
        t.setheading(-t.heading())
        t.forward(10)



# Function 2: Movement using delta x / delta y (coordinate-based movement)
def move_with_deltas(t, deltax, deltay):
    newx = t.xcor() + deltax
    newy = t.ycor() + deltay

    if newx > 250 or newx< -250:
        newx = t.xcor()
        deltax *=-1
    if newy > 250 or newy< -250:
        newy = t.ycor()
        deltay *=-1
    
    t.goto(newx,newy)
    return deltax, deltay 
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.title("The Bouncing Ball")

playing_area()

t = Turtle()
t.color(generate_color())
t.speed(0)
t.shape("circle")
t.setheading(random.randint(0,360))
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)




alive = True 

while alive:
    deltax,deltay = move_with_deltas(t,deltax,deltay)


screen.exitonclick()