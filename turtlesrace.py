from turtle import Screen, Turtle, textinput
import random

scr = Screen()
scr.bgcolor("black")
scr.setup(width=600, height=600)
colour= ["pink", "yellow", "green", "blue", "purple", "red"]
turtle_position= [100,60,20,-20,-60,-100]
all_turtles = []

def rand_walk():
    walk = random.randint(0, 10)
    return walk

for _ in range(6):
    turtle= Turtle("turtle")
    turtle.color(colour[_])
    turtle.penup()
    turtle.goto(-280, turtle_position[_])
    all_turtles.append(turtle)

race_over= True

user = textinput(title="What do you think🙄??", prompt= f"which turtle will win\n{colour}\nEnter the colour: ").lower()

if user:
    race_over= False

while not race_over:

    for turt in all_turtles:
        turt.forward(rand_walk())
        
        if turt.xcor() > 270:
            race_over= True
            win = turt.pencolor()

if win == user:
    print(f"you win! the {win} turtle won ")
else:
    print(f"u loose! you've think of {user} turtle but, the {win} turtle won")