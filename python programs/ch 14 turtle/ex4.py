import turtle
import math
# Setup
s = turtle.Screen()
s.setup(width=600, height=400)
s.bgcolor("white")

# Turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t.speed(2)
t.color("yellow")
t.width(25)
t1.speed(2)
t1.color("blue")
t1.width(25)
t2.speed(2)
t2.color("red")
t2.width(25)

# Draw the "G"
t.circle(100,50)
t1.circle(100,-120)
t2.circle(100, 80)




# Hide the turtle
t.hideturtle()

# Keep window open
s.mainloop()





