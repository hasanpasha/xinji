# Getting start

import turtle
import time
import random


delay = 0.1

# Score
score = 0
high_score = 0

#Set up the screen 
win = turtle.Screen()
win.title('Snake Game by @basha22hsn')
win.bgcolor('black')
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("square")
food.speed(0)
food.color("red")
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290))

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score : 0  high score : 0",align="center",font=("Courier", 24, "bold"))

segments = []


# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)



def exit():
    win._destroy()

#def easy_speed():
    #a = 1
#def regular_speed():
   # delay = 0.1
#def difficult_left():
   # delay = 0.005

# Keyboard Clicking Functions
win.listen()
win.onkey(exit, "Escape")
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_right, "Right")
win.onkey(go_left, "Left")
#win.onkeypress(easy_speed, "e")
#win.onkeypress(regular_speed, "r")
#win.onkeypress(difficult_left, "d")


# The Main Loop
while True:
    win.update()

    # Open high_score.txt file
    f = open("high_score.txt",'w')

    # Check for collisions with the border
    if head.xcor() > 290 or head.ycor() > 290 or head.xcor() < -290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        food.goto(random.randint(-290,290),random.randint(-290,290))

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("score : {}  high score : {}".format(score, high_score),align="center",font=("Courier", 24, "bold"))

    # Check for collisions with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.color("gray")
        new_segment.shape("square")
        segments.append(new_segment)

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("score : {}  high score : {}".format(score, high_score),align="center",font=("Courier", 24, "bold"))
        
        # Increase the speed of the snake faster and faster
        delay -= 0.001
        
        try:
            f.write("{}".format(high_score))
        except:
            print("Could not write in the file ")
        

    # Move the end segmensts first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    # the move() after segmensts it means first we move the segments[0] to were the head was
    # -- then move the head
    move()

    # Check for collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            food.goto(random.randint(-290,290),random.randint(-290,290))            
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("score : {}  high score : {}".format(score, high_score),align="center",font=("Courier", 24, "bold"))            
            delay = 0.1

    time.sleep(delay)
    f.close()
win.mainloop()
