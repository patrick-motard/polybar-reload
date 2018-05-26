import logging
import os
import subprocess
import time

def get_screen_size():
    import os
    from Xlib.display import Display
    display = Display(os.environ.get("DISPLAY",":0.0"))
    root = display.screen().root
    w = root.get_geometry().width
    h = root.get_geometry().height
    return (w,h)

user = os.environ['USER']
reload_polybar = f"sh /home/{user}/.config/polybar/launch.sh"
k = ()

while True:
    j = get_screen_size()
    if j != k:
        process = subprocess.Popen(reload_polybar.split())
        output, error = process.communicate()
    k = j
    time.sleep(1)
