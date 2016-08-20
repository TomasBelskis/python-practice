import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tomas!")

ln = turtle.Turtle()
ln.color("blue")
ln.pensize(3)

ln.forward(60)
ln.left(150)
ln.forward(50)

wn.exitonclick()