import turtle

batman = turtle.Turtle()

batman.turtlesize(1, 1, 1)
batman.pensize(3)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("BATMAN")

batman.color("yellow", "white")

batman.begin_fill()

batman.left(90)
batman.circle(50, 85)
batman.circle(15, 110)
batman.right(180) 

batman.circle(30, 150)
batman.right(5)
batman.forward(10)

batman.right(90)
batman.circle(-70, 140)
batman.forward(40)
batman.right(110)

batman.circle(100, 30)
batman.circle(30, 100)
batman.left(50)
batman.forward(50)
batman.right(145)

batman.forward(30)
batman.left(55)
batman.forward(10)

batman.forward(10)
batman.left(55)
batman.forward(30)

batman.right(145)
batman.forward(50)
batman.left(50)
batman.circle(30, 100)
batman.circle(100, 30)

batman.right(90)
batman.right(20)
batman.forward(40)
batman.circle(-70, 140)

batman.right(90)
batman.forward(10)
batman.right(5)
batman.circle(30, 150)

batman.left(180)
batman.circle(15, 110)
batman.circle(50, 85)


batman.end_fill()
turtle.done()