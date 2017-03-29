from Tkinter import *
import mechanize
import re
import giphy

###Mechanize set-up
url = "http://elbot_e.csoica.artificial-solutions.com/cgi-bin/elbot.cgi"
br = mechanize.Browser()
br.set_handle_robots(False)

#br.open(cache.base_url)
br.open( url )
# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
###Finised setting of virtual browser

###Setting of Regex values
regex = '<style><.+?></style>'
regex1 = '(?<=-->)(.*)(?=<!)'
pattern = re.compile(regex1)
###Done

def Return_output( string ):
    br.select_form(nr=0)
    br.form['ENTRY'] = string
    response = br.submit()
    text = response.read()
    reply = re.findall(pattern, text)
    return reply


window = Tk()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=BOTH)

counter = 1
def enter_pressed(event):

    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text=input_get)
    input_user.set('')
    label.pack()
    
    global counter
    output_label = Label(frame, text =Return_output(input_get))
    
    giphy.download_gif(Return_output(input_get),counter)
    
    output_label.pack()

    counter+=1
    return "break"

frame = Frame(window, width=300, height=300)
frame.pack_propagate(False) # prevent frame to resize to the labels size
input_field.bind("<Return>", enter_pressed)
frame.pack()



window.mainloop()
