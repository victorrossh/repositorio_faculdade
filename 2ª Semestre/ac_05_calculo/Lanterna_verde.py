import turtle as lant
lant.title("Lanterna Verde")
lant.bgcolor("green")

lant.color("white")
lant.begin_fill()
lant.circle(150)
lant.end_fill()

lant.setposition(-100, 50)

lant.begin_fill()
lant.color("green")

lant.forward(200)
lant.left(90)
lant.forward(30)
lant.left(90)
lant.forward(200)
lant.left(90)
lant.forward(30)
lant.left(90)

lant.end_fill()
lant.penup()

lant.begin_fill()
lant.circle(0)
lant.setposition(-100, 220)
lant.color("green")

lant.forward(200)
lant.left(90)
lant.forward(30)
lant.left(90)
lant.forward(200)
lant.left(90)
lant.forward(30)
lant.left(90)

lant.end_fill()

lant.setposition(0, 70)
lant.color("green")
lant.begin_fill()
lant.circle(80)
lant.end_fill()
lant.left(82)
lant.color("green")
lant.fd(20)
lant.color("black")
lant.rt(80)

lant.color("white")
lant.begin_fill()
lant.setposition(0, 100)
lant.circle(47)
lant.end_fill()

lant.hideturtle()
lant.done()
