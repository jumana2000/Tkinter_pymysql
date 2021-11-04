from tkinter import *
import tkinter.messagebox
import pymysql
from PIL import ImageTk, Image


t=tkinter.Tk()
t.title('Add Employee')
t.geometry('700x500')

image=Image.open('C:\\Users\\jumana\\Desktop\\Employee\\Emp.jpg')
image=image.resize((700,500))
image=ImageTk.PhotoImage(image)
pic=tkinter.Label(t,image=image)
pic.place(x=0,y=0)


heading=tkinter.Label(text='Add Employee',bg='lightblue',fg='black',font=('times new roman',30,'bold'))
heading.place(x=150,y=5)

name=tkinter.Label(text='Name',bg='lightblue',fg='black',font=('times new roman',20,'bold'))
name.place(x=90,y=100)

name_entry=tkinter.Entry(width=30)
name_entry.place(x=240,y=110)

age=tkinter.Label(text='Age',bg='lightblue',fg='black',font=('times new roman',20,'bold'))
age.place(x=90,y=170)

age_entry=tkinter.Entry(width=30)
age_entry.place(x=240,y=180)


location=tkinter.Label(text='Location',bg='lightblue',fg='black',font=('times new roman',20,'bold'))
location.place(x=90,y=250)

location_entry=tkinter.Entry(width=30)
location_entry.place(x=240,y=260)


def add():
    name=name_entry.get()
    age=age_entry.get()
    location=location_entry.get()


    if(name=="" or location=="" or age==""):
        tkinter.messagebox.showerror("Error","Please fill the fields!!!")
    else:
        x=pymysql.connect(host='localhost',user='root',password='password',db='employee')
        cr=x.cursor()

        cr.execute("insert into e_table values('"+name+"','"+age+"','"+location+"')")
        x.commit()
        x.close()
        
        tkinter.messagebox.showinfo('Thank You','Thank You for visiting')
        t.destroy()
    

f=tkinter.Button(text='Add',command=add,bg='lightblue',fg='black',font=('times new roman',15,'bold'))
f.place(x=225,y=300)


def view():
    import pymysql
    x=pymysql.connect(host='localhost',
                  user='root',
                  password='password',
                  db='employee')
    cur=x.cursor()
    
    tx=tkinter.Text(height=6,width=50)
    tx.place(x=50,y=370)
    
    cur.execute('select * from e_table')
    v=cur.fetchall()
    for i in v:
        tx.insert(INSERT,(i))
        
    


tkinter.Button(text='View Data',command=view,bg='lightblue',fg='black',font=('times new roman',15,'bold')).place(x=550,y=400)


t.mainloop()
