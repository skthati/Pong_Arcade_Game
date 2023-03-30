from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.pong_board()



    def pong_board(self):
        t = Turtle()
        t.speed(0)
        t.shape("triangle")
        t.hideturtle()
        t.penup()
        t.goto(-405, 255)
        t.pensize(10)
        t.pendown()
        t.color("white")
        t.begin_fill()

        for i in range(2):
            t.forward(800)
            t.right(90)
            t.forward(500)
            t.right(90)

        t.penup()
        t.goto(0, 250)
        t.pendown()
        t.setheading(270)
        t.forward(490)