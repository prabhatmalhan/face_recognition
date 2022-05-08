import tkinter.filedialog as fd
from tkinter import *
from camCapture import capture
import os
from editConfig import EditConfig as EC

ec = EC(os.path.join("..", "config.json"))


def captureCam():
    name = input.get(1.0, "end-1c")
    if name == '':
        name = 'extra'

    id = str(ec.countSamples())
    print(ec.addSample(name))
    name = id

    root = os.path.join('..', 'resources')
    try:
        os.mkdir(os.path.join(root, name))
    except:
        pass
    capture(name)


def captureVid():
    name = input.get(1.0, "end-1c")
    if name == '':
        name = 'extra'

    id = str(ec.countSamples())
    print(ec.addSample(name))
    name = id

    filename = fd.askopenfilename(title='Open a video', initialdir='/')
    if filename == '':
        return
    root = os.path.join('..', 'resources')
    try:
        os.mkdir(os.path.join(root, name))
    except:
        pass

    capture(name, filename)


root = Tk()
root.geometry("200x200+500+50")
input = Text(root, height=1, width=20)
input.place(x=25, y=25)
cap = Button(root, text='Camera', width=15, command=lambda: captureCam())
cap.place(x=45, y=65)
cap2 = Button(root, text='Video', width=15, command=lambda: captureVid())
cap2.place(x=45, y=105)

root.mainloop()
