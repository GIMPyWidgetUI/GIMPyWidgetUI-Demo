import tkinter as tk
from tkinter import mainloop

from PIL import Image, ImageTk
import ttkbootstrap as ttk
from GIMPy_Widget_UI import Btn_S1 as button
from GIMPy_Widget_UI import Toggle_S1 as toggle


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("ESP RelayBoard")
    passive_ui = Image.open("RelayBoard_Passive.png").convert("RGBA")
    imagesize = passive_ui.size
    controls_file_loc = 'Controls_Positions_File.txt'
    base_photo = ImageTk.PhotoImage(passive_ui)
    image_width, image_height = imagesize
    # Create a canvas and add the image
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=base_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    canvas.pack()

    def relay_clicked(val):
        print(val)

    rl1 = button("Relay1", canvas,
                 button.str_to_coordinates(controls_file_loc,'Relay1',4),command=relay_clicked)

    rl2 = button("Relay2", canvas,
                 button.str_to_coordinates(controls_file_loc,'Relay2',4),command=relay_clicked)
    rl3 = button("Relay3", canvas,
                 button.str_to_coordinates(controls_file_loc,'Relay3',4),command=relay_clicked)
    rl4 = button("Relay4", canvas,
                 button.str_to_coordinates(controls_file_loc,'Relay4',4),command=relay_clicked)

    rl5 = toggle("Relay5", canvas,
                        toggle.str_to_coordinates(controls_file_loc, 'Relay5', 4),
                        command=relay_clicked, default_state=True)

    rl6 = toggle("Relay6", canvas,
                        toggle.str_to_coordinates(controls_file_loc, 'Relay6', 4),
                        command=relay_clicked, default_state=True, press_drag_color=(255,80,50))

    rl7 = toggle("Relay7", canvas,
                        toggle.str_to_coordinates(controls_file_loc, 'Relay7', 4),
                        command=relay_clicked, press_drag_color=(200,0,255))
    rl8 = toggle("Relay8", canvas,
                        toggle.str_to_coordinates(controls_file_loc, 'Relay8', 4),
                        command=relay_clicked, default_state=True, press_drag_color=(0,255,0))
    mainloop()