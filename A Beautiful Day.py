
import turtle
import random

#set up screen for drawing
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_screen.colormode(255)

screenwidth, screenheight = my_screen.screensize()

# this function draws mountains
def mountains (radius):
    
    my_turtle.pu ()
    my_turtle.color ("green", "green")
    my_turtle.setpos(screenwidth, 0)
    my_turtle.width(radius/20)
    my_turtle.pd()
    while my_turtle.xcor () > -screenwidth:
        my_turtle.seth(90)
        my_turtle.circle(radius, 180)

#this function draws the sun        
def sun(radius):
    my_turtle.pu()
    turtle.textinput("hey", "It's a beautiful day!")
    my_turtle.setpos(screenwidth-radius, screenheight-radius)
    my_turtle.pd()
    #draw ridges
    for i in range (19):
        my_turtle.color ("yellow", "")
        my_turtle.width(radius/20)
        my_turtle.begin_fill()
        my_turtle.circle(radius/10, 180)
        my_turtle.rt(200)
    my_turtle.end_fill()
    my_turtle.pu()
    
     
            
    
def head (radius):
    
#draw head of stick figure
    my_turtle.width(1)  
    my_turtle.color ("black", "white")
    my_turtle.begin_fill()
    my_turtle.setpos(0,0)
    my_turtle.seth(0)
    my_turtle.pd()
    my_turtle.circle (radius)
    my_turtle.lt(90)
    my_turtle.end_fill()
    my_turtle.penup()
    
#draw hairline of stick figure
def hairline (radius):
    my_turtle.fd(radius*1.5)
    my_turtle.pendown()
    my_turtle.lt(90)
    
    my_turtle.fd((radius**2-(radius/3)**2)**.5)
    my_turtle.bk((radius**2-(radius/3)**2)**.5)
    my_turtle.lt(180)
    my_turtle.fd((radius**2-(radius/3)**2)**.5)
    
    my_turtle.bk((radius**2-(radius/3)**2)**.5)
    
   # draw eyes of stick figure
def eyes (radius):
    my_turtle.rt(90)
    my_turtle.penup()
    my_turtle.fd(radius/3)
    my_turtle.rt(90)
    my_turtle.fd(radius/2)
    my_turtle.pendown()
    my_turtle.dot(radius/5)
    my_turtle.penup()
    
##draw nose of stick figure
def nose (radius):
    my_turtle.lt(180)
    my_turtle.fd(radius)
    my_turtle.pendown()
    my_turtle.dot(radius/5)
    my_turtle.penup()
    my_turtle.rt(180)
    my_turtle.fd(radius/2)
    my_turtle.lt(90)
    my_turtle.fd(radius/3)
    my_turtle.pendown()
    my_turtle.width (radius/20)
    my_turtle.fd(radius/5)
    my_turtle.lt(90)
    my_turtle.fd(radius/5)
    my_turtle.bk(radius/5)
    my_turtle.rt (90)
    my_turtle.penup()
    my_turtle.fd(radius/4)
    my_turtle.rt(90)
    
#drawmouth of stick figure
def mouth (radius):
    my_turtle.pendown()
    my_turtle.color("black", "red")
    my_turtle.begin_fill()
    my_turtle.fd (radius/4)
    my_turtle.bk (2*radius/4)
    my_turtle.lt(90)
    my_turtle.circle(-radius/4, 180)
    my_turtle.end_fill()
    my_turtle.pu()
    my_turtle.setpos(0,0)
    my_turtle.rt(90)
    
##draw ears of stick figure
def ears (radius):
    my_turtle.circle(radius,90)
    my_turtle.lt(90)
    my_turtle.fd(radius/5)
    my_turtle.circle (radius/5, 220)
    my_turtle.pd()
    my_turtle.rt(45)
    my_turtle.width (1)
    my_turtle.circle(radius/6,180)
    my_turtle.pu()
    my_turtle.setpos(0,0)
    
    my_turtle.seth(0)
    my_turtle.circle(radius, 270)
    ears = turtle.pos()
    my_turtle.rt(90)
    my_turtle.pd()
    my_turtle.circle(radius/6, 180)
    my_turtle.pu()
    
#draw neck,hands stomack and legs (using sticks) of stick figure
def neck(radius):
    my_turtle.setposition(0,0)
    my_turtle.seth(270)
    my_turtle.pd()          
    my_turtle.fd (radius)
def left_hand (radius):
    my_turtle.left(45)
    my_turtle.bk(radius*3/2)
    my_turtle.fd(radius*3/2)
def right_hand (radius):
    my_turtle.rt(90)
    my_turtle.bk(radius*3/2)
    my_turtle.fd(radius*3/2)
def stomach (radius):
    my_turtle.lt(45)
    my_turtle.fd(radius)
def right_leg (radius):
    my_turtle.lt(45)
    my_turtle.fd(radius*3/2)
    my_turtle.bk(radius*3/2)
def left_leg (radius):
    my_turtle.rt(90) #(dif angles for dif positions)
    my_turtle.fd(radius*3/2)

#thought bubble above stick figure's head
   
def thought_bubble (radius):
    my_turtle.pu()
    my_turtle.setpos(0,0)
    my_turtle.seth(0)
    my_turtle.circle(radius, 120)
    my_turtle.pd()
    my_turtle.lt(90)
    my_turtle.bk(radius/5)
    for i in range (20):
        my_turtle.circle(radius/10, 180)
        my_turtle.lt(200)
    my_turtle.pu()

#draw hi
def say_hi (radius):
    my_turtle.seth(270)
    my_turtle.bk(radius*2/3)
    my_turtle.pd()
    my_turtle.fd(radius/2)
    my_turtle.bk(radius/4)
    my_turtle.seth(0)
    my_turtle.fd(radius/4)
    my_turtle.seth(270)
    my_turtle.fd(radius/4)
    my_turtle.bk(radius/2)
    my_turtle.seth(0)
    my_turtle.pu()
    my_turtle.fd(radius/6)
    my_turtle.pd()
    my_turtle.dot(radius/15)
    my_turtle.pu()
    my_turtle.seth(270)
    my_turtle.fd(radius/8)
    my_turtle.pd()
    my_turtle.fd(radius*3/8)



#draw stick figure (using functions of the body parts)
def draw_stick_figure (radius):
    head (radius)
    hairline (radius)
    eyes (radius)
    nose (radius)
    mouth (radius)
    ears (radius)
    neck (radius)
    left_hand (radius)
    right_hand (radius)
    stomach (radius)
    right_leg (radius)
    left_leg (radius)
    
def main (num):
    # user input will determine the scale of the image, draw all the parts! Only draw if between 50 and 150 inclusive
    while num<50 or num>150:
        num = int(turtle.textinput("Welcome!", "Enter a random number between 50 and 150."))
    mountains (num)
    sun (num)
    draw_stick_figure(num)
    thought_bubble (num)
    say_hi(num)
#set num to 0 and call main    
num = 0
main (num)

