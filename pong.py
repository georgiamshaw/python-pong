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

while True:
    wn.update()
