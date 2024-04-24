from turtle import Turtle, Screen

scr = Screen()
scr.setup(1000, 1000)
scr.tracer(0)
scr.bgcolor("#cccccc")
scr.title("Click to 10")

number = -1

turt = Turtle()
turt.pu()
turt.ht()

def write(x, y):
    global number
    turt.clear()
    number += 1
    turt.write(str(number), align = "center", font = ("Arial", 24, "normal"))
    if number == 10:
        scr.bye()
    else:
        scr.update()

scr.onclick(write)

write(0, 0)

scr.mainloop()
