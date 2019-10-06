import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

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
ball.dx = 0.5
ball.dy = 0.5

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))




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


# Main loop of the game

while True:
    wn.update()

    # move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# create borders

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this reverses the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # this reverses the direction

    if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1 # this reverses the direction
            pen.clear()
            scoreA += 1
            pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1 # this reverses the direction
            pen.clear()
            scoreB += 1
            pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    # paddle and ball colliding
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        ball.dx += -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(-340)
        ball.dx += 1
