#import the modules
import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

#create the head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#create the apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,300)
pen.write("Score: 0  High Score: 0", align="center", font=("agency fb", 12,"normal"))

#arena
arena = turtle.Turtle()
arena.speed(0)
arena.color("white")
arena.hideturtle()
arena.penup()

#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def reset_score():
    score = 0
    pen.clear()
    delay = 0.1
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("agency fb", 12,"normal"))

        
#Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up") or wn.onkey(go_up, "w")
wn.onkey(go_down, "Down") or wn.onkey(go_down, "s")
wn.onkey(go_left, "Left") or wn.onkey(go_left, "a")
wn.onkey(go_right, "Right") or wn.onkey(go_right, "d")


#main game loop
while True:
    wn.update()
    
    arena.goto(-300,300)
    arena.pendown()
    arena.goto(300,300)
    arena.goto(300,-300)
    arena.goto(-300,-300)
    arena.goto(-300,300)
    
    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        
        #hide the segment
        for segment in segments:
            segment.goto(1000,1000)
            
        #clear the segments list
        segments.clear()
        
        #reset score
        score = 0
        pen.clear()
        
        delay = 0.1
        
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("agency fb", 12,"normal"))
    
    #check for collision with food
    if head.distance(apple) < 20:
        #move food to random spot
        x = random.randrange(-280,280, 20)
        y = random.randrange(-280,280, 20)
        apple.goto(x,y)
        
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        
        #shorten delay
        delay -= 0.001
        
        #increase score
        score += 1
        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("agency fb", 12,"normal"))
        
    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #check for head collision with segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"
            
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            #clear the segments list
            segments.clear()
            
            #reset score
            score = 0
            pen.clear()
        
            delay = 0.1
        
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("agency fb", 12,"normal"))
    
    time.sleep(delay)

wn.mainloop()
