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

#simple_race(michelangelo)
#simple_race(leonardo)

def restart_race():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
  michelangelo.clear()
  leonardo.clear()

#restart_race()

#part b

def realistic_race(runner1 = michelangelo, runner2 = leonardo):
 runner1.down()
 runner2.down()
 for i in range(0,10):
   stride1 = random.randrange(0,10)
   stride2 = random.randrange(0,10)
   runner1.forward(stride1)
   runner2.forward(stride2)

#realistic_race()
#restart_race()

 for i in range(0,10):
   stride1 = random.randrange(0,10)
   stride2 = random.randrange(0,10)
   print(stride1)
   print(stride2)

# Part B - complete part B here
window.exitonclick()
# for i in range(0,10):
  #  stride1 = random.randrange(0,10)
  #  runner1.forward(stride1)
  #  stride2 = random.randrange(0,10)
  #  runner2.forward(stride1)