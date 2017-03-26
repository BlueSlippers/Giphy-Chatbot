from Tkinter import *
from PIL import Image, ImageTk, ImageSequence
import urllib2
import base64
import chat_get, filter, giphy


class App:
    def __init__(self, parent, location):
        self.parent = parent
        self.canvas = Canvas(parent, width=500, height=900)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open(location))]
        # width,height=img.size
        self.image = self.canvas.create_image(500, 500, image=self.sequence[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(10, lambda: self.animate((counter + 1) % len(self.sequence)))


root = Tk()


top_frame = Frame(root)
top_frame.pack(side=TOP)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=BOTH)

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)
label_1 = Label(bottom_frame, text="Message")


label_1.pack(side=LEFT, fill=BOTH)

def display_outputtext(outputtext):
    label_temp2=Label(top_frame,text=outputtext)
    label_temp2.pack(fill=BOTH)

def display_input():
    label_temp = Label(top_frame, text=entry_1.get())
    label_temp.pack(fill=BOTH)
    output_text = chat_get.return_output_text(entry_1.get())
    display_outputtext(output_text)
    gif_input = filter.split_string(output_text)
    url_gif = giphy.get_gif_url(gif_input)
    # DOWNLOADING THE gif and getting the location of that gif which is gonna be stored in "location" variable
    app = App(root, location)


entry_1 = Entry(bottom_frame)  # Input
entry_1.pack(side=LEFT, fill=BOTH)
button_1 = Button(bottom_frame, text="Send", command=display_input)
button_1.pack()

root.mainloop()






