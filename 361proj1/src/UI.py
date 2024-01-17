# Author: Robin Shindelman
# Date: 2023-01-11
# Description: This is the user interface for project 1. There should be two
# buttons on implementation: a visualize otter button, and a quit button. 

import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
from time import sleep


# ---------------- Functions ----------------
def visualize_otter():
    """
    Display image on the screen. Handles all communication with calls
    to other funcs and finally renders the image on the screen.
    :params: None
    :return: None
    """
    num = numGen_comm()
    path = image_comm(num)
    image_render(path)

def numGen_comm():
    """
    Handle the communication pipeline: UI.py <--> numGen.py 
    :params: None
    :return: 
    line1: A random number of type string.
    """
    numGen_pipe = '/Users/robinshindelman/repos/school/361.SE1/361proj1/src/prng_service.txt'
    # Send 'run' to numGen.py
    with open(numGen_pipe, 'w') as comm:
        comm.write('run')

    # Receive 'num' from numGen.py
    line1 = ''
    sleep(1)
    with open(numGen_pipe, 'r') as comm:
        line1 = comm.readline()

    # Clear the pipes!
    comm = open(numGen_pipe, 'w')
    comm.close()
    return line1

def image_comm(num):
    """
    Handle the communication pipeline: UI.py <--> image.py
    :params: 
    num: pseudo-random generated number originating in numGen.py, routed through
         UI.py
    :return: 
    line1: Should be an image pathway based in ./images/
    """
    image_pipe = '/Users/robinshindelman/repos/school/361.SE1/361proj1/src/img_service.txt'
    # Send 'num' to image.py
    with open(image_pipe, 'w') as comm:
        comm.write(num)

    # Receive 'path' from numGen.py
    line1 = ''
    sleep(1)
    with open(image_pipe, 'r') as comm:
        line1 = comm.readline()

    # Clear the pipes!
    comm = open(image_pipe, 'w')
    comm.close()
    return line1

def image_render(path):
    """
    Handle the actual image rendering in the GUI.
    Sorry about all the comments, still learning how to use Tkinter.
    :params: 
    path: Pathway to one of the images randomly selected in the ./images/ dir.
    :return: None
    """
    # Image is a PIL module, open() handles actually opening the image pathway.
    img = Image.open(path)
    # ImageTk is a PIL module which using PhotoImage() converts the image data
    # into something readable by the Tkinter GUI.
    img = ImageTk.PhotoImage(img)
    # TopLevel is part of Tkinter, it generates a new window on top of the root
    # window.
    result_win = Toplevel(root)
    result_win.title('Otter')
    # tk.Label() is a weird name for a method that displays an image, but it
    # can display both images and text.
    render = tk.Label(result_win, image=img)
    # Keeps the image on the screen until it's closed manually.
    render.image = img
    render.pack()


# ---------------- My GUI scripting ----------------
root = tk.Tk()
root.geometry("600x400")
title_font = 'Garamond', 30
button_font = 'Garamond', 20

root.title('Otter Visualizer')

heading = tk.Label(root, 
                   text='Visualize an Otter Today! \n Press Quit to exit.', 
                   font=title_font,
                   pady=20)
heading.pack()

visualizer = tk.Button(root, 
                       text='Otter it up',
                       width=15,
                       height=3,
                       command=visualize_otter)
visualizer.pack()

root.mainloop()
