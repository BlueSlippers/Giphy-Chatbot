from Tkinter import *
from PIL import Image, ImageTk, ImageSequence


class App:
    def __init__(self, parent, location):
        self.parent = parent
        self.canvas = Canvas(parent, width=500, height=900)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open(location))]
        self.image = self.canvas.create_image(300, 200, image=self.sequence[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter + 1) % len(self.sequence)))

'''
root = Tk()
app = App(root)
root.mainloop()
'''
