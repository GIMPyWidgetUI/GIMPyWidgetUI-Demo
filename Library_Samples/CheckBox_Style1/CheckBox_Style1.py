import ast
import csv
import re
import tkinter as tk
from enum import Enum

import cv2
import numpy as np
from PIL import Image, ImageTk
from GIMPy_Widget_UI import CheckBox_S1 as chk_s1
import ttkbootstrap as ttk

def command_test(message):
    print(message)


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("Checkbox Demo - Style 1")
    passive_ui = 'Passive_UI.png'
    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    ui_image_width, ui_image_height = ui_image.size
    canvas = tk.Canvas(root, width=ui_image_width, height=ui_image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    ui_image_width, ui_image_height = ui_image.size
    canvas.pack()

    control_poly_path = "check_box_position.png.txt"

    checkbox_cb_polygon = chk_s1.str_to_coordinates(control_poly_path, 'menu_order#Ice_Cream', 4)

    checkbox_cb_image_paths = ['CheckBox_TickMark_3d.png'
                           ,'CheckBox_unselected.png']

    checkbox_cb_centroid = chk_s1.find_control_centroid(control_poly_path,"checkbox", "menu_order#Ice_Cream")

    cb = chk_s1(canvas, "menu_order#Ice_Cream", checkbox_cb_polygon, checkbox_cb_image_paths,
                checkbox_cb_centroid, command=command_test)
    cb.set(True)
    root.mainloop()
