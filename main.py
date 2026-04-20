from turtle import *
import random

# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
# Creates the rectangular game boundary
def playing_area():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
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
def move_with_heading(t, turtles):
    t.forward(5)
    if t.xcor() > 250 or t.xcor() < -250:
        t.setheading(180 - t.heading())
        t.forward(10)
        turtles.append(new_turt())
    if t.ycor() > 250 or t.ycor() < -250:
        t.setheading(-t.heading())
        t.forward(10)
        turtles.append(new_turt())
    return turtles
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
def new_turt(): 
    tr = Turtle()
    tr.color(generate_color())
    tr.speed(0)
    tr.shape("circle")
    tr.setheading(random.randint(0,360))
    turtles.append(tr)
    return tr
def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.color("white")
    player.shape("turtle")
def up():
    global player
    player.setheading(90)
    player.forward(10)
def down():
    global player
    player.setheading(-90)
    player.forward(10)
def left():
    global player
    player.left(10)
    player.forward(10)
def right():
    global player
    player.right(10)
    player.forward(10)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.title("The Bouncing Ball")
screen.listen()
screen.onkey(create_player, "space")
screen.onkeypress(up, "w")
screen.onkeypress(left, "a")
screen.onkeypress(down, "s")
screen.onkeypress(right, "d")

playing_area()

player = None

t = Turtle()
t.color(generate_color())
t.speed(0)
t.shape("circle")
t.setheading(random.randint(0,360))
# deltax = random.randint(-2,2)
# deltay = random.randint(-2,2)

turtles = [t]


alive = True 

while alive:
    if player:
        move_with_heading(player,turtles)
    for obj in turtles:
        turtles = move_with_heading(obj,turtles)
        if player != None and player.distance(obj) < 20:
            obj.hideturtle()
            turtles.remove(obj)
        


screen.exitonclick()