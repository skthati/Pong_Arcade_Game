from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_paddle()
        self.computer_paddle()

    def player_paddle(self):
        t = Turtle()
        t.speed(0)
        t.shape("triangle")
        t.color("white")
        t.pensize(15)
        t.hideturtle()
        t.penup()
        t.goto(-350, -30)
        t.pendown()
        t.setheading(270)
        t.forward(100)
    
    def computer_paddle(self):
        t = Turtle()
        t.speed(0)
        t.shape("triangle")
        t.color("white")
        t.pensize(15)
        t.hideturtle()
        t.penup()
        t.goto(350, 150)
        t.pendown()
        t.setheading(270)
        t.forward(100)