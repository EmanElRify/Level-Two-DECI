import turtle

pen = turtle.Turtle()

def square(l,color):
    pen.color(color)
    for i in [1,2,3,4]:
        pen.forward(l)
        pen.right(90)
 
square(color = "red", l = 100)   
turtle.done()