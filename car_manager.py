import random
from turtle import Turtle
import numpy

COLORS = ((177, 42, 12), (217, 114, 61), (239, 171, 104), (194, 177, 136), (0, 4, 126), (0, 56, 185), (139, 65, 255), (104, 69, 251), (12, 166, 221))
INITIAL_VELOCITY = 5
SPEED_UP = 5
LANES = (numpy.arange(-180, 180, 30))

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.velocity = INITIAL_VELOCITY

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=320, y=random.choice(LANES))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.velocity)

    def increase_difficulty(self):
        self.velocity += SPEED_UP


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-300, 200)
        self.color("gray50")
        self.lay()
        self.color("white")
        self.paint()

    def lay(self):
        self.begin_fill()
        for _ in range(2):
            self.forward(600)
            self.right(90)
            self.forward(400)
            self.right(90)
        self.end_fill()

    def paint(self):
        for height in numpy.arange(-165, 180, 30):
            self.penup()
            self.goto(x=300, y=height)
            self.seth(180)
            for _ in range(30):
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
