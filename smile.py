import turtle
smile = turtle.Turtle()
smile.up()
smile.goto(0, -100)
smile.down()

#background of smile
smile.begin_fill()
smile.fillcolor("yellow")
smile.circle(100)
smile.end_fill()

#lips of smile
smile.up()
smile.goto(-67, -40)
smile.setheading(-60)
smile.width(5)
smile.down()
smile.circle(80, 120)
smile.fillcolor("black")

for i in range(-35, 105, 70):
    smile.up()
    smile.goto(i, 35)
    smile.setheading(0)
    smile.down()
    smile.begin_fill()
    smile.circle(10)
    smile.end_fill()

smile.hideturtle()