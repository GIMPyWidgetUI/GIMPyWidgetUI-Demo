import tkinter as tk
from PIL import Image, ImageTk
from GIMPy_Widget_UI import CheckBox_S2 as chk_s2
import ttkbootstrap as ttk

def command_test(message):
    print(message)


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("Checkbox Style2 Demo")
    passive_ui = 'Passive_UI.png'
    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    bg_image_width, bg_image_height = ui_image.size
    canvas = tk.Canvas(root, width=bg_image_width, height=bg_image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo, tags='baseImage')
    canvas.place(x=0, y=0)
    bg_image_width, bg_image_height = ui_image.size
    canvas.pack()

    control_pos_path = "Zoo.txt"

    checkbox_cb_image_paths = ['Tick.png'
                           ,'Unticked.png']

    cb_list = ["zoo#item1", "zoo#item2", "zoo#item3", "zoo#item4", "zoo#item5", "zoo#item6", "zoo#item7",
               "zoo#item8", "zoo#item9", "zoo#item10", "zoo#item11", "zoo#item12", "zoo#item13"]

    for item in cb_list:
        checkbox_cb_polygon = chk_s2.str_to_coordinates(control_pos_path, item, 4)
        checkbox_cb_centroid = chk_s2.find_control_centroid(control_pos_path,"checkbox", item)
        chk_s2(canvas, item, ui_image.size, ui_image,
               checkbox_cb_polygon, checkbox_cb_image_paths, checkbox_cb_centroid, command=command_test)

    root.mainloop()
