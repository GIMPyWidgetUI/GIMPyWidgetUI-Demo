import ast
import csv
import re
import tkinter as tk
from enum import Enum

import cv2
import numpy as np
from PIL import Image, ImageTk
from GIMPy_Widget_UI import On_Off_Button as OnOff
import ttkbootstrap as ttk

def command_test(message):
    print(message)


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("On Off Button Demo")

    on_off_button_path = 'ON_OFF_MK_Btn.png'
    garage_button_path = 'ON_OFF2_Btn.png'
    passive_ui = 'Passive_UI.png'

    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    bg_image_width, bg_image_height = ui_image.size
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo)
    canvas.place(x=0, y=0)
    bg_image_width, bg_image_height = ui_image.size
    canvas.pack()

    control_poly_path = "ON_OFF_Positions.txt"

    light_button_polygons = [OnOff.str_to_coordinates(control_poly_path, 'MK_ON', 4),
                             OnOff.str_to_coordinates(control_poly_path, 'MK_OFF', 4)]

    light_button_centroids = [OnOff.find_control_centroid(control_poly_path,"ON_OFF", "MK_ON"),
                              OnOff.find_control_centroid(control_poly_path,"ON_OFF", "MK_OFF")]

    Light_Btn = OnOff(canvas, "Light", light_button_polygons, on_off_button_path,
                              light_button_centroids, command=command_test, default_state_is_on=True)

    Garage_button_polygons = [OnOff.str_to_coordinates(control_poly_path, 'Garage_ON', 4),
                             OnOff.str_to_coordinates(control_poly_path, 'Garage_OFF', 4)]

    Garage_button_centroids = [OnOff.find_control_centroid(control_poly_path,"ON_OFF", "Garage_ON"),
                              OnOff.find_control_centroid(control_poly_path,"ON_OFF", "Garage_OFF")]

    Garage_Btn = OnOff(canvas, "Garage", Garage_button_polygons, garage_button_path,
                              Garage_button_centroids, command=command_test)

    print(Light_Btn.Value)
    print(Garage_Btn.Value)

    root.mainloop()
