import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")

t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

a = 0

for i in range(300):
    t.forward(a)
    t.right(random.randint(80, 160)) 
    a += 2  

t.hideturtle()
turtle.done()
