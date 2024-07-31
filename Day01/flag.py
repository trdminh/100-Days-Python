import turtle

def draw_rectangle(x, y, width, height):

    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


def main():

    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    width, height = 540, 360
    draw_rectangle(x, y, width, height)

    pice = 22
    center_x, center_y = x + 5 * pice + 160, y + height - pice * 5 
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(center_x, center_y, pice * 3)
    turtle.ht()
    turtle.mainloop()

if __name__ == "__main__":
   main()