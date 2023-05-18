'''
    def data(s):
        s.product_name = s.pn1.get()
        s.product_category = s.pc1.get()
        s.product_desc = s.pd1.get('1.0',tk.END)
        s.product_price = s.price1.get()
        s.variation = s.colorvar.get('1.0',tk.END)
        
        s.l0 = []
        
        if s.checkbox.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        if s.checkbox2.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        if s.checkbox3.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        if s.checkbox4.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        if s.checkbox5.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        if s.checkbox6.get() == 1:
            s.l0.append('/')
        else:
            s.l0.append('')
        
        s.i = ws.max_row
        s.i+=1
        s.entered_data = [s.i, s.product_name, s.product_category, s.product_desc, s.product_price, s.variation]
        s.final = s.entered_data + s.l0
        print(s.final)
        ws.append(s.final)
        wb.save(path)
        messagebox.showinfo(title='Message', message='Data saved')