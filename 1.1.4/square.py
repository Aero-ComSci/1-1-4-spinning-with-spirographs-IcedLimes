import turtle as trtl
painter=trtl.Turtle()
painter.hideturtle()
painter.speed(0)

def draw_square(size,color):
    painter.penup()
    painter.goto(-size/2,size/2)
    painter.pendown()
    painter.color(color)
    for _ in range(4):
        painter.forward(size)
        painter.right(90)

num_squares=6
size_increment=30
colors=["red","orange","yellow","green","blue","purple"]

for i in range(6):
    size=(i+1)*size_increment
    color=colors[i%len(colors)]
    draw_square(size,color)

painter.hideturtle()
trtl.done()
