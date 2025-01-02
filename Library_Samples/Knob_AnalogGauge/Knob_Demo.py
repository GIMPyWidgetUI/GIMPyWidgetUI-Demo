import tkinter as tk
from PIL import Image, ImageTk
# import customtkinter as ctk
from GIMPy_Widget_UI import KnobS1 as knob
from GIMPy_Widget_UI import AnalogGauge as agauge
import ttkbootstrap as ttk


def test_command(value):
    print(f'Test command value={value}')


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    root.title("Knob - Analog Gauge")
    # root.configure(bg="white")
    controls_file_loc = 'Widget_Positions.txt'
    passive_ui = 'Knob_Passive.png'
    ui_image = Image.open(passive_ui).convert("RGBA")
    ui_photo = ImageTk.PhotoImage(ui_image)
    image_width, image_height = ui_image.size
    canvas = tk.Canvas(root, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=ui_photo, tags='baseImage')
    canvas.place(x=0, y=0)

    ac_volt_needle_path = 'AC_Volt_Needle.png'
    ac_volt_needle_image = Image.open(ac_volt_needle_path).convert("RGBA")
    ac_volt_needle_photo = ImageTk.PhotoImage(ac_volt_needle_image)
    analog_gauge_centroid = agauge.find_control_centroid(controls_file_loc,"AnalogGauge", "AC_Volts")
    gauge_x, gauge_y = analog_gauge_centroid[0], analog_gauge_centroid[1]
    canvas.create_image(gauge_x, gauge_y, anchor=tk.CENTER, image=ac_volt_needle_photo, tags='AC_Volt_needle')
    AC_Volt_gauge = agauge(root, canvas, ac_volt_needle_path,gauge_x, gauge_y, 50, 300, 226,
                           'AC_Volt_needle')


    def update_AC_Volt_Gauge(value):
        AC_Volt_gauge.set(value)

    knob_path = 'Knob_Indicator.png'
    knob_image = Image.open(knob_path).convert("RGBA")
    knob_photo = ImageTk.PhotoImage(knob_image)
    knob_centroid = knob.find_control_centroid(controls_file_loc, "Knob", "AC_Knob")
    knob_xy = [knob_centroid[0], knob_centroid[1]]
    knob_range = [50, 300]
    AC_knob = knob(root,canvas,"AC_Volts_Knob",
                       knob_path,knob.str_to_coordinates(controls_file_loc,"AC_Knob",4),
                       knob_xy, knob_range,226, resolution=1, init_angle_rotation=76, command=update_AC_Volt_Gauge)


#****************************************************************

    dc_amp_needle_path = 'DC_Amp_Needle.png'
    dc_amp_needle_image = Image.open(dc_amp_needle_path).convert("RGBA")
    dc_amp_needle_photo = ImageTk.PhotoImage(dc_amp_needle_image)
    analog_gauge_centroid = agauge.find_control_centroid(controls_file_loc,"AnalogGauge", "DC_Amp")
    gauge_x, gauge_y = analog_gauge_centroid[0], analog_gauge_centroid[1]
    dc_max_angle = 90
    knob_range = [-50, 50]
    canvas.create_image(gauge_x, gauge_y, anchor=tk.CENTER, image=dc_amp_needle_photo, tags='DC_Amp_needle')
    DC_Amp_gauge = agauge(root, canvas, dc_amp_needle_path,gauge_x, gauge_y, knob_range[0], knob_range[1], dc_max_angle,
                           'DC_Amp_needle')


    def update_DC_Amp_Gauge(value):
        DC_Amp_gauge.set(value)
        print(value)

    # knob_path = 'Knob_Indicator.png'
    # knob_image = Image.open(knob_path).convert("RGBA")
    # knob_photo = ImageTk.PhotoImage(knob_image)
    #
    # ABOVE 3 are reused from AC Knob declarations
    #
    knob_centroid = knob.find_control_centroid(controls_file_loc, "Knob", "DC_Knob")
    knob_xy = [knob_centroid[0], knob_centroid[1]]
    DC_knob = knob(root,canvas,"DC_Amps_Knob",
                       knob_path,knob.str_to_coordinates(controls_file_loc,"DC_Knob",4),knob_xy,
                       knob_range,180, resolution=2 ,init_angle_rotation=90, command=update_DC_Amp_Gauge)

    canvas.pack()
    root.mainloop()
