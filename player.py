from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.lasers = []
        self.goto(position)
        self.speed = 20


    def move_left(self):
        x = self.xcor()
        x -= self.speed
        if x < -450: # if x is -350 do nothing
            x = -450
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.speed
        if x > 450:
            x = 450
        self.setx(x)


    def move_forward(self):
            y = self.ycor()
            y += self.speed
            if y > 300:
                y = 300
            self.sety(y)

    def move_backward(self):
        y = self.ycor()
        y -= self.speed
        if y < -300:
            y = -300
        self.sety(y)


    def increase_speed(self):
        self.speed = 40

    def reset_speed(self):
            self.speed = 20

    def shoot_laser(self, laser):
        if len(self.lasers) <= 1:
            shoot_laser = Turtle()
            shoot_laser.penup()
            shoot_laser.shape(f'{laser}')
            shoot_laser.goto(x=self.xcor(), y = self.ycor())
            self.lasers.append(shoot_laser)






