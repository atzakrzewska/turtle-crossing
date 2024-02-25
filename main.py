from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager, Road
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor("DarkOliveGreen3")
screen.colormode(255)

player = Player()

road = Road()
road.lay()

scoreboard = Scoreboard()
scoreboard.update()

screen.listen()
screen.onkeypress(fun=player.move, key="w")

car_manager = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    # detect finishing the level
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_difficulty()
        scoreboard.level_up()
screen.exitonclick()
