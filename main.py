import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
play = Player()


screen.listen()
screen.onkeypress(play.moving, "Up")
screen.onkeypress(play.moving, "w")


carros = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    score.update()
    time.sleep(0.3)
    screen.update()
    carros.create_car()
    carros.moving()

    for car in carros.cars:
        if car.distance(play) < 25:
            screen.clear()
            score.game_over()
            screen.exitonclick()
            game_is_on = False

    if play.new_level():
        carros.new_level()
        score.new_level()
