import textwrap
from turtle import Turtle, Screen
from board1 import Board as b
from paddle1 import Paddle as p

sc = Screen()
sc.setup(width=830,  height=530)
sc.bgcolor("black")

# Register the paddle shape
shape = ((0, 0), (0, 10), (-100, 10), (-100, 0))
sc.register_shape("paddle", shape)


sc.listen()
sc.onkey(key="Up", fun=p.move_up)
sc.onkey(key="Down", fun=p.move_down)

# Draw the board
b.pong_board(sc)

# Position the paddles
p.player_paddle(sc)
p.computer_paddle(sc)


sc.exitonclick()
