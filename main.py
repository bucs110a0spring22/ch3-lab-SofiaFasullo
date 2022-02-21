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

## 5. your code goes here

def simple_race(runner = michelangelo):
  distance_ran = random.randrange(0,100)
  runner.down()
  runner.forward(distance_ran)
  runner.up()

simple_race(michelangelo)
simple_race(leonardo)

def restart_race():
  michelangelo.up()
  leonardo.up()
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)

restart_race()

# Part B - complete part B here


window.exitonclick()
