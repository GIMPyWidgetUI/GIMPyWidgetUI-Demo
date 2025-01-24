import vlc
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog

class CircleButton(tk.Canvas):
    def __init__(self,  btn_name, master=None, x=50, y=50, radius=20,
                 command=None, btn_text ='', text_size = None, color=(255, 255, 254), **kwargs):
        super().__init__(master, width=2*radius, height=2*radius, **kwargs)
        self.radius = radius
        self.text_size = text_size
        self.btn_name = btn_name
        self.btn_text = btn_text
        self.color = color
        self.radius = radius
        self.command = command
        self.oval = self.create_oval(2, 2, radius*2-2, radius*2-2, tags=self.btn_name, fill=self.__rgb_to_hex(self.color),
                         outline = self.__rgb_to_hex(self.color), width=2)
        self.text = self.create_text(radius+1, radius+1, text=self.btn_text, anchor=tk.CENTER, tags=self.btn_name,
                                     font=("Helvetica", self.radius // 3 if self.text_size is None else self.text_size),
                                     fill='white')

        self.tag_bind(btn_name, "<ButtonPress-1>", self.__top_layer_mouse_dn)
        self.tag_bind(btn_name, "<ButtonRelease-1>", self.on_release)
        # self.configure(relief='groove', borderwidth=0)
        self.place(x=x, y=y)
        # self.tag_bind(self.btn_name, "<Button-1>", self.on_press)


    def __rgb_to_hex(self, rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    def __top_layer_mouse_dn(self, event):
        x, y = event.x, event.y
        closesttag = self.find_closest(event.x, event.y)
        tag_name = self.gettags(closesttag)

        # print(tag_name)
        pressed_color = (self.color[0]-20 if self.color[0] > 20 else self.color[0] ,
                         self.color[1]-20 if self.color[1] > 20 else self.color[1],
                         self.color[2]-20 if self.color[2] > 20 else self.color[2])

        self.itemconfig(self.oval, fill=self.__rgb_to_hex(pressed_color),
                               outline=self.__rgb_to_hex(self.color), width=4)

        self.itemconfig(self.text, font=("Helvetica",
                        (self.radius // 3 if self.text_size is None else self.text_size)-2))
        self.move(self.text, 0, 0)

    def on_release(self, event):
        x, y = event.x, event.y
        closesttag = self.find_closest(event.x, event.y)
        tag_name = self.gettags(closesttag)

        self.itemconfig(self.oval, fill=self.__rgb_to_hex(self.color),
                               outline=self.__rgb_to_hex(self.color), width=4)
        self.itemconfig(self.text, font=("Helvetica", self.radius // 3 if self.text_size is None else self.text_size))
        self.move(self.text, -0, -0)
        if self.command is not None and len(tag_name)>1 and tag_name[1] == 'current':
            self.command()

class Video:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player

    def open_file(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if video_path:
            media = self.player.get_instance().media_new(video_path)
            self.player.set_media(media)
            self.player.set_hwnd(self.canvas.winfo_id())

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def rewind(self):
        self.player.set_time(self.player.get_time() - 10000)  # Rewind 10 seconds

    def forward(self):
        self.player.set_time(self.player.get_time() + 10000)  # Forward 10 seconds

    def volume_up(self):
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(volume + 10)  # Increase volume by 10

    def volume_down(self):
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(volume - 10)  # Decrease volume by 10

class VideoPlayer:
    def __init__(self, root, canvas, btns_x=0, btns_y=0):
        self.root = root
        self.btns_x = btns_x
        self.btns_y = btns_y
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.video = Video(canvas, self.player)
        self.canvas = canvas
        self.create_ui()

    def exit(self):
        self.player.stop()
        self.root.destroy()

    def create_ui(self):
        self.controls_frame = ttk.Frame(self.root, height=100, width=500)
        self.controls_frame.place(x=self.btns_x, y=self.btns_y)

        self.open_button = CircleButton('btnOpen' ,self.controls_frame,10, 0,30, btn_text='Open',
                                        color=(250, 110, 130), command=self.video.open_file)

        self.play_button = CircleButton('btnPlay' ,self.controls_frame,70, 0,30, btn_text='Play',
                                        color=(250, 110, 130), command=self.video.play)

        self.pause_button = CircleButton('btnPause' ,self.controls_frame,130, 0,30,
                                        btn_text='Pause', color=(250, 110, 130), command=self.video.pause)

        self.forward_button = CircleButton('btnForward' ,self.controls_frame,190, 0,30
                                        , btn_text='Forward',color=(250, 110, 130), command=self.video.forward)

        self.rewind_button = CircleButton('btnRewind' ,self.controls_frame,250, 0,30
                                        , btn_text='Rewind',color=(250, 110, 130), command=self.video.rewind)

        self.vol_dn_button = CircleButton('btnVol_dn' ,self.controls_frame,310, 0,30
                                        , btn_text='Vol-',color=(250, 110, 130), command=self.video.volume_down)

        self.vol_up_button = CircleButton('btnVol_up' ,self.controls_frame,370, 0,30
                                        , btn_text='Vol+',color=(250, 110, 130), command=self.video.volume_up)

        self.exit_button = CircleButton('btnExit' ,self.controls_frame,430, 0,30
                                        , btn_text='Exit',color=(200,50,10), command=self.exit)


if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    # root = tk.Tk()
    root.title("Video Player")
    root.geometry("700x800")

    canvas1 = tk.Canvas(root, bg='black')
    canvas1.place(x=0, y=0, width=700, height=650)

    player1 = VideoPlayer(root, canvas1, btns_x=80, btns_y=700)

    root.mainloop()
