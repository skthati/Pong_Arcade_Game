from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# shape = ((-100, 0), (0, 0), (0, 10), (-100, 10))
shape = ((0, 0), (0, 10), (-100, 10), (-100, 0))
screen.register_shape("paddle", shape)

def move_up():
    padd.sety(padd.ycor() - 20)


def move_down():
    padd.sety(padd.ycor() + 20)

screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)

padd = Turtle()
padd.color("blue")
padd.shape("paddle")

# padd.shapesize(stretch_wid=5, stretch_len=1)

padd.setheading(0)
padd.forward(100)
screen.exitonclick()


