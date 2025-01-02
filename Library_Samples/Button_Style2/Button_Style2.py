import re
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from enum import Enum
from GIMPy_Widget_UI import Btn_S2 as bts2
from GIMPy_Widget_UI import Draw_Over_Under
import ttkbootstrap as ttk

def command_test(value):
    print(f"Command test called {value}")


if __name__ == "__main__":
    root = ttk.Window(themename='solar')
    root.title("Button - Style 2")
    passive_ui = (Image.open("Passive_UI.png").convert("RGBA"))
    btns_imagesize = passive_ui.size
    btns_position_file_loc = 'Buttons_Demo_Position.txt'

    base_photo = ImageTk.PhotoImage(passive_ui)
    btns_image_width, btns_image_height = btns_imagesize
    # Create a canvas and add the image
    canvas = tk.Canvas(root, width=btns_image_width, height=btns_image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=base_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    canvas.pack()

    btn1 = bts2("African_Map", canvas, btns_imagesize,
                bts2.str_to_coordinates(btns_position_file_loc,'African_Map', 4), passive_ui,
                drawmode=Draw_Over_Under.UNDER, color_selected=(100, 50, 50, 255), command=command_test)
    btn2 = bts2("Au_Map", canvas, btns_imagesize,
                bts2.str_to_coordinates(btns_position_file_loc,'Au_Map', 4), passive_ui,
                drawmode=Draw_Over_Under.OVER, color_selected=(50, 50, 50, 180), command=command_test)

    btn3 = bts2("Round_Btn", canvas, btns_imagesize,
                bts2.str_to_coordinates(btns_position_file_loc,'Round_Btn', 4), passive_ui,
                drawmode=Draw_Over_Under.OVER, color_selected=(150, 250, 180, 255), command=command_test)

    btn4 = bts2("Silver_Btn", canvas, btns_imagesize,
                bts2.str_to_coordinates(btns_position_file_loc,'Silver_Btn', 4), passive_ui,
                drawmode=Draw_Over_Under.UNDER, color_selected=(214, 100, 150, 185), command=command_test)

    root.mainloop()