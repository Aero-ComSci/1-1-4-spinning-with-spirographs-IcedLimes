#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.goto(-200, 0)
painter.pendown()
#infinite loop
while(True):

    x = -200
    y = 0
    move_x = 1
    move_y = 1
    while (x < 1):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1
    
        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1

    painter.penup()
    painter.goto(-200,0)
    painter.pendown()

    # resets x and y values
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    while (x < 1):
        #when y was greater than -100 it would keep subtracting the y value by one while the x value added by one to move diagonally down and right until y was equal to -100 
        while (y > -100):
            x = x + move_x
            y = y - move_y
            painter.goto(x,y)
        # when y was less than zero it would move right and up diagonally until it reached zero to create the first square
        while (y < 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        # repeats because x is at 0 when the first cycle completes which is less than 1 so it makes another diagonal
        #goes back to og position
    painter.penup()
    painter.goto(-200,0)
    painter.pendown()

wn = trtl.Screen()
wn.mainloop()
