from turtle import Turtle, Screen
import time
from snake import Snake

snake = Snake()

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






screen.exitonclick()
