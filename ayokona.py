import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

with open("C:/Users/kayth/Desktop/credentials.txt") as c:
    l = c.read().split('\n')

# FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def check():
    return check2()

def check2():
    txt = entry1.get()
    txt2 = entry2.get()
    if txt in l and txt2 in l:
        new_window()
    else:
        messagebox.showinfo(title='Message', message='Invalid username and password')
        
def new_window():
    main = tk.Toplevel(root)
    main.title('Main Page')
    main.geometry('500x800')
    newlabel = tk.Label(main, text='Main Page', font=('Arial',18))
    newlabel.pack()
    newbtn = tk.Button(main, text = 'Upload', command = upload)
    newbtn.pack()

    newlabel.mainloop()
    
def upload():
    f_types = [('JPG','*.jpg'),('PNG','*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    btn = tk.Button(main, image = img)
    btn.grid(row=3, column=1)


# LOGIN PAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
root = tk.Tk()

root.geometry('300x190')
root.title('DARK STIMULI CLOTHING')

label = tk.Label(root, text='Log-in', font=('Arial',18))
label.pack(padx=20,pady=20)

label1 = tk.Label(root, text='Username:', font=('Arial', 12))
label1.place(x=30, y=70)

label2 = tk.Label(root, text='Password:', font=('Arial', 12))
label2.place(x=30, y=110)

entry1 = tk.Entry(root)
entry1.place(x=120, y=70)

entry2 = tk.Entry(root)
entry2.place(x=120, y=110)

btn = tk.Button(root, text='Login', command = check)
btn.place(x=160, y=150)

root.mainloop()

        


