import mouse
import time

def handle_click(*args, **kwargs):
    print('Press!!!')


# mouse.on_click(lambda: print("Left Button clicked."))
# mouse.on_right_click(lambda: print("Right Button clicked."))
mouse.on_button(callback=handle_click, buttons=['x'], types=['up'])
time.sleep(5)
