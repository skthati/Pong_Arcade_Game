from turtle import Screen
from board import Board as b
from paddle import Paddle as p


sc = Screen()
sc.setup(width=830,  height=530)
sc.bgcolor("black")

# Draw the board
b.pong_board(sc)

# Position the paddles
p.player_paddle(sc)
p.computer_paddle(sc)



    
sc.exitonclick()
