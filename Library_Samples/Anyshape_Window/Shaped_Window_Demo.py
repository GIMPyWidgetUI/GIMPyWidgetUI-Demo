import sys
import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from GIMPy_Widget_UI import ShapedWindow as shaped_window
from GIMPy_Widget_UI import Btn_S1 as button

def start_move(event, root, start_pos):
    start_pos[0] = event.x
    start_pos[1] = event.y
    closesttag = canvas.find_closest(event.x, event.y)
    tag_name = canvas.gettags(closesttag)

    if tag_name[0] == "baseImage":
        root.bind("<B1-Motion>", lambda e: move_window(e, root, start_pos))
    else:
        root.unbind("<B1-Motion>")

def move_window(event, root, from_pos):
    dx = event.x - from_pos[0]
    dy = event.y - from_pos[1]
    root.geometry(f"+{root.winfo_x() + dx}+{root.winfo_y() + dy}")

def quit_command(val):
    shaped_window.quit()

def minimise_window(val):
    shaped_window.minimise_window(root)

if __name__ == "__main__":
    root = ttk.Window()
    root.attributes("-topmost", True)
    root.wm_title("Game Controller")
    start_pos = [0, 0]

    root.wm_attributes('-transparentcolor', 'white')

    root.bind("<Button-1>", lambda event: start_move(event, root, start_pos))

    canvas = tk.Canvas(root, width=600, height=600, bg='gray', highlightthickness=0)
    canvas.pack()

    controls_file_loc = 'Positions.txt'
    canvas.create_polygon(shaped_window.str_to_coordinates(controls_file_loc,'root_window_shape',4),
                          outline='gray', fill='', width=15)

    passive_ui = Image.open("Controller_Passive.png").convert("RGBA")
    imagesize = passive_ui.size
    base_photo = ImageTk.PhotoImage(passive_ui)
    image_width, image_height = imagesize
    # Create a canvas and add the image
    canvas.create_image(0, 0, anchor=tk.NW, image=base_photo, tags='baseImage')
    root.place_window_center()
    root.update_idletasks()
    root.overrideredirect(True)

    close_button = button('Quit', canvas,
                          button.str_to_coordinates(controls_file_loc,'Quit',4),
                          command=lambda q: shaped_window.quit())

    minimise_button = button('Minimise', canvas,
                          button.str_to_coordinates(controls_file_loc,'Minimise',4),
                          command=lambda q:shaped_window.minimise_window(root))

    root.mainloop()