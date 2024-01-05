from turtle import *
from math import dist

class Circle():
  radius=0
  center=(0,0)
  pen = 0
  line_color="blue"
  fill_color = "red"
  def __init__(self,r,c):
    self.radius=r
    self.center=c
  def draw(self):
    if self.pen ==0:
      self.pen=Turtle()
    self.pen.clear()
    new_center = (self.center[0],self.center[1]-self.radius)
    self.pen.penup()
    self.pen.goto(new_center)
    self.pen.pendown()
    self.pen.color(self.line_color,self.fill_color)
    self.pen.begin_fill()
    self.pen.circle(self.radius)
    self.pen.end_fill()
  def set_line_color(self,color):
    self.line_color=color
  def set_fill_color(self,color):
    self.fill_color=color
  def move_x(self,value):
    self.center=(self.center[0]+value,self.center[1])
  def move_y(self,value):
    self.center=(self.center[0],self.center[1]+value)
  def left_key(self):
    self.move_x(-5)
  def right_key(self):
    self.move_x(5)
  def up_key(self):
    self.move_y(5)
  def down_key(self):
    self.move_y(-5)
  def is_touching(self,other):
    total=self.radius+other.radius
    if dist(self.center,other.center) < total:
      return True
    return False

display=Screen()
display.listen()
display.tracer(0)

a=Circle(200,(100,100))
b=Circle(100,(-200,-100))
display.onkeypress(a.left_key,"Left")
display.onkeypress(a.right_key,"Right")
display.onkeypress(a.up_key,"Up")
display.onkeypress(a.down_key,"Down")
while True:
  a.draw()
  b.draw()
  if a.is_touching(b):
    b.set_fill_color("green")
  else:
    b.set_fill_color("red")
  display.update()

'''
x = -100
y = -100
draw=Turtle()
display = Screen()
display.tracer(0)
draw.hideturtle()
running=True

def draw_circle(x,y):
  global draw
  draw.penup()
  draw.goto(x,y)
  draw.pendown()
  draw.color("red","blue")
  draw.begin_fill()
  draw.circle(50)
  draw.end_fill()
def esc_key():
  global running
  running = False
def left_key():
  global x
  x-=10
  if x < -400:
    x=-400
def right_key():
  global x
  x+=10
def up_key():
  global y
  y+=10
def down_key():
  global y
  y-=10
def setup_keys():
  
  display.listen()
  display.onkeypress(left_key,"Left")
  display.onkeypress(up_key,"Up")
  display.onkeypress(right_key,"Right")
  display.onkeypress(down_key,"Down")
  display.onkey(esc_key,"Escape")
def main():
  global display,draw
  setup_keys()
  while running==True:
   draw.clear()
   draw_circle(x,y)
   display.update()

main()
'''