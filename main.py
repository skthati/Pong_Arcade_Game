from turtle import Turtle, Screen
from paddle import Paddle

# Screen setup
sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")

# Stop animation
sc.tracer(0)


#  Paddle shape
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.speed(0)
paddle.goto(-350, 0)

# Paddle movement

def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

sc.listen()

sc.onkey(move_up, "Up")
sc.onkey(move_down, "Down")

# Game loop

start_game = True

while start_game:
    sc.update()


sc.exitonclick()