from pynput.mouse import Button, Controller
import time

mouse = Controller()


#i = 0
while True:
    mouse.click(Button.left, 1)
    time.sleep(30)