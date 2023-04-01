from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position, color, shape ):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.speed(0)
        self.goto(position)
        self.ball_shape_size(shape)
    
    def ball_shape_size(self, shape):
        if shape == "square":
            self.shapesize(stretch_wid=5, stretch_len=1)
            
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        
        