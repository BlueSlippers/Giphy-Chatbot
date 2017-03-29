##Redundant. Not used. 
'''from Tkinter import *


root = Tk()

top_frame = Frame(root)
top_frame.pack(side=TOP)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=BOTH)

bottom_frame = Frame(root,bg='#48C9B0')
bottom_frame.pack(side=BOTTOM)
#label_1 = Label(bottom_frame, text="Message",bg='#48C9B0')

#label_1.pack(side=LEFT, fill=BOTH)


def display_input():
    label_temp = Label(top_frame, text=entry_1.get(), fg='#85C1E9', anchor='sw')
    label_temp.pack(fill=BOTH)
    display_outputtext("Hello")


def display_outputtext(outputtext):
    label_temp2 = Label(top_frame, text=outputtext)
    label_temp2.pack(fill=BOTH)


entry_1 = Entry(bottom_frame)  # Inpu
entry_1.pack(side=LEFT, fill=BOTH)
button_1 = Button(bottom_frame, text="Send", command=display_input, activebackground= '#2E86C1', activeforeground='#ECF0F1',
                  bg='#3498DB', fg='#ECF0F1', bd= 5, height=1,width=10, font='Serif')
button_1.pack()



root.mainloop()
'''
