
import turtle
import random
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_screen.colormode(255)
screen_size_multiplier = .9
screenwidth, screenheight = my_screen.screensize()

def flower (a, b, scale, col1, col2, col3, col4, col5, col6, col7, col8, col9):
    #draw petals
    my_turtle.pu()
    my_turtle.setpos(a, b)
    my_turtle.rt(90)
    my_turtle.pd()
    my_turtle.fillcolor(col1, col2, col3)
    origin = my_turtle.pos()
    dot_dir = my_turtle.heading()
    my_turtle.begin_fill()
    for i in range (6):
        my_turtle.circle(scale, 220)
        my_turtle.lt(200)
    my_turtle.end_fill()
    my_turtle.pu()
    #draw stem
    my_turtle.setpos(origin)
    my_turtle.seth(dot_dir)
    my_turtle.pd()
    my_turtle.fillcolor(col4, col5, col6)
    my_turtle.begin_fill()
    my_turtle.fd(scale*9)
    my_turtle.end_fill()
    my_turtle.pu()
    #draw dot in center
    my_turtle.setpos(origin)
    my_turtle.seth (dot_dir)
    my_turtle.fillcolor(col7, col8, col9)
    my_turtle.bk(scale+2/3*scale)
    my_turtle.pd()
    my_turtle.begin_fill()
    my_turtle.circle(scale/3)
    my_turtle.end_fill ()
    
def random_flowers():
    #randomize position on screen
    a = random.randint(int(-1*screen_size_multiplier*screenwidth),int(screen_size_multiplier*screenwidth))
    b = random.randint(int(-1*screen_size_multiplier*screenwidth),int(screen_size_multiplier*screenheight))
    #randomize size of flower
    scale = random.randint (1, 50)
    #randomize colors
    col1 = random.randint (1, 255)
    col2 = random.randint (1, 255)
    col3 = random.randint (1, 255)
    col4 = random.randint (1, 255)
    col5 = random.randint (1, 255)
    col6 = random.randint (1, 255)
    col7 = random.randint (1, 255)
    col8 = random.randint (1, 255)
    col9 = random.randint (1, 255)
    

    flower (a, b, scale, col1, col2, col3, col4, col5, col6, col7, col8, col9)

def many_random_flowers():
    for num in range (50):
        random_flowers()
    

many_random_flowers()
