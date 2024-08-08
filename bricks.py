from turtle import Turtle
from random import choice


class Bricks():
    
    def __init__(self):
        self.all_bricks = []

    def place_bricks(self,brick_rows,bricks_columns,bricks_colors):
        for i in range(brick_rows):
            for j in range(bricks_columns):
                brick = Turtle()
                brick.shape(f'{choice(bricks_colors)}')
                # brick.color(f'{colors[i]}')
                # brick.color('blue')
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.penup()
                brick.goto(-420 + j * 120, -100 - i * 30)
                self.all_bricks.append(brick)


