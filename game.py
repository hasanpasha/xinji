#This is turtle game

#Part ONE : Getting started
import turtle 
from tkinter import *
import os
#from filewriter import Writer
#import time

#seconds = time.time()
#local_time = time.ctime(seconds)

win = turtle.Screen()
win.title("pong by @basha22hsn")
# Win background color
win.bgcolor("black")
# Win size
win.setup(width=800,height=600)
win.tracer(0) #This stops the window from updating 

# Score
score_a = 0
score_b = 0


# Paddle A

paddle_a = turtle.Turtle()
# set the speed of paddle_a to the maximum possible speed, otherwise things be really slow
paddle_a.speed(0)
# Give the paddle_a a shape 
paddle_a.shape("square")
# Give paddle color
# paddle_a shape size set
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# paddle color
paddle_a.color("white")
# The code below stops the paddle_a from drawing a line by default   
paddle_a.penup()
# paddle_a start from the below 
# First number horrizonally means 350 far from the center 
# Second Verticlully means in the center
paddle_a.goto(-350, 0)


# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
# Move the ball 
ball.dx = 0
ball.dy = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 25, "bold"))

# Functions

#paddle_a_up
def paddle_a_up():
    # Get the y corner and set it as y
    y = paddle_a.ycor()
    # Increase y 
    if y < 240:
        y += 40 
    # set the new y variable 
    paddle_a.sety(y)

#paddle_a_down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 40 
    paddle_a.sety(y)

#paddle_b_up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 40 
    paddle_b.sety(y)

#paddle_b_down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 40 
    paddle_b.sety(y)

# First speed
def _1s():
    ball.dx = 0.25
    ball.dy = 0.25


# second speed
def _2s():
    ball.dx = 0.5
    ball.dy = 0.5

# Third speed
def _3s():
    ball.dx = 0.75
    ball.dy = 0.75

# fourd speed
def _4s():
    ball.dx = 1.0
    ball.dy = 1.0

# fifth speed
def _5s():
    ball.dx = 1.25
    ball.dy = 1.25

# Exit
def Exit():
    def SureExit():
        try:
            win._destroy()
            ExitWin.destroy()
        except:
            ExitWin.destroy()
    def ExitWinDestroy():
        ExitWin.destroy()
    ExitWin = Tk()
    ExitWin.title("Warning !")
    ExitWin.configure(bg='white')
    ExitWin.wm_attributes('-type', 'splash')
    # width, height, far from right, far from top
    ExitWin.geometry("200x75+500+400")
    SureLabel = Label(ExitWin, text="Are you sure ?",bg="white").grid(row=1,column=5)
    YesButton = Button(ExitWin, text="Yes",command=SureExit,bg="white").grid(row=2,column=3)
    NoButton = Button(ExitWin, text="No",command=ExitWinDestroy,bg="white").grid(row=2,column=7)
    ExitWin.mainloop()
    
# Reset
def reset():
    score_a = 0
    score_b = 0
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "bold"))
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0

# stop
def _0s():
    if ball.dx and ball.dy != 0:
        ball.dx = 0
        ball.dy = 0
    elif ball.dx and ball.dy == 0:
        ball.dx = 0.25
        ball.dy = 0.25
   

# Keyboard binding 

# Tell the win to listen to the keyboard inputs 
win.listen()
# when the "w" button clicked the paddle_a_up function is enabled
#paddle_a_up "W"
win.onkey(paddle_a_up, "w")
#paddle_a_down "s"
win.onkey(paddle_a_down, "s")
#paddle_b_up "Up"
win.onkey(paddle_b_up, "Up")
#paddle_b_down "Down"
win.onkey(paddle_b_down, "Down")

# Exit "Esc"
win.onkey(Exit, "Escape")

# Ball speed "1, 2, 3, 4, 5" five levels
win.onkey(_0s, "space")
win.onkey(_1s, "1")
win.onkey(_2s, "2")
win.onkey(_3s, "3")
win.onkey(_4s, "4")
win.onkey(_5s, "5")

win.onkey(reset, "r")

# Main Game Loop

# This code below mean everytime it's true the window is updating.
#f = open("{}".format(local_time), 'a')
while True:

    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking 
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if  ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    
    if  ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        if score_a != 0:
            score_a += 1
        elif score_a == 0:
            score_a *= 0
            score_a += 1
        # First clear the score so it won't print in top of it the score
        pen.clear()
        # update the score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "bold"))
        os.system("aplay lose_b.wav&")
        #f = open("{}".format(local_time), 'w')
        #f.write("score A: {}".format(score_a))
        #Writer(filename='{}'.format(local_time), ext='txt') << ["{}".format(score_a)]
        #f.close()

    if  ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        if score_b != 0:
            score_b += 1
        elif score_b == 0:
            score_b *= 0
            score_b += 1
        pen.clear() 
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "bold"))
        os.system("aplay lose_b.wav&")
        #f = open("{}".format(local_time), 'w')
        #f.write("\nscore B : {}".format(score_b))
        #Writer(filename='{}'.format(local_time), ext='txt') << ["{}".format(score_a),"{}".format(score_b)]
        #f.close()

    # Padlle and ball collisions

    # paddle a
    if (ball.xcor() > 340 and ball.ycor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    #paddle b
    if (ball.xcor() < -340 and ball.ycor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
