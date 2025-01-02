import tkinter as tk
from PIL import Image, ImageTk
# import customtkinter as ctk
from GIMPy_Widget_UI import AnalogGauge as agauge
from GIMPy_Widget_UI import SliderGaugeS1 as slider, SliderUPPERLOWER
import ttkbootstrap as ttk


def test_command(value):
    print(f'Test command value={value}')


if __name__ == "__main__":
    root = ttk.Window()
    root.title("Analog Gauge + Slider Demo")
    root.configure(bg="white")
    controls_file_loc = 'Widget_Positions.txt'
    passive_ui = 'Passive_UI_DC_Amp.png'
    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    image_width, image_height = ui_image.size
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo, tags='baseImage')
    canvas.place(x=0, y=0)

    dc_amp_needle_path = 'DC_Amp_Needle.png'
    dc_amp_needle_image = Image.open(dc_amp_needle_path).convert("RGBA")
    dc_amp_needle_photo = ImageTk.PhotoImage(dc_amp_needle_image)
    analog_gauge_centroid = agauge.find_control_centroid(controls_file_loc,"AnalogGauge", "DC_Amp")
    gauge_x, gauge_y = analog_gauge_centroid[0], analog_gauge_centroid[1]
    canvas.create_image(gauge_x, gauge_y, anchor=tk.CENTER, image=dc_amp_needle_photo, tags='DC_Amp_needle')

    gauge_DC_Amp = agauge(root, canvas, dc_amp_needle_path, gauge_x, gauge_y, -50,
                          50, 90, 'DC_Amp_needle')


    def update_DC_gauge(Value):
        print(Value)
        val = Value.split(',')[2]
        print(float(val))
        gauge_DC_Amp.set(float(val))

    slider_paths =  ['DC_Amp_Slider_Indicator.png',
                     'DC_Amp_Slider_Indicator.png']

    slider_range = [-50,50]
    DC_meter_slider = slider(root,canvas,"DC_Slider",slider_paths,
                      slider.str_to_coordinates(controls_file_loc, 'DC_Slider', 4),
                      slider_range, slider_range,False, resolution=1, command=update_DC_gauge)
    DC_meter_slider.set(SliderUPPERLOWER.UPPER,0)


    canvas.pack()

    root.mainloop()
