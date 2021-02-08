# Teresa Yu
# Feb 7 2021
# Snake Game
# This game is a recreation of the classic Snake Game, using python turtle.

import turtle
import random
import time

def move(): 
  head.fd(20)
  if head.direction == "up":
      head.setheading(90)
  if head.direction == "down": 
      head.setheading(270) 
  if head.direction == "left": 
      head.setheading(180) 
  if head.direction == "right": 
      head.setheading(0)

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

speed = 2.5    
score = 0
high_score = 0
segments = [] 

window = turtle.getscreen()
window.setup(width=750,height=410)
window.bgcolor("#90EE90")
window.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white", "blue")
head.penup()
head.home()
head.direction = None

food = turtle.Turtle()
food.shape("circle")
food.penup()
food.color("red")
food.goto(0, 100) 

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.goto(0, 150)
pen.ht()
pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

while True:
  pen.clear()
  pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))
  window.update()
  if head.xcor() > 350 or head.xcor() < -350 or head.ycor() > 180 or head.ycor() < -180:
    time.sleep(1)
    head.home()
    pen.clear()
    score = 0
    pen.clear
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))
    for segment in segments:
      segment.goto(1000, 10000) 
    segments = []
    

  if head.distance(food) < 20:
    x = random.randint(-300,300)
    y = random.randint(-150,150)
    food.goto(x,y)
    score += 10

    new_segment = turtle.Turtle() 
    new_segment.shape("square") 
    new_segment.color("white") 
    new_segment.penup() 
    segments.append(new_segment)

    if score > high_score:
      high_score = score
  
  for index in range(len(segments)-1, 0, -1): 
    x = segments[index-1].xcor() 
    y = segments[index-1].ycor() 
    segments[index].goto(x, y) 
  if len(segments) > 0: 
    x = head.xcor() 
    y = head.ycor() 
    segments[0].goto(x, y) 
  move()

  for segment in segments: 
    if segment.distance(head) < 20:
      for segment in segments:
        segment.goto(1000, 1000) 
      segments = []
      head.home()
      time.sleep(1)
      pen.clear()
      pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))
      score = 0

  time.sleep(0.1)
 