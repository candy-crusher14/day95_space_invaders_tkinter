from turtle import Turtle

class PowerUp(Turtle):
    def __init__(self, position,power_type, power_style):
        super().__init__()
        self.power_type = power_type
        self.shape("circle")
        if self.power_type == "increase_life":
            self.shape(power_style[0])
        elif self.power_type == "increase_score":
            self.shape(power_style[1])
        elif self.power_type == "increase_speed":
            self.shape(power_style[2])


        self.penup()
        self.goto(position)
        self.dy = -1.0  # Falling speed

    def move_powers(self):
        self.sety(self.ycor() + self.dy)