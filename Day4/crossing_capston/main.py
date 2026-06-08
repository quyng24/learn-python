from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Crossing Capston Game")

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player)  < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()