from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

# Screen setup
sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")

# Stop animation
sc.tracer(0)

# Create turtles for left and right paddles from class

l_paddle = Paddle((-350, 0), "blue", "square")
r_paddle = Paddle((350, 0), "red", "square")

#Create turtles for left and right Score Board

l_score = Scoreboard((-100, 230))
r_score = Scoreboard((100, 230))


# Paddle movement using "Up", "Down", "w", "s" keys

sc.listen()

# Right Paddle
sc.onkey(r_paddle.move_up, "Up")
sc.onkey(r_paddle.move_down, "Down")

# Left Paddle
sc.onkey(l_paddle.move_up, "w")
sc.onkey(l_paddle.move_down, "s")

# Ball and Ball Movement

ball = Ball()

# Game loop

start_game = True

while start_game:
    # ball.ball_speed controls the speed of the ball and increases everytime paddle hits and resets to 0.1 if paddle misses.
    time.sleep(ball.ball_speed)
    sc.update()

    # Check collision with top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # check collision with left and right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # check if paddle misses the ball
    if ball.xcor() > 370:
        ball.bounce_x()
        ball.goto(0, 0)
        l_score.left_score()
        ball.ball_speed = 0.1
    
    if ball.xcor() < -370:
        ball.bounce_x()
        ball.goto(0, 0)
        r_score.right_score()
        ball.ball_speed = 0.1


    ball.move()

sc.exitonclick()