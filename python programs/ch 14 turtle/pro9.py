import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()

pen.color("red")

for x in range(1, 6):
    # angles eg 360-288=72
    print(pen.heading())
    pen.backward(200)
    pen.left(144)

turtle.done()