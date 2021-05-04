from turtle import Turtle
import random

CAR_COLOURS = ["red", "green", "blue", "orange", "yellow", "purple"]
INITIAL_MOVEMENT_SPEED = 5
MOVEMENT_INCREASE = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = INITIAL_MOVEMENT_SPEED
         
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len = 2, stretch_wid = 1)
            new_car.pu()
            new_car.color(random.choice(CAR_COLOURS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() < -330:
                self.all_cars.remove(car)

            car.bk(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVEMENT_INCREASE