from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

# Screen setup
sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")

# Stop animation
sc.tracer(0)

# Create turtle from class

l_paddle = Paddle((-350, 0), "blue", "square")
r_paddle = Paddle((350, 0), "red", "square")
ball = Paddle((0, 0), "white", "circle")

# Paddle movement

sc.listen()

# Right Paddle
sc.onkey(r_paddle.move_up, "Up")
sc.onkey(r_paddle.move_down, "Down")

# Left Paddle
sc.onkey(l_paddle.move_up, "w")
sc.onkey(l_paddle.move_down, "s")

# Ball movement

ball.dx = 2
ball.dy = 2

# Game loop

start_game = True

while start_game:
    sc.update()
    ball.dx += 2
    ball.dy += 2
    ball.goto(ball.dx, ball.dy)


sc.exitonclick()