#-------PONG GAME-------#

#--ball.py--#
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()

#--paddle.py--#
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

#--scoreboard.py--#
from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-170, 240)
        self.write(f"PLAYER 1: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(170, 240)
        self.write(f"PLAYER 2: {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

#--main.py--#
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("DarkSlateGrey")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect r_paddle miss
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        time.sleep(1)

    # Detect l_paddle miss
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        time.sleep(1)

screen.exitonclick()

