import keyboard, time, pynput

enabled = 0

h = 0
while h == 0:
    try:
        timeDelay = int(input("Delay (in milliseconds): "))
        h = 1
    except: pass

leftOrRight = ""
while leftOrRight != "l" and leftOrRight != "r": leftOrRight = input("l/r click? ").lower()

print("Press \"g\" to toggle the autoclicker.\nThere is a one second period after you turn it on/off where it doesn't click. This is intended.\nClose this program to stop/close the autoclicker.")

while True:
    if keyboard.is_pressed('g'):
        if enabled == 1:
            enabled = 0
            time.sleep(1)
        else:
            enabled = 1
            time.sleep(1)
    if enabled == 1:
        if timeDelay > 50: time.sleep((timeDelay - 25) / 1000)
        else: time.sleep(timeDelay / 2000)
        if leftOrRight == "l": pynput.mouse.Controller().press(pynput.mouse.Button.left)
        else: pynput.mouse.Controller().press(pynput.mouse.Button.right)
        if timeDelay > 50: time.sleep(25 / 1000)
        else: time.sleep(timeDelay / 2000)
        if leftOrRight == "l": pynput.mouse.Controller().release(pynput.mouse.Button.left)
        else: pynput.mouse.Controller().release(pynput.mouse.Button.right)