from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) 

 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(0.1)     
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend_snake()
        scoreboard.update_scoreboard()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        end_of_game = True
        scoreboard.game_over()
    
    if snake.head.position() in [snake_body.position() for snake_body in snake.snake_segments[1:]]:
        end_of_game = True
        scoreboard.game_over()



screen.exitonclick()
