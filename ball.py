from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color('white')
        self.penup()
        self.goto((0, 0))

        self.x_move = 8
        self.y_move = 8
        self.move_speed = 1.2



    def move_ball(self):
        # new_y = self.ycor() - self.y_move
        # self.sety(new_y)

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def level_up(self):
        self.x_move *= self.move_speed
        self.y_move *= self.move_speed
    def reset_position(self):
        self.goto((0, 0))
        self.goto(0, 0)
        # self.move_speed = 0.04
        self.bounce_x()
