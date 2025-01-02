import tkinter as tk
from PIL import Image, ImageTk

from GIMPy_Widget_UI import Btn_S1 as bts1
import ttkbootstrap as ttk

def btn_s1_command_rx(value):
    print(value)

if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("Button - Style 1")
    passive_ui = Image.open("Passive_UI.png").convert("RGBA")
    imagesize = passive_ui.size
    controls_file_loc = 'Buttons_Demo_Position.txt'
    base_photo = ImageTk.PhotoImage(passive_ui)
    image_width, image_height = imagesize
    # Create a canvas and add the image
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=base_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    canvas.pack()


    btn_Africa = bts1("African_Map", canvas,
                      bts1.str_to_coordinates(controls_file_loc, 'African_Map', 4),
                      command=btn_s1_command_rx)
    btn_Aus = bts1("Au_Map", canvas,
                   bts1.str_to_coordinates(controls_file_loc, 'Au_Map', 4),
                   command=btn_s1_command_rx)

    btn_round = bts1("Round_Btn", canvas,
                   bts1.str_to_coordinates(controls_file_loc, 'Round_Btn', 4),
                   command=btn_s1_command_rx)

    btn_silver = bts1("Silver_Btn", canvas,
                   bts1.str_to_coordinates(controls_file_loc, 'Silver_Btn', 4),
                   command=btn_s1_command_rx, press_drag_color=(255, 180, 50))

    root.mainloop()