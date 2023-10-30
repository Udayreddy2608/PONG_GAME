from turtle import Screen
from screen import MidLine
from paddles import Paddle
from ball import Ball
import time
from scoring import Scoreboard

screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")

screen.tracer(0)
mid=MidLine()
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score1=Scoreboard((120,250))
score2=Scoreboard((-120,250))


screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

game_on=True
x=0.1
while game_on:
    time.sleep(x)
    screen.update()
    ball.move()

    if  ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision
    if ball.distance(r_paddle)<40 and ball.xcor()>320 or  ball.distance(l_paddle)<40 and ball.xcor()<-320:
        ball.bounce_x()
        x*=0.9
    if ball.xcor()>380:
        ball.goto(0,0)
        ball.bounce_x()
        score2.update()
        x=0.1
    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.bounce_x()
        score1.update()
        x=0.1

































screen.exitonclick()