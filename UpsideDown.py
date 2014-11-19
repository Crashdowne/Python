"""
	CSC 106 Assignment 3 - Upside Down
	
	Marina Retseptor and Bryan Kesteloo
"""
import turtle

# Draw method
def drawTriangle(points,color,myTurtle):
	# Gets the colour to fill
    myTurtle.fillcolor(color)
	# Move pointer up
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
	# Move down
    myTurtle.down()
	# Fills the area with colour
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

# Calculates the midpoint for the drawing of the triangles
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Recursive method
def sierpinski(points,degree,myTurtle):
	# Sets the different colours used to draw
    colormap = ['purple','pink','cyan','grey','black',
                'cyan','orange']
	# Calls the draw triangle method
    drawTriangle(points,colormap[degree],myTurtle)
	# Base case degree > 0
    if degree > 0:
        sierpinski([points[0],
						# Starts the drawing at the midpoint and moves out from there
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   # Sets the points of the triangle in the xy plane
   #			points[0] points[1]	points[2]
   myPoints = [[200,100],[0,-100],[-200,100]]
   # Calls the recursive method, gives it a base case of degree 3
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()

"""
	[1] Interactive Python. Visualizing Recursion[Online]. Available: 
	http://interactivepython.org/runestone/static/pythonds/Recursion/graphical.html
"""