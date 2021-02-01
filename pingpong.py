import turtle
# uncomment if you have the sound  file u need 
# import os


wn = turtle.Screen()
wn.title("ping pong game")
wn.bgcolor("brown")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
Score_A = 0
Score_B = 0

#paddle_A
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_len=1, stretch_wid=5)
paddle1.color("black")
paddle1.penup()
paddle1.goto(-350, 0)



#paddle_B
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.color("black")
paddle2.penup()
paddle2.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font={"courier", 24, "normal"} )

#myfuntion setting directiion for up in paddle1
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

#myfuntion setting directiion for down in paddle1
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

    #myfuntion setting directiion for up in paddle2
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

#myfuntion setting directiion for down in paddle2
def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
# keyboard binding od the letters to the game
wn.listen()
wn.onkeypress(paddle1_up, "a")
wn.onkeypress(paddle1_down, "x")
wn.onkeypress(paddle2_up, "p")
wn.onkeypress(paddle2_down, "l")


#mainloop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder checking to enable the ball bounce when it hits the  topboarder
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("aplay soundfile.extension&")
    
    #boarder checking to enable the ball boumce as it hits the down side of the boader
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("aplay soundfile.extension&")


    # boarder checking and making sure the ball returns to the origin and reverses the throw
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        Score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font={"courier", 24, "normal"} )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font={"courier", 24, "normal"} )



    #paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #os.system("aplay soundfile.extension&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #os.system("aplay soundfile.extension&")
