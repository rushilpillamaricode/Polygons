from turtle import Turtle
import random 

t = Turtle()
colors = "yellow,gold,orange,red,maroon,violet,magenta,purple,navy,blue,skyblue,cyan,turquoise,lightgreen,green,darkgreen,chocolate,brown,black,gray".split(",")
t.width(5)
for i in range(3,11):
    color = random.choice(colors)
    t.color(color)
    for j in range(i):        
        t.forward(100)
        t.right(360/i)