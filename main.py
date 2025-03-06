from turtle import Screen
from paddle import Paddle
from field import Field
from ball import Ball
import time


#Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

#Initializing all the objects
field = Field()

paddle_left = Paddle(-350)
paddle_right = Paddle(350)

ball = Ball()

#Listen for user key presses
screen.listen()
screen.onkey(key="w", fun=paddle_left.move_paddle_up)
screen.onkey(key="s", fun=paddle_left.move_paddle_down)
screen.onkey(key="Up", fun=paddle_right.move_paddle_up)
screen.onkey(key="Down", fun=paddle_right.move_paddle_down)


#Main game logic
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()
    
    #Detect collision if paddles miss
    if ball.xcor() > 380:
        ball.restart()
        field.l_score += 1
        field.update_score()

    if ball.xcor() < -380:
        ball.restart()
        field.r_score += 1
        field.update_score()



screen.exitonclick()
