from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1


    def move(self):
        x_cor = self.xcor() + self.x_change
        y_cor = self.ycor() + self.y_change
        self.goto(x=x_cor, y=y_cor)
    

    def bounce_y(self):
        self.y_change *= -1


    def bounce_x(self):
        self.x_change *= -1


    def restart(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1


    def increase_speed(self):
        self.move_speed *= 0.9
