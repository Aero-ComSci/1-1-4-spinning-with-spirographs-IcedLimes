import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

# First pattern
x = -200
y = 0
move_x = 1
move_y = 1

# Draw the first pattern (original)
while (x < 0):
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

# Set starting point for the opposite pattern
x = 0
y = 0
painter.penup()
painter.goto(x, y)
painter.pendown()

move_x = 1
move_y = 1

# Draw the opposite pattern
while (x < 200):
    while (y < 100):
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = -1
    while (y > 0):
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = 1

wn = trtl.Screen()
wn.mainloop()
