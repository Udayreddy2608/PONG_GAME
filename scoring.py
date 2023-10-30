from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}",align="center",font=("Courier",54,"normal"))
        self.hideturtle()


    def update(self):
        self.clear()
        self.score+=1
        self.write(f"{self.score}", align="center", font=("Courier", 54, "normal"))

