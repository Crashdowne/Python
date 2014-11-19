"""
    CSC 106 Assignment 3 - MyGraphic
    
     Marina Retseptor and Bryan Kesteloo
"""
import turtle
import random

# Method to draw a circle of a given color, radius, and x,y coordinates
def DrawCircle(draw, x, y, r, color):
    draw.penup()
    draw.goto(x, y-r)
    draw.pendown()
    draw.pencolor(color)
    draw.circle(r)
 
# Draws a circle with the color filled in
def DrawFilledCircle(draw, x, y, r, color):
    draw.penup()
    draw.goto(x, y-r)
    draw.pendown()
    draw.pencolor(color)
    draw.begin_fill()
    draw.circle(r)
    draw.end_fill()
    
# Sets the size of the drawing screen
screenWidth = 1000
screenHeight = 1000
draw = turtle.Turtle()
# Sets the drawing speed to max
draw.speed(0)
wn = turtle.Screen()
# Sets up the window parameters, with it centered at 0,0
wn.setup (width=screenWidth, height=screenHeight, startx=0, starty=0)

radius = 100
# Loop goes from the first value (eg 500) to the second (eg -500) by increments of -100 (subtracting radius fixes the range being exclusive)
for row in range((screenHeight/2), (-1*(screenHeight/2) - radius), radius*-1):
    for col in range((screenWidth/2), (-1*(screenWidth/2) - radius), radius*-1):
        DrawFilledCircle(draw, col, row, radius, "black")
        for i in range(radius, 0, -10):
            wn.colormode(255)
            # Generates random colors for the empty circles
            color = (random.randrange(0.0, 255.0, 1.0), random.randrange(0.0, 255.0, 1.0), random.randrange(0.0, 255.0, 1.0))
            DrawCircle(draw, col, row, i, color)

wn.exitonclick()

'''
    [1] Python Documentation[Online]. Available: 
    https://docs.python.org/2/library
    https://docs.python.org/3/library/turtle.html
    https://docs.python.org/2/library/random.html
    
    [2] Stack Overflow. Draw a circle[Online] Available:
    http://stackoverflow.com/questions/4772660/how-to-draw-a-circle-and-a-hexagon-with-the-turtle-module
    
    [3] Python Wiki. For loops[Online]. Available:
    https://wiki.python.org/moin/ForLoop
'''