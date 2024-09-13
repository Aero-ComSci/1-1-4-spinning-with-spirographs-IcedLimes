import turtle as trtl
painter=trtl.Turtle()
painter.hideturtle()
painter.speed(0)

# gives list of colors 
colors=["red","orange","yellow","green","blue","purple"]

# creates a function called draw_square 

def draw_square(size,color):
    painter.penup()
    #goes to size divided by 2
    painter.goto(-size/2,size/2)
    painter.pendown()
    #picks the painters color as one of the colors in the list, the specific color is chosen later
    painter.color(color)
    #draws the square based on the size that is decided later.
    for _ in range(4):
        painter.forward(size)
        painter.right(90)

#finds the size and color 6 times
for i in range(6):
    # finds the size
    size=(i+1)*30
    #goes through each color in the dictionary
    color=colors[i%len(colors)]
    #runs the draw_square function
    draw_square(size,color)
#hides the turtle
painter.hideturtle()
trtl.done()
