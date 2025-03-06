from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.start_score()
        self.draw_middle_line()
        

    def start_score(self):
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def draw_middle_line(self):
        self.teleport(x=0, y=-300)
        self.setheading(90)
        self.pensize(5)
        for _ in range(16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


    def update_score(self):
        self.clear()
        self.goto(-50, 250)
        self.write(arg=self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(50, 250)
        self.write(arg=self.r_score, align="center", font=("Courier", 30, "normal"))
        self.draw_middle_line()
