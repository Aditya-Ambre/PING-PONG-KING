'''HI this is a simple PING PONG Game By DAYMAREBAIT
   It uses turtle and winsound module 
   the logic part is basic maths

   CONTROLS :-
   PLAYER A : W "UP" E "DOWN"
   PLAYER B : K "UP" L "DOWN"  
'''


import turtle
import winsound

win = turtle.Screen()
win.title("DAYMAREBAIT : ||PING PONG KING||")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Player A
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.shapesize(stretch_wid=5, stretch_len=1)
playerA.penup()     # removes the lines made by turtle
playerA.goto(-350, 0)    # position of the Paddle

# Player B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.shapesize(stretch_wid=5, stretch_len=1)
playerB.penup()     # removes the lines made by turtle
playerB.goto(350, 0)    # position of the Paddle


# BALL
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.shapesize(stretch_wid=2, stretch_len=2)
Ball.color("Light green")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.14
Ball.dy = 0.14

# Score_tracker
score_A = 0
score_B = 0
# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.penup()
sb.color("yellow")
sb.hideturtle()
sb.goto(0, 260)
sb.write("Player A : 0      Player B : 0", align="center",
         font=("Courier", 24, "bold"))
# PADDLE MOVEMENTS


def Paddle_A_Up():
    y = playerA.ycor()
    y += 30
    playerA.sety(y)


def Paddle_A_Dwm():
    y = playerA.ycor()
    y -= 30
    playerA.sety(y)


def Paddle_B_Up():
    y = playerB.ycor()
    y += 30
    playerB.sety(y)


def Paddle_B_Dwm():
    y = playerB.ycor()
    y -= 30
    playerB.sety(y)


# keyboardbinding
win.listen()
win.onkeypress(Paddle_A_Up, "w")
win.onkeypress(Paddle_A_Dwm, "e")
win.onkeypress(Paddle_B_Up, "k")
win.onkeypress(Paddle_B_Dwm, "l")
# Main function loop
while True:
    win.update()

    # Moving the Ball
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)

    # Check Margins
    if Ball.ycor() > 280:
        Ball.sety(280)
        Ball.dy *= -1

    if Ball.ycor() < -280:
        Ball.sety(-280)
        Ball.dy *= -1

    #  score update
    if Ball.xcor() > 350:
        score_A += 1
        sb.clear()
        sb.write("Player A: {}  Player B: {}".format(score_A, score_B),
                 align="center", font=("Courier", 24, "normal"))
        Ball.goto(0, 0)
        Ball.dx *= -1

    elif Ball.xcor() < -350:
        score_B += 1
        sb.clear()
        sb.write("Player A: {}  Player B: {}".format(score_A, score_B),
                 align="center", font=("Courier", 24, "normal"))
        Ball.goto(0, 0)
        Ball.dx *= -1

    # Paddle and ball collisions
    if Ball.xcor() < -340 and Ball.ycor() < playerA.ycor() + 50 and Ball.ycor() > playerA.ycor() - 50:
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif Ball.xcor() > 340 and Ball.ycor() < playerB.ycor() + 50 and Ball.ycor() > playerB.ycor() - 50:
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
