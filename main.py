# Teresa Yu
# Feb 7 2021
# Snake Game
# This game is a recreation of the classic Snake Game, using python turtle.

# Using turtle, random and time modules.
import turtle
import random
import time

# Defining a move function to make the snake's head move forward
def move(): 
  head.fd(speed)

  # Rotate in the direction inputted (by keyboard) from the below functions.
  if head.direction == "up":
      head.setheading(90)
  if head.direction == "down": 
      head.setheading(270) 
  if head.direction == "left": 
      head.setheading(180) 
  if head.direction == "right": 
      head.setheading(0)

# Defining functions for each direction. If the direction inputted is not the opposite direction, rotate to the desired direction.
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

# Initializing speed (how fast), score, high score, and segments (number of body parts).
speed = 20   
score = 0
high_score = 0
segments = [] 

# Set up the screen/background. Tracer is used to make the game run more smoothly.
window = turtle.getscreen()
window.setup(width=750,height=410)
window.bgcolor("#90EE90")
window.tracer(0)

# Set up the head of the snake, and initialize the direction it's going as None.
head = turtle.Turtle()
head.shape("square")
head.color("white", "blue")
head.penup()
head.home()
head.direction = None

# Set up food, and move it to (0,100) thus it is far away from home. That way, the game won't detect the food being near the head.
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.color("red")
food.goto(0, 100) 

# Initialize the pen to write the scores.
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.goto(0, 150)
pen.ht()
pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

# Listen for what the user inputs on the keyboard to control the movement of the snake. User can use WSAD or arrow keys. Call on desired direction function when pressed. 
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# While the game is running:
while True:
  # Update the screen and write the scores using the pen.
  window.update()
  pen.clear()
  pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

  # If the snake goes out of the screen, pause and restart the game. 
  if head.xcor() > 350 or head.xcor() < -350 or head.ycor() > 180 or head.ycor() < -180:
    time.sleep(1)
    head.home()
    pen.clear()
    score = 0
    pen.clear
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))
    # Hide the segments. Then, remove all of the segments.
    for segment in segments:
      segment.goto(1000, 10000) 
    segments = []
    
  # If the snake "eats" the food, randomly put the food somewhere else. Add 10 to the current score.
  if head.distance(food) < 20:
    x = random.randint(-300,300)
    y = random.randint(-150,150)
    food.goto(x,y)
    score += 10

    # Add a new segment to the snake.
    new_segment = turtle.Turtle() 
    new_segment.shape("square") 
    new_segment.color("white") 
    new_segment.penup() 
    segments.append(new_segment)
    
    # If the current score is higher than the high score, change it to the current score. 
    if score > high_score:
      high_score = score
  
  # Loop through the segments, starting with the last segment. Since indices start at 0, subtract 1 from the length.
  for i in range(len(segments)-1, 0, -1): 
    # Go to the x and y coordinates of the previous segment.
    x = segments[i-1].xcor() 
    y = segments[i-1].ycor() 
    segments[i].goto(x, y) 
  
  # The first segment goes to the x and y coordinates of the head.
  if len(segments) >= 1: 
    x = head.xcor() 
    y = head.ycor() 
    segments[0].goto(x, y) 
  # Move the segments with the head, changing directions as well.
  move()
  
  # Check if each segment is collides with the head. If it does, restart the game.
  for segment in segments: 
    if segment.distance(head) < 5:
      for segment in segments:
        segment.goto(1000, 1000) 
      segments = []
      head.home()
      time.sleep(1)
      pen.clear()
      pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))
      score = 0

  # Make game run slower.
  time.sleep(0.1)
 