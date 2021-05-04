from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height = 600, width = 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

end_of_game = False 
while not end_of_game:
    time.sleep(0.1)
    screen.update()

    # Tried to clear turtle instances to save memory but doesn't seem to work :(
    for turt in screen.turtles():
        if turt.xcor() < -330:
            screen.turtles().remove(turt)


    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            end_of_game = True
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()