from turtle import Turtle, Screen
import main1

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_paddle
        self.computer_paddle

    
    def create_paddle(self):
        t = Turtle()
        t.shape("paddle")
        t.speed(0)
        t.penup()
  
    
    def player_paddle(self):
        plp = self.create_paddle(Screen)
        plp.color("yellow")
    
    def computer_paddle(self):
        cpp = self.create_paddle()
        cpp.color("red")
    
    def move_up():
        # self.sety(padd.ycor() - 20)
        pass


    def move_down():
        # padd.sety(padd.ycor() + 20)
        pass

