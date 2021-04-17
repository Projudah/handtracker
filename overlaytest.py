import tkinter as tk
from time import sleep
from overlay import Window


def other_stuff(text):
    '''A simple demonstration. The usage of sleep is to emphasize the effects of each action.'''
    print(text)
    sleep(2)
    win_0.hide()  # Hides the overlay.
    sleep(1)
    win_0.show()  # Shows the overlay.
    sleep(1)
    win_0.focus()  # Sets focus to overlay.
    win_1.center()  # Moves the overlay to the center of the screen.
    sleep(1)
    Window.hide_all()  # Hides all overlays.
    sleep(1)
    Window.show_all()  # Shows all overlays.
    sleep(1)
    win_0.destroy()  # Kills the overlay.
    sleep(1)
    Window.destroy_all()  # Kills all overlays and ends the mainloop.


'''Creates two windows.'''
win_0 = Window()
label_0 = tk.Label(win_0.root, text="Window_0")
label_0.pack()
win_1 = Window()
label_1 = tk.Label(win_1.root, text="Window_1")
label_1.pack()

# Identical to the after method of tkinter.Tk.
Window.after(2000, other_stuff, 'Hello World')

Window.launch()
