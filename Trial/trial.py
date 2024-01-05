"""
x=input("Choose a number")
y=True
for i in range (2,int(x)):
    if int(x)%i==0:
        y=False
        print("That number is composite.")
        break    
if y==True:
    print("That number is prime.")
    """
from turtle import *
w=Turtle()
w.pensize(50)
w.left(90)
w.color("Brown")
w.goto(0,-50)
w.begin_fill()
w.forward(300)
w.right(50)
w.forward(120)
w.forward(50)
w.backward(100)
w.end_fill()
done()

       

         
        
    
