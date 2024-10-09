import turtle as trtl
painter=trtl.Turtle()
screen=trtl.Screen()
painter.hideturtle()
painter.speed(0)
screen.setup(width=800, height=800)

def square():
        painter.setheading(90)
        painter.penup()
        painter.forward(40)
        painter.pendown()
        painter.right(90)
        painter.forward(40)
        painter.right(90)
        painter.forward(80)
        painter.right(90)
        painter.forward(80)
        painter.right(90)
        painter.forward(80)
        painter.right(90)
        painter.forward(80)
        

distance=0
for _ in range(5):
    painter.penup()
    painter.goto(-360+distance,0)
    painter.pendown()
    square()
    distance+=180

wn = trtl.Screen()
wn.mainloop()
