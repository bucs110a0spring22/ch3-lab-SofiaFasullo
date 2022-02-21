import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

run1 = random.randrange(0,100)   ## 5. your code goes here
run2 = random.randrange(0,100)
michelangelo.down()
leonardo.down()
michelangelo.forward(run1)
leonardo.forward(run2)

# Part B - complete part B here


window.exitonclick()
