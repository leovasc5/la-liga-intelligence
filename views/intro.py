from tkinter import *
import os
from pathlib import Path
from tkinter.font import BOLD

p = Path(os.getcwd())

root = Tk()
root.title("La Liga Intelligence - Loading")
root.iconbitmap(str(p)+"\\assets\\img\\icon.ico")
root.configure(background="#FFFFFF")
labelName = Label(root, text="La Liga 21/22 Intelligence", bg="#FFFFFF", font=(None, 38, BOLD))
labelName.place(relx=0.5, y=200, anchor=CENTER)
photo_path = str(p)+"\\assets\\img\\animation.gif"

frameCnt = 21
frames = [PhotoImage(file=photo_path,format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == (frameCnt):
        ind = 0
        root.destroy()
    label.configure(image=frame, borderwidth=0)
    root.after(100, update, ind)

label = Label(root)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
w = 800
h = 650
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
def disable_event():
    pass

root.overrideredirect(True)
root.after(0, update, 0)
root.mainloop()