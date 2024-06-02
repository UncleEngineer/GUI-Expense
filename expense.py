from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

GUI = Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมบันทึกใช้จ่าย')

# FONT CONFIGURE
FONT1 = ('Angsana New',30,'bold')
FONT2 = ('Angsana New',20)

#######TAB######
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab,height=600)
T2 = Frame(Tab,height=600)
Tab.add(T1,text='บันทึก')
Tab.add(T2,text='ดูข้อมูล')
Tab.pack(fill=BOTH,expand=1)




L = Label(T1,text='บันทึกค่าใช้จ่ายในหน้านี้ได้เลย',font=FONT1)
L.pack()
#########################
L = Label(T1,text='รายการค่าใช้จ่าย',font=FONT2)
L.pack()
v_title = StringVar()
E1 = ttk.Entry(T1,textvariable=v_title,font=FONT2,width=50)
E1.pack()
E1.focus()

# def goE2(event):
#     E2.focus()
# E1.bind('<Return>',goE2)
E1.bind('<Return>',lambda x: E2.focus())

#########################
L = Label(T1,text='ราคา',font=FONT2)
L.pack()
v_price = StringVar()
E2 = ttk.Entry(T1,textvariable=v_price,font=FONT2)
E2.pack()
#########################
L = Label(T1,text='ประเภท',font=FONT2)
L.pack()
clist = ['ค่าอาหาร','ค่าเดินทาง','การศึกษา','ค่ารักษาพยาบาล']

D1 = ttk.Combobox(T1,values=clist,font=(FONT2))
D1.pack()
D1.set('ค่าอาหาร')
#########################
F1 = Frame(T1,width=200,height=80)
F1.pack(pady=20)


def save():
    title = v_title.get()
    price = v_price.get()
    ptype = D1.get()

    t = datetime.now().strftime('%Y%m%d-%H:%M:%S')

    with open('data.csv','a',newline='',encoding='utf-8') as f:
        fw = csv.writer(f)
        data = [t,title,price,ptype]
        fw.writerow(data)

    v_title.set('')
    v_price.set('')
    E1.focus()
    readdata_csv()


B = ttk.Button(F1,text='บันทึก',command=save)
B.place(x=0,y=0,width=200,height=80)

# MAC
# B = Button(F1,text='บันทึก')
# B.pack(ipadx=50,ipady=50)

###########################TAB 2###########################
header = ['วัน/เวลา','รายการ','ราคา','หมวดหมู่']
headerw = [150,200,150,180]

expenselist = ttk.Treeview(T2, columns=header, show='headings',height=20)
expenselist.pack()

for h,w in zip(header,headerw):
    expenselist.heading(h,text=h,anchor='center')
    expenselist.column(h,width=w)

expenselist.column('ราคา',anchor='e')

style = ttk.Style()
style.configure('Treeview.Heading',padding=(10,10),font=('Angsana New',20,'bold'))
style.configure('Treeview',rowheight=40,font=('Angsana New',15))

# expenselist.insert('','end',values=['A','B','C','D'])


def readdata_csv():

    #clear
    expenselist.delete(*expenselist.get_children())
    total = []
    with open('data.csv',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
        # print(data)

        for d in data:
            total.append(float(d[2]))

            d[2] = '{:,.2f}'.format(float(d[2]))
            expenselist.insert('','end',values=d)
            
    total = sum(total)
    record = ['','','Total:     {:,.2f}'.format(total),'']
    expenselist.insert('','end',values=record)

try:
    readdata_csv()
except:
    pass

GUI.mainloop()