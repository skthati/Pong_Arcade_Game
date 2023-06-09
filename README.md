
<a name="readme-top"></a>


<div align="center">
<!-- Title: -->
<h1><a href="https://github.com/skthati/Pong_Arcade_Game/">Pong Game</a> - Python Turtle </h1>
</div>

<!-- Table of contents -->
<hr>
<hr>
<ol>
    <li><a href="#pong-game">Pong Game</a></li>
    <li><a href="#basics">Basics</a> </li>
</ol>
<hr>
<hr>


 <!--Pong Game  -->
## Pong Game <a name="pong-game"></a>
Very famous Pong game.

Ball speed increases on every successful paddle hit.

Ball speed resets, if a paddle misses the ball.

Each side gets a score, if other side paddle misses the ball.

Game rules.

* Use "Up" or "Down" keys to control right paddle.
* Use "w" or "s" keys to control left paddle.


Output

![Pong Game ](images/working_pong_game.gif)

Game files.

[main.py](main.py)

[paddle.py](paddle.py)

[ball.py](paddle.py)

[score_board](score_board.py)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  

<!-- Bloopers   -->
## Bloopers <a name="bloopers"></a>
Some blooper gifs.

Paddle drawing lines.
![Alt text](Not%20working/Images/moving_paddle.gif)

Ball starts from random place and flies off.

![Alt text](images/ball_movement.gif)

This shows paddle creation and also paddle moving to its position. Also paddle going out of screen.

![Alt text](images/paddle_movement.gif)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  


<!-- Pong Game -->
## Pong Game Screen Setup <a name="pong_game_screen"></a>
Famous arcade game.

Screen setup
```Python
from turtle import Turtle, Screen

sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")

sc.exitonclick()
```

![Alt text](images/paddle.png)

### Create paddle shape

```Python
#  Paddle shape
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
```

### Paddle movement

```Python
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
```
![Alt text](images/paddle_movement.gif)

    
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  

## Paddle Class <a name="paddle_class"></a>
Move all code to paddle class.


[paddle.py](paddle.py)

```Python
from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(position)
```

[main.py](main.py)

```Python
from paddle import Paddle

# Create turtle from class

l_paddle = Paddle((-350, 0), "blue")
r_paddle = Paddle((350, 0), "red")
```

Left paddle move with "w" and "s" keys

```Python
# Left Paddle
sc.onkey(l_paddle.move_up, "w")
sc.onkey(l_paddle.move_down, "s")
```

Right paddle moce with "Up" and "Down" keys

```Python
# Right Paddle
sc.onkey(r_paddle.move_up, "Up")
sc.onkey(r_paddle.move_down, "Down")
```


<!-- 

Test1  
## Test <a name="test"></a>
Test Test

1. Code
    ```Python
    sc.onkey(key="Up", fun=up_move)
    sc.onkey(key="Right", fun=right_move)
    sc.onkey(key="Left", fun=left_move)
    sc.onkey(key="Down", fun=down_move)
    ```

2. Output

    ![Alt text](images/snake_working.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  


-->

 
