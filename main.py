# import
import turtle

# drawing screen
drawing_screen = turtle.Screen()
drawing_screen.bgcolor("white")
drawing_screen.title("Drawing Board")
drawing_screen.listen()
# turtes
pen1 = turtle.Turtle()



# functions
def forwardTurtle():
    pen1.forward(50)
def backdTurtle():
    pen1.backward(50)
def turn_left():
    pen1.setheading(pen1.heading()-10)
def turn_right():
    pen1.setheading(pen1.heading()+10)
def clear_screen():
    pen1.clear()
def backToHome():
    pen1.penup()
    pen1.home()
    pen1.pendown()

drawing_screen.onkey(fun=forwardTurtle , key= "w")
drawing_screen.onkey(fun=backdTurtle , key= "s")
drawing_screen.onkey(fun=turn_left , key= "d")
drawing_screen.onkey(fun=turn_right , key= "a")
drawing_screen.onkey(fun=clear_screen , key= "c")
drawing_screen.onkey(fun=backToHome , key= "h")
turtle.mainloop()