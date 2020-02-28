import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = 700#(x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)





def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":


    video_name = "test.mp4" #This is your video file path
    video = imageio.get_reader(video_name)

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    marquee = Marquee(root, text="Arnab is amazing", borderwidth=1, relief="sunken",fps=60)
    marquee.pack(side=tk.BOTTOM)


    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()
