from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(height = 600, width = 800)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.paddle_up, 'w') 
screen.onkey(left_paddle.paddle_down, 's')
screen.onkey(right_paddle.paddle_up, 'Up')
screen.onkey(right_paddle.paddle_down, 'Down')

end_of_game = False
while not end_of_game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    if ((ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (ball.xcor() < -320 and ball.distance(left_paddle) < 50)):
        ball.x_bounce()

    if ball.xcor() > 380: 
        scoreboard.update_left_score()
        ball.reset_position()


    if ball.xcor() < -380:
        scoreboard.update_right_scoreboard()
        ball.reset_position()

screen.exitonclick()  