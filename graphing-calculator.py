step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

mode = 2 # Modes: 0 - input/output; 1 - graph only; 2 - both; 3 - constantly remake the graph (ONLY DO IF USING RANDOM OR ELSE IT DOESNT CHANGE)
mode3DelayBetweenRegraphs = 0 # Delay between times graphed when mode = 3 (seconds) - Does not take time to graph into account

screenWidth = 600 # Any Integer
screenHeight = 400 # Any Integer

graphAxes = True

dotOrLine = "dot" # Whether to use the dot() function or the line() function when drawing the graph

lineSize = 2 # Size of the line (I recommend keeping it below or at 15)
clearTurtlesBeforeGraph = False # Clear the turtle before it graphs the equation - Useful when mode = 3

useExampleGraph = False # If it should use the example graphs I've made.

# Define equations here.
# Make sure every one starts with 'lambda x: ' (That allows it to call it as a funtion which allows a variable to change after its defined)
# If theres another equation after it it should have a comma after it
# Treat 'lambda x: ' as a 'y = ' when writing equations
equations = [
    lambda x: 0.01 * ((x ** 2) - screenHeight / 2)
]

if useExampleGraph:
    import requests
    exec(requests.get("https://the-tr2nk.web.app/example-equations.txt").text)

# You do not need to modify anything below this line.

# Import libraries
import turtle, math, random, time
try: import numpy # Print statement if numpy isn't installed
except: print("The numpy library is not installed. Please consider installing it.")

graphers = [] # List for the class object
turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"] # Colors for the turtle

# Define the class
class Graph:
    def __init__(self, color, equation, mode, dotsize, graphLine, width, height):
        self.equation = equation # Set the equation function
        self.ycor = 0.0 # Define the variable for later
        self.nan = False # Define the variable for later
        self.lineSize = dotsize # Define the variable for later
        if mode == 1 or mode == 2 or mode == 3: # Define turtle if mode is 1 or 2
            self.turtle = turtle.Turtle() # Turtle object
            self.turtle.pu() # Pen up
            self.turtle.speed(0) # Maximum speed infinity
            if graphLine == 0: # Graph the x andy axis lines
                self.turtle.color("#FFFFFF") # Color white
                self.turtle.pensize(self.lineSize) # Pen size
                self.turtle.goto(0 - width / 2, 0) # Goto one side
                self.turtle.pd() # Pendown
                self.turtle.goto(width / 2, 0) # Goto other side
                self.turtle.pu() # Penup
                self.turtle.goto(0, 0 - height / 2) # Goto the bottom
                self.turtle.pd() # Pendown
                self.turtle.goto(0, height / 2) # Goto the top
                self.turtle.pu() # Penup
            self.turtle.color(color) # Set color

    def graphEquation(self, x): # What to do when graphing mode
        self.ycor = self.equation(x) # Calculate y value
        if math.isnan(float(self.ycor)): self.nan = True # If output is nan then self.nan = True
        else: self.turtle.goto(x, self.ycor); self.nan = False # If it isnt nan then goto correct coords
        if self.nan == False: # If it isn't nan
            self.turtle.dot(self.lineSize) # Make it draw a dot

    def inout(self, x):  # What to do when input/output mode
        try:
            self.vairbale = self.equation(float(x)) # Calculate equation
            if math.isnan(float(self.vairbale)): return "NaN" # If equation output is nan return NaN
            else: return self.vairbale # It not nan return answer
        except: return "Bad Input D:" # If error return bad input

if mode == 1 or mode == 2 or mode == 3: # If mode 1, 2, or 3 then setup turtle window
    screen = turtle.Screen() # Turtle Screen object
    screen.setup(screenWidth, screenHeight) # Screen size
    screen.bgcolor("#333333") # Screen color
    screen.tracer(0) # All actions happen as fast as possible

# Create Graph class object with color and equation
for i in range(len(equations)): graphers.append(Graph(turtleColors[i % 9], equations[i], mode, lineSize, graphAxes, screenWidth, screenHeight)); graphAxes = False

# Create the graph if mode is 1, 2, or 3
while mode == 1 or mode == 2 or mode == 3:
    for o in graphers: # For every equation:
        x = 0 - (screenWidth / 2) # Set minimum x value
        if clearTurtlesBeforeGraph: o.turtle.clear() # Clear the turtle
        for i in range(round((screenWidth / step) + step)):
            o.graphEquation(x) # Graph an equation (one at a time)
            x += step # Increase x by step
    for o in graphers: o.turtle.hideturtle() # Hide turtles

    screen.update() # Update the screen
    
    if mode != 3: break # Break the loop if mode isn't 3
    else: time.sleep(mode3DelayBetweenRegraphs) # Delay if mode is 3

# Do the input/output if mode is 0 or 2
if mode == 0 or mode == 2:
    while True: # Loop forever
        x = input("What x value do you want to find the y values for (decimals supported)?\n") # Input x value
        print("Outputs when x = " + x) # First print statement
        for o in range(len(graphers)): print("Equation " + str(o + 1) + ": " + str(graphers[o].inout(x))) # Print output for each equation
        print("") # New line

# If mode is 1 make sure graph window doesn't instantly close
if mode == 1: screen.mainloop() # Keep screen open after script stops (only does something on independent python where turtle opens a window)