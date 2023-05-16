import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

with open("C:/Users/kayth/Desktop/credentials.txt") as c:
    l = c.read().split('\n')
    print(l)

class app():
    def __init__(s): # s for self -shortcut purposes
        s.root = tk.Tk()

        s.root.geometry('300x175')
        s.root.title('DARK STIMULI CLOTHING')

        s.label = tk.Label(s.root, text='Log-in', font=('Arial',18))
        s.label.pack(padx=20,pady=20)

        s.label1 = tk.Label(s.root, text='Username:', font=('Arial', 12))
        s.label1.place(x=30, y=70)

        s.label2 = tk.Label(s.root, text='Password:', font=('Arial', 12))
        s.label2.place(x=30, y=110)

        s.entry = tk.Entry(s.root)
        s.entry.place(x=120, y=70)

        s.entry2 = tk.Entry(s.root)
        s.entry2.bind('<KeyPress>', s.shortcut)
        s.entry2.place(x=120, y=110)
        
        s.root.mainloop()

    def new_window(s):
        s.newwindow = tk.Toplevel(s.root)
        s.newwindow.title('Main Page')
        s.newwindow.geometry('500x800')
        s.newlabel = tk.Label(s.newwindow, text='Main Page', font=('Arial',18))
        s.newlabel.pack()
        s.newbtn = tk.Button(s.newwindow, text = 'Upload', command = s.upload)
        s.newbtn.pack()

        s.newlabel.mainloop()
    '''
    def check(s):
        if s.entry.get() in l and s.entry2.get() in l:
            print(True)
        else:
            messagebox.showinfo(title='Message', message='Invalid username and password') '''
    
    def shortcut(s, event):
        if event.keysym == 'Return' and event.state == 8:
            s.new_window
        elif event.keysym == 'Return' and event.state == 0:
            s.new_window

    def upload(s):
        s.f_types = [('JPG','*.jpg'),('PNG','*.png')]
        s.filename = filedialog.askopenfilename(filetypes=s.f_types)
        s.img = ImageTk.PhotoImage(file=s.filename)
        s.btn = tk.Button(s.newwindow, image = s.img)
        s.btn.grid(row=3, column=1)
            

app()
