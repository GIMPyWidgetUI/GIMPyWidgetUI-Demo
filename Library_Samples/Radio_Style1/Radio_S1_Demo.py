import tkinter as tk
import re

from PIL import Image, ImageTk, ImageDraw
import cv2
import numpy as np
import ttkbootstrap as ttk
from GIMPy_Widget_UI import RadioS1 as radio_s1

def command_test(value):
    print("Command test executed, value=" + value)


if __name__ == "__main__":
    root = ttk.Window()
    root.title("Radio Style 1 Demo")
    passive_ui = 'Radio_Demo_Passive.png'
    control_poly_path = "Radio1_Positions.txt"

    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    image_width, image_height = ui_image.size
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    canvas.pack()


    radio_s1('Play*CD', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'Play*CD', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('Play*Cassette', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'Play*Cassette', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('Play*Vinyl', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'Play*Vinyl', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('Play*USB', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'Play*USB', 4), command=command_test, stipple_color=(0, 255, 255), default=True)


    radio_s1('grp2*Min', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'grp2*Min', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('grp2*Low', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'grp2*Low', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('grp2*Max', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'grp2*Max', 4), command=command_test, stipple_color=(0, 255, 255))
    radio_s1('grp2*Med', canvas, radio_s1.str_to_coordinates(control_poly_path,
             'grp2*Med', 4), command=command_test, stipple_color=(0, 255, 255), default=True)



    root.mainloop()