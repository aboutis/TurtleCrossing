from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(x=280, y=randint(-200, 200))
            self.cars.append(new_car)

    def moving(self):
        for car in self.cars:
            car.backward(self.speed)


    def new_level(self):
        self.speed += MOVE_INCREMENT