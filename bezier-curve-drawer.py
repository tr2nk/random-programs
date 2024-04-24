import turtle
import random

def cubic_bezier_curve(control_points, steps, initialize=None, set_position=None, end_fn=None):
    if initialize:
        initialize()

    for i in range(steps + 1):
        current_step = 1 / steps * i
        new_list = [point for point in control_points]

        while len(new_list) != 1:
            new_list = [([(1 - current_step) * new_list[i][0] + current_step * new_list[i + 1][0], (1 - current_step) * new_list[i][1] + current_step * new_list[i + 1][1]]) for i in range(len(new_list) - 1)]

        if set_position:
            set_position(new_list[0][0], new_list[0][1])

    if end_fn:
        end_fn()

def initialize_turtle():
    global turtle_canvas
    turtle_canvas.clear()
    turtle_canvas.penup()

def set_turtle_position(x, y):
    global turtle_canvas
    turtle_canvas.goto(x, y)
    turtle_canvas.pendown()

def randomize_control_points(x=0, y=0): # Function called on click and at the start
    global control_points, steps

    control_points = [
        [random.randint(-256, 256), random.randint(-128, 128)],
        [random.randint(-256, 256), random.randint(-128, 128)],
        [random.randint(-256, 256), random.randint(-128, 128)]
    ]

    cubic_bezier_curve(control_points, steps, initialize_turtle, set_turtle_position)

steps = 1000

screen = turtle.Screen()
screen.setup(1024, 512)
screen.bgcolor("#002255")
screen.tracer(0)
screen.onclick(randomize_control_points)

turtle_canvas = turtle.Turtle()
turtle_canvas.color("white")
turtle_canvas.hideturtle()
turtle_canvas.penup()

randomize_control_points()

screen.update()
screen.mainloop()
