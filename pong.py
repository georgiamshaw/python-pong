import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A

paddleA = turtle.Turtle()
paddleA.speed(0) # speed of animation
paddleA.shape("square") # built in shape
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0) # place on Screen

# Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0) # speed of animation
paddleB.shape("square") # built in shape
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0) # place on Screen

# Ball

ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square") # built in shape
ball.color("white")
ball.penup()
ball.goto(0, 0) # place on Screen

# Function

def paddleAUp():
    y = paddleA.ycor() # this method is from the turtle module. it returns the y coordinate
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor() # this method is from the turtle module. it returns the y coordinate
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor() # this method is from the turtle module. it returns the y coordinate
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor() # this method is from the turtle module. it returns the y coordinate
    y -= 20
    paddleB.sety(y)

# keyboard binding
# listening for keyboard input

wn.listen()
wn.onkey(paddleAUp, "w")
wn.onkey(paddleADown, "s")
wn.onkey(paddleBUp, "Up")
wn.onkey(paddleBDown, "Down")

# def paddleBUp():



# Main loop of the game

while True:
    wn.update()
