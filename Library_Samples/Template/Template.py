import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
# from GIMPy_Widget_UI import


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("Your Window Title goes here...")
    passive_ui = Image.open("Passive_UI image path goes here...").convert("RGBA")
    imagesize = passive_ui.size
    controls_file_loc = 'Control/Widget position txt file path goes here'
    base_photo = ImageTk.PhotoImage(passive_ui)
    image_width, image_height = imagesize
    # Create a canvas and add the image
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=base_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    canvas.pack()
