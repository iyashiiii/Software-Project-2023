# ESSENTIAL FILES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #1. main.py    -- main program
    #2. admin.txt  -- admin username and password
    #3. excel file -- for overall database

# IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import sqlite3

# ADMIN ACCESS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(r"C:\Users\kayth\Desktop\admin.txt") as c:
    l = c.read().split('\n')
  
# INITIAL WINDOW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class app():
    def __init__(s): # s for self -shortcut purposes
        
        s.root = tk.Tk()

        s.root.geometry('330x190')
        s.root.title('DARK STIMULI CLOTHING')

        s.label = tk.Label(s.root, text='Log-in', font=('Arial',12))
        s.label.pack(padx=20,pady=20)

        s.label1 = tk.Label(s.root, text='Username:', font=('Arial', 12))
        s.label1.place(x=30, y=70)

        s.label2 = tk.Label(s.root, text='Password:', font=('Arial', 12))
        s.label2.place(x=30, y=110)

        s.entry1 = tk.Entry(s.root, bg='#DADEDF')
        s.entry1.place(x=120, y=70)     
        
        s.entry2 = tk.Entry(s.root, bg='#DADEDF')
        s.entry2.place(x=120, y=110)
        
        s.btn = tk.Button(s.root, text='Login', command = s.check)
        s.btn.place(x=160, y=150)
        
        
        
        s.root.mainloop()

# FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# check if user is an admin ---
    def check(s):
        s.txt = s.entry1.get()
        s.txt2 = s.entry2.get()
        if s.txt in l and s.txt2 in l:
            s.new_window()
        else:
            messagebox.showerror(title='Message', message='Invalid username and password')
            
# upload function for product image --
    def upload(s):
        s.f_types = [('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')]
        s.filename = filedialog.askopenfilename(filetypes=s.f_types)
        s.img = Image.open(s.filename)
        s.img = s.img.resize((300,300))
        s.img = ImageTk.PhotoImage(s.img)
        
        
        s.frameupload = tk.Frame(s.win)
        s.frameupload.columnconfigure(0, weight=1)
        s.frameupload.columnconfigure(1, weight=1)
        s.frameupload.columnconfigure(2, weight=1)
        
        s.picture = tk.Label(s.frameupload, image = s.img)
        s.picture.grid(row=0, column=0)
        
        s.frameupload.pack()
        
# place data in excel from New Product page -- 
    def data(s):
        s.cb_xs = ''
        s.cb_s = ''
        s.cb_m = ''
        s.cb_l = ''
        s.cb_xl = ''
        s.cb_xl = ''
        s.cb_xxl = ''
        
        if s.checkbox.get() == 1:
            s.cb_xs = '/'
        
        if s.checkbox2.get() == 1:
            s.cb_s = '/'
       
        if s.checkbox3.get() == 1:
            s.cb_m = '/'
       
        if s.checkbox4.get() == 1:
            s.cb_l = '/'
        
        if s.checkbox5.get() == 1:
            s.cb_xl = '/'
       
        if s.checkbox6.get() == 1:
            s.cb_xxl = '/'
        
        s.fob = open(s.filename, 'rb')
        s.blob_data = s.fob.read()
        
               
        s.product_name = s.pn1.get()
        s.product_category = s.pc1.get()
        s.product_desc = s.pd1.get('1.0',tk.END)
        s.product_price = s.price1.get()
        
        s.conn = sqlite3.connect('data.db')
        s.table = '''CREATE TABLE IF NOT EXISTS Clothing_Management
                (Product_Name TEXT, Product_image blob, Category TEXT, Description TEXT, Price INT, XS TEXT, S TEXT, M TEXT, L TEXT, XL TEXT, XXL TEXT, Stock INT, Sales INT) '''
        s.conn.execute(s.table)
        
        s.insert = '''INSERT INTO Clothing_Management (Product_Name, Product_image, Category, Description, Price, XS, S, M, L, XL, XXL, Stock, Sales) VALUES 
                (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        s.var = (s.product_name, s.blob_data , s.product_category, s.product_desc, s.product_price, s.cb_xs, s.cb_s, s.cb_m, s.cb_l, s.cb_xl, s.cb_xxl, 0, 0)
        s.cursor = s.conn.cursor()
        s.cursor.execute(s.insert, s.var)
        s.conn.commit()
        
        
        
        s.conn.close()
        messagebox.showinfo(title='Message', message='Data Saved')
        


# place sales data in excel from Enter Sales page -- 
    def data_label(s):
        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]
        print(s.liss)
        s.chosen_product = [s.menu.get()]
        s.chosen_product1 = s.chosen_product[0]
        print(s.chosen_product)
        s.checking = '''SELECT Sales from Clothing_Management WHERE Product_Name = ?'''

        s.cursor.execute(s.checking, s.chosen_product)
        s.gg = s.cursor.fetchone()
        
        
        print(s.gg)
        print(s.gg[0])
        print(s.sales.get(),)
        s.ggfinal = s.gg[0] + int(s.sales.get(),)
        s.forsales = '''UPDATE Clothing_Management SET Sales = ? WHERE Product_Name = ?''' 
        s.finall = (s.ggfinal, s.chosen_product1)
        
        for i in s.liss:
            if i in s.chosen_product:
                s.cursor.execute(s.forsales, s.finall)
                messagebox.showinfo(title='Message', message='Data Saved')
            
        
        s.conn.commit()
        s.conn.close()
        
    def data_label2(s):
        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]
        print(s.liss)
        s.chosen_product = [s.menu.get()]
        s.chosen_product1 = s.chosen_product[0]
        print(s.chosen_product)
        s.checking = '''SELECT Sales from Clothing_Management WHERE Product_Name = ?'''

        s.cursor.execute(s.checking, s.chosen_product)
        s.gg = s.cursor.fetchone()
        
        
        print(s.gg)
        print(s.gg[0])
        print(s.sales3.get(),)
        s.ggfinal = s.gg[0] - int(s.sales3.get(),)
        s.forsales = '''UPDATE Clothing_Management SET Sales = ? WHERE Product_Name = ?''' 
        s.finall = (s.ggfinal, s.chosen_product1)
        
        for i in s.liss:
            if i in s.chosen_product:
                s.cursor.execute(s.forsales, s.finall)
                messagebox.showinfo(title='Message', message='Data Saved')
            
        
        s.conn.commit()
        s.conn.close()
    
    def data_label3(s):
        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]
        print(s.liss)
        s.chosen_product = [s.menuw.get()]
        s.chosen_product1 = s.chosen_product[0]

        s.checking = '''SELECT Stock from Clothing_Management WHERE Product_Name = ?'''

        s.cursor.execute(s.checking, s.chosen_product)
        s.gg = s.cursor.fetchone()
        
    
        s.ggfinal = s.gg[0] + int(s.salesw.get(),)
        s.forsales = '''UPDATE Clothing_Management SET Stock = ? WHERE Product_Name = ?''' 
        s.finall = (s.ggfinal, s.chosen_product1)
        
        for i in s.liss:
            if i in s.chosen_product:
                s.cursor.execute(s.forsales, s.finall)
                messagebox.showinfo(title='Message', message='Data Saved')
            
            
        
        
        s.conn.commit()
        s.conn.close()
        
        
    def data_label4(s):
        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]
        print(s.liss)
        s.chosen_product = [s.menuw.get()]
        s.chosen_product1 = s.chosen_product[0]
        print(s.chosen_product)
        s.checking = '''SELECT Stock from Clothing_Management WHERE Product_Name = ?'''

        s.cursor.execute(s.checking, s.chosen_product)
        s.gg = s.cursor.fetchone()
        
        
        print(s.gg)
        print(s.gg[0])
        print(s.sales3x.get(),)
        s.ggfinal = s.gg[0] - int(s.sales3x.get(),)
        s.forsales = '''UPDATE Clothing_Management SET Stock = ? WHERE Product_Name = ?''' 
        s.finall = (s.ggfinal, s.chosen_product1)
        
        for i in s.liss:
            if i in s.chosen_product:
                s.cursor.execute(s.forsales, s.finall)
                messagebox.showinfo(title='Message', message='Data Saved')
            
        
        
        s.conn.commit()
        s.conn.close()
        
    def data_label5(s):
        s.gget = [s.menuw.get()]
        
        s.prnm = tk.Label(s.win4, text=f'Product: {s.gget[0]}', font=('Verdana 16 bold italic'), height=2)
        s.prnm.pack(padx = 20, pady = 5, anchor='nw')#(x=90, y=30)
        
        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        
        s.checkprice = '''SELECT Price from Clothing_Management WHERE Product_Name = ?'''
        s.checkstock = '''SELECT Stock from Clothing_Management WHERE Product_Name = ?'''
        s.checksales = '''SELECT Sales from Clothing_Management WHERE Product_Name = ?'''
        
        s.cursor.execute(s.checkprice, s.gget)
        
        s.price__ = s.cursor.fetchone()
        
        s.price_ = s.price__[0]
        print(s.price_)
        
        s.cursor.execute(s.checkstock, s.gget)
        
        s.stock__ = s.cursor.fetchone()
        s.stock_ = s.stock__[0]
        
        s.cursor.execute(s.checksales, s.gget)
        
        s.sales__ = s.cursor.fetchone()
        s.sales_ = s.sales__[0]
        
        s.prnm2 = tk.Label(s.win4, text=f'Price: P{s.price_}', font=('Verdana 12'))
        s.prnm2.pack(padx = 20, pady = 5, anchor='nw')#(x=90, y=30)
        
        s.prnm3 = tk.Label(s.win4, text=f'Current stock: {s.stock_}', font=('Verdana 12'))
        s.prnm3.pack(padx = 20, pady = 5, anchor='nw')#(x=90, y=30)
        
        s.prnm4 = tk.Label(s.win4, text=f'Currently sold: {s.sales_}', font=('Verdana 12'))
        s.prnm4.pack(padx = 20, pady = 5, anchor='nw')#(x=90, y=30)
        
        s.tsales = int(s.price_) * int(s.sales_)
        
        
        s.totalsales = tk.Label(s.win4, text=f'Total Sales: Php {s.tsales}', font=('Verdana 16 bold'))
        s.totalsales.pack(padx = 20, pady = 5, anchor='nw')#(x=90, y=30)
    ''' 
    def handle(s):
        
        s.new_window
        s.win.destroy()
    
        
    def handle2(s):
        s.win2.destroy()
        s.new_window
    
    def handle3(s):
        s.win3.destroy()
        s.new_window
    
    def handle4(s):
        s.win4.destroy()
        s.new_window'''
# SECONDARY WINDOWS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Main Page selection for all function --
    def new_window(s):
        s.main = tk.Tk()
        s.main.title('Main Page')
        s.main.geometry('500x400')
        s.newlabel = tk.Label(s.main, text='What would you like to do?', font=('Arial 20 underline'), height=3)
        s.newlabel.pack(fill='x')#(x=90, y=30)
        
        s.frame = tk.Frame(s.main)
        s.frame.columnconfigure(0, weight=1)
        
        s.btn1 = tk.Button(s.frame, text='New product', font=('Arial', 18), background='#FEFEBE', command = s.window1)
        s.btn1.grid(row=0, column=0, sticky='news')
        
        s.btn2 = tk.Button(s.frame, text='Enter sales', font=('Arial', 18), background='#C7F6B6', command = s.window2)
        s.btn2.grid(row=1, column=0, sticky='news')
        
        s.btn3 = tk.Button(s.frame, text='Manage inventory', font=('Arial', 18), background='#F4E3FF', command = s.window3)
        s.btn3.grid(row=2, column=0, sticky='news')
        
        s.btn4 = tk.Button(s.frame, text='Product stats', font=('Arial', 18), background='#FBBF77', command = s.window4)
        s.btn4.grid(row=3, column=0, sticky='news')
        
        s.frame.pack(fill='x')
        
        s.close = tk.Button(s.main, text='Close', font=('Arial', 16), width=8, background='#FFCBCB')
        s.close.pack(side='bottom', pady=30)
        
        s.root.destroy()
        

        s.main.mainloop()
        
        
        
        
# New Product page --       
    def window1(s):
        s.win = tk.Tk()
        s.win.title('New product')
        s.win.geometry('500x800')
        s.pn = tk.Label(s.win, text='Product Name:', font=('Arial',12))
        s.pn.pack(padx=10,pady=2, anchor='nw')
        
        s.pn1 = tk.Entry(s.win, width=50, bg='#DADEDF')
        s.pn1.place(x=120,y=5)
        
        s.pc = tk.Label(s.win, text='Product Category:', font=('Arial',12))
        s.pc.pack(padx=10,pady=2, anchor='nw')
        
        s.pc1 = tk.Entry(s.win, width=50, bg='#DADEDF')
        s.pc1.place(x=145,y=35)
        
        s.pd = tk.Label(s.win, text='Short Product Description:', font=('Arial',12))
        s.pd.pack(padx=10,pady=2, anchor='nw')

        s.pd1 = tk.Text(s.win, height=3, background='#DADEDF')
        s.pd1.pack(padx=10,pady=2)
        
        s.price = tk.Label(s.win, text='Product Price: (number only)', font=('Arial',12))
        s.price.pack(padx=10,pady=2, anchor='nw')
        
        s.price1 = tk.Entry(s.win, width=30, bg='#DADEDF')
        s.price1.place(x=218,y=146)
        
        s.cl = tk.Label(s.win, text='Available Sizes:', font=('Arial', 12))
        s.cl.pack(padx=10,pady=2, anchor='nw')
        
        s.checkbox = tk.IntVar()
        s.checkbox2 = tk.IntVar()
        s.checkbox3 = tk.IntVar()
        s.checkbox4 = tk.IntVar()
        s.checkbox5 = tk.IntVar()
        s.checkbox6 = tk.IntVar()
        
        s.c = tk.Checkbutton(s.win, text='XS', font=('Arial', 8), variable=s.checkbox, bg='#DADEDF')
        s.c.pack(padx=10,pady=2, anchor='nw')
        
        s.c2 = tk.Checkbutton(s.win, text='S', font=('Arial', 8), variable=s.checkbox2, bg='#DADEDF')
        s.c2.pack(padx=10,pady=2, anchor='nw')
        
        s.c3 = tk.Checkbutton(s.win, text='M', font=('Arial', 8), variable=s.checkbox3, bg='#DADEDF')
        s.c3.pack(padx=10,pady=2, anchor='nw')
        
        s.c4 = tk.Checkbutton(s.win, text='L', font=('Arial', 8), variable=s.checkbox4, bg='#DADEDF')
        s.c4.pack(padx=10,pady=2, anchor='nw')
        
        s.c5 = tk.Checkbutton(s.win, text='XL', font=('Arial', 8), variable=s.checkbox5, bg='#DADEDF')
        s.c5.pack(padx=10,pady=2, anchor='nw')
         
        s.c6 = tk.Checkbutton(s.win, text='XXL', font=('Arial', 8), variable=s.checkbox6, bg='#DADEDF')
        s.c6.pack(padx=10,pady=2, anchor='nw')
        
        s.upl = tk.Button(s.win, text = 'Upload Product Image & Preview', font=('Arial', 10), background='#DADEDF', command = s.upload)
        s.upl.pack(padx=10,pady=20,anchor='nw')
        
        s.submit = tk.Button(s.win, text='Submit', font=('Arial', 16), width=8, background='#FFCBCB', command = s.data)
        s.submit.pack(side='bottom', pady=20)
        
        
        s.win.mainloop()

# Enter Sales page --         
    def window2(s):
        s.win2 = tk.Tk()
        s.win2.title('Enter sales')
        s.win2.geometry('600x450')
        
        s.label2 = tk.Label(s.win2, text='Select a product and enter sales for today', font=('Arial',20), height=3)
        s.label2.pack(fill='x')#(x=90, y=30)
        

        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.menu = StringVar()
        s.drop = ttk.Combobox(s.win2, width=15, textvariable = s.menu)
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]

        s.conn.commit()
        s.conn.close()
        
        s.drop['values'] = (s.liss)       
        s.drop.pack()
        s.drop.current()
        
        s.sales = tk.Entry(s.win2, width=15, bg='#DADEDF')
        s.sales.pack(pady = 20)
        
        s.submitsales = tk.Button(s.win2, text='Submit', font=('Arial', 12), width=8, background='#FFCBCB', command = s.data_label)
        s.submitsales.pack(side='top', pady=20)
        
        s.label3 = tk.Label(s.win2, text='Or enter sales deduction:', font=('Arial',20), height=1)
        s.label3.pack(fill='x')#(x=90, y=30)
        
        s.sales3 = tk.Entry(s.win2, width=15, bg='#DADEDF')
        s.sales3.pack(pady = 20)
        
        s.submitsales3 = tk.Button(s.win2, text='Submit', font=('Arial', 12), width=8, background='#FFCBCB', command = s.data_label2)
        s.submitsales3.pack(side='bottom', pady=20)
        
        
        s.win2.mainloop()
       
    def window3(s):
        s.win3 = tk.Tk()
        s.win3.title('Inventory')
        s.win3.geometry('600x450')
        
        s.labelw = tk.Label(s.win3, text='Select a product and enter no. of stocks', font=('Arial',20), height=3)
        s.labelw.pack(fill='x')#(x=90, y=30)
        

        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.menuw = StringVar()
        s.dropw = ttk.Combobox(s.win3, width=15, textvariable = s.menuw)
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]

        s.conn.commit()
        s.conn.close()
        
        s.dropw['values'] = (s.liss)       
        s.dropw.pack()
        s.dropw.current()
        
        s.salesw = tk.Entry(s.win3, width=15, bg='#DADEDF')
        s.salesw.pack(pady = 20)
        
        s.submitsales = tk.Button(s.win3, text='Submit', font=('Arial', 12), width=8, background='#FFCBCB', command = s.data_label3)
        s.submitsales.pack(side='top', pady=20)
        
        s.label3 = tk.Label(s.win3, text='Or enter stock deduction:', font=('Arial',20), height=1)
        s.label3.pack(fill='x')#(x=90, y=30)
        
        s.sales3x = tk.Entry(s.win3, width=15, bg='#DADEDF')
        s.sales3x.pack(pady = 20)
        
        s.submitsales3x = tk.Button(s.win3, text='Submit', font=('Arial', 12), width=8, background='#FFCBCB', command = s.data_label4)
        s.submitsales3x.pack(side='bottom', pady=20)
        
        
        s.win3.mainloop()
    
    def window4(s):
        s.win4 = tk.Tk()
        s.win4.title('Product Stats')
        s.win4.geometry('300x450')
        
        s.label44 = tk.Label(s.win4, text='Product Stats', font=('Arial',20), height=3)
        s.label44.pack(fill='x')#(x=90, y=30)
        

        s.conn = sqlite3.connect('data.db')
        s.cursor = s.conn.cursor()
        s.cursor.execute('''SELECT Product_Name from Clothing_Management''')
        s.f = s.cursor.fetchall()
        
        s.menuw = StringVar()
        s.dropw = ttk.Combobox(s.win4, width=15, textvariable = s.menuw)
        
        s.lis = [str(i) for i in s.f]
        s.liss = [i[2:-3] for i in s.lis]

        s.conn.commit()
        s.conn.close()
        
        s.dropw['values'] = (s.liss)       
        s.dropw.pack()
        s.dropw.current()
        
        
        
        s.show = tk.Button(s.win4, text='Show', font=('Arial', 12), width=8, background='#FFCBCB', command = s.data_label5)
        s.show.pack(side='bottom', pady=20)

        s.win4.mainloop()
app()
