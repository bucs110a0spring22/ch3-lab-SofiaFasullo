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
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
  michelangelo.clear()
  leonardo.clear()

restart_race()

#part b

def realistic_race(runner1 = michelangelo, runner2 = leonardo):
 runner1.down()
 runner2.down()
 for i in range(1,11):
   stride1 = random.randrange(0,10)
   stride2 = random.randrange(0,10)
   runner1.forward(stride1)
   runner2.forward(stride2)

realistic_race()
restart_race()


# Part B - complete part B here

def draw_shapes(num_sides=4):
  for i in range(1,num_sides+1):
    leonardo.down()
    leonardo.forward(10)
    leonardo.left(360/num_sides)
  leonardo.up()
  leonardo.forward(5*num_sides)
  leonardo.clear()

draw_shapes(4)
draw_shapes(6)
draw_shapes(9)
draw_shapes(12) 

restart_race()

window.exitonclick()