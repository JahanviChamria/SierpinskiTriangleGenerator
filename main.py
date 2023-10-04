from turtle import Turtle, Screen
import random

screen=Screen()
screen.title("Chaos Game Sierpinski Triangle Generator")
screen.bgcolor("black")

VER=[[-200,-100],[0,200],[200,-100]]
t=Turtle()
t.speed("fastest")
t.penup()
ansx=screen.textinput(title=f"Starting Parameters", prompt="Enter the starting x coordinate: ")
x=int(ansx.title())
ansy=screen.textinput(title=f"Starting Parameters", prompt="Enter the starting y coordinate: ")
y=int(ansy.title())
ansn=screen.textinput(title=f"Starting Parameters", prompt="Enter the number of iterations: ")
ansnt=ansn.title()
ansc=screen.textinput(title=f"Starting Parameters", prompt="Enter the colour: ")
c=ansc.title()
t.goto(x,y)
t.pencolor(c)
if ansx=="Exit":
    exit(1)
else:
    t.hideturtle()
    for i in range(int(ansnt)):
        ch=random.choice(VER)
        midx=(x+ch[0])/2
        midy = (y + ch[1]) / 2
        t.goto(midx,midy)
        t.dot(4, c)
        x=midx
        y=midy

screen.exitonclick()



