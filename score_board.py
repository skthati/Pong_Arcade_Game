from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(position)
        self.lscore = 0
        self.rscore = 0
        self.write(f"{self.lscore}", align="center", font=("Arial", 40, "normal"))
        self.write(f"{self.rscore}", align="center", font=("Arial", 40, "normal"))
    
    
    def left_score(self):
        self.lscore += 1
        self.clear()
        self.write(f"{self.lscore}", align="center", font=("Arial", 40, "normal"))
        
        
    def right_score(self):
        self.rscore += 1
        self.clear()
        self.write(f"{self.rscore}", align="center", font=("Arial", 40, "normal"))
    
        
    def reset_score(self):
        self.lscore = 0
        self.rscore = 0
        self.clear()
        self.write(f"{self.lscore}", align="center", font=("Arial", 40, "normal"))
        self.write(f"{self.rscore}", align="center", font=("Arial", 40, "normal"))
    


    

    

