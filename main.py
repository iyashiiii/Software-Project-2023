import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

class app():
    def __init__(s):
        s.root = tk.Tk()

        s.root.geometry('300x150')
        s.root.title('Start Page')

        s.label = tk.Label(s.root, text='Enter your name:', font=('Arial',18))
        s.label.pack(padx=20,pady=20)

        s.entry = tk.Entry(s.root)
        s.entry.bind('<KeyPress>', s.shortcut)
        s.entry.pack()

        s.root.mainloop()

    def new_window(s):
        s.newwindow = tk.Toplevel(s.root)
        s.newwindow.title('Main Page')
        s.newwindow.geometry('500x800')
        s.newlabel = tk.Label(s.newwindow, text='Main Page', font=('Arial',18))
        s.newlabel.pack()
        s.newbtn = tk.Button(s.newwindow, text = 'Upload', command = upload())

        s.newlabel.mainloop()
    
    def shortcut(s, event):
        if event.keysym == 'Return' and event.state == 8:
            s.new_window()

    def upload(s):
        s.f_types = [('All files','*.*'),('JPG','*.jpg'),('PNG','*.png')]
        s.filename = filedialog.askopenfilename(filetypes=s.f_types)
        s.img = ImageTk.PhotoImage(file=s.filename)
        s.btn = Button(s.newwindow, image = s.img)
        s.btn.pack(padx = 20, pady = 20)
            

app()
