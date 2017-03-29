#Redundant file. Not im use anymore
'''
from Tkinter import *
from PIL import Image, ImageTk, ImageSequence
 
 
class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=500, height=900)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open("C:\Users\hp\Desktop\giphy1.gif"))]
        #width,height=img.size
        self.image = self.canvas.create_image(500, 500, image=self.sequence[0])
        self.animate(1)
 
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(10, lambda: self.animate((counter + 1) % len(self.sequence)))
 
 
root = Tk()
app = App(root)
 
top_frame=Frame(root)
top_frame.pack(side=TOP)
 
def display_input():
    label_temp=Label(top_frame,text=entry_1.get())
    label_temp.pack(side=LEFT,fill=BOTH)
 
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=BOTH)
 
bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)
label_1=Label(bottom_frame,text="Message")
entry_1=Entry(bottom_frame)
 
label_1.pack(side=LEFT,fill=BOTH)
entry_1.pack(side=LEFT,fill=BOTH)
 
button_1=Button(bottom_frame,text="Send",command=display_input)
button_1.pack()
 
root.mainloop()
'''
