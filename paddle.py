from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, x_axis):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.color("white")
        self.teleport(x=x_axis, y=0)


    def move_paddle_up(self):
        self.forward(20)
    

    def move_paddle_down(self):
        self.backward(20)
