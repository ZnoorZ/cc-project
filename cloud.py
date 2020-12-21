from tkinter import *
import requests
from tkinter import ttk as tk




root = Tk()
root.geometry("800x600")

text = Label(root,width=50,height=5,text="Students Management System",font="20")
text.grid(row = 5, column = 6)
   



def create():
    frame=tk.Frame(root)
    frame.place(relheight=2,relwidth=2)
    
    
    def func():
        if marks.get()!="":
            url = 'http://127.0.0.1:5000/adddata'
            x = requests.get(url, params = {"name": name.get() ,"id": id.get() ,"course": course.get() ,"marks": marks.get() })
            print(x.text)
            status.config(text=x.text)
            name.set("")
            id.set("")
            course.set("")
            marks.set("")

    name=StringVar()
    id=StringVar()
    course=StringVar()
    marks=StringVar()
    
    text1 = Label(frame,width=50,height=5,text="**** Create ****",font="20")
    text1.grid(row = 1, column = 1)
        #text = Label(frame,width=50,height=5,text="Students Management System",font="20")
        #text.grid(row = 2, column = 1)

    nl = Label(frame,width=20,height=2,text="Name",font="15")
    nl.grid(row = 3, column = 0)
    il = Label(frame,width=20,height=2,text="Id",font="15")
    il.grid(row = 4, column = 0)
    cl = Label(frame,width=20,height=2,text="Course",font="15")
    cl.grid(row = 5, column = 0)
    ml = Label(frame,width=20,height=4,text="Marks",font="15")
    ml.grid(row = 6, column = 0)
    data1 = Entry(frame,width=50,textvariable=name)
    data1.grid(row = 3, column = 1)
    data2 = Entry(frame,width=50,textvariable=id)
    data2.grid(row = 4, column = 1)
    data3 = Entry(frame,width=50,textvariable=course)
    data3.grid(row = 5, column = 1)
    data4 = Entry(frame,width=50,textvariable=marks)
    data4.grid(row = 6, column = 1)

    status = Label(frame,width=50,height=2,text="Running",font="15")
    status.grid(row =8 , column = 1)
    ok = Button(frame,height =1,width=6, text = "Save",bg="orange",command=func)
    ok.grid(row = 7, column = 1)
    bt1=tk.Button(root,text='DELETE',command=delete)
    bt1.grid(row=0,column=1)
    bt2=tk.Button(root,text='READ',command=read)
    bt2.grid(row=0,column=2)
    bt3=tk.Button(root,text='UPDATE',command=update)
    bt3.grid(row=0,column=3)
    bt4=tk.Button(root,text='back',command=frame.destroy)
    bt4.grid(row=0,column=5)



def delete():
    frame=tk.Frame(root)
    frame.place(relheight=2,relwidth=2) 
    id=StringVar()
    
    def fun():
        url = 'http://127.0.0.1:5000/deldata'
        x = requests.get(url, params = {"id": id.get()})
        print(x.text)
        status.config(text=x.text)
        id.set("")

        
    text1 = Label(frame,width=50,height=5,text="**** Delete ****",font="20")
    text1.grid(row = 1, column = 1)
    #text = Label(frame,width=50,height=5,text="Students Management System",font="20")
    #text.grid(row = 2, column = 1)

    
    il = Label(frame,width=20,height=2,text="Id",font="15")
    il.grid(row = 3, column = 0)
    data2 = Entry(frame,width=50,textvariable=id)
    data2.grid(row = 3, column = 1)

    status = Label(frame,width=50,height=2,text="Running",font="15")
    status.grid(row = 7, column = 1)
    ok = Button(frame,height =1,width=6, text = "Delete",bg="orange",command=fun)
    ok.grid(row = 6, column = 1)
    bt=tk.Button(root,text='CREATE',command=create)
    bt.grid(row=0,column=0)
    bt2=tk.Button(root,text='READ',command=read)
    bt2.grid(row=0,column=2)
    bt3=tk.Button(root,text='UPDATE',command=update)
    bt3.grid(row=0,column=3)
    bt4=tk.Button(root,text='back',command=frame.destroy)
    bt4.grid(row=0,column=5)

   



def read():
    frame=tk.Frame(root)
    frame.place(relheight=2,relwidth=2) 
    def fun1():
        url = 'http://127.0.0.1:5000/finddata'
        x = requests.get(url, params = {"id": id.get()})
        print(x.text)
        status.config(text=x.text)
        id.set("")
   

    text1 = Label(frame,width=50,height=5,text="**** Find ****",font="20")
    text1.grid(row = 1, column = 1)
    #text = Label(frame,width=50,height=5,text="Students Management System",font="20")
    #text.grid(row = 2, column = 1)

    id=StringVar()
    il = Label(frame,width=20,height=2,text="Id",font="15")
    il.grid(row = 3, column = 0)
    data2 = Entry(frame,width=50,textvariable=id)
    data2.grid(row = 3, column = 1)

    status = Label(frame,width=50,height=10,text="Running",font="15")
    status.grid(row = 7, column = 1)
    ok = Button(frame,height =1,width=6, text = "Find",bg="orange",command=fun1)
    ok.grid(row = 6, column = 1)
    
    bt=tk.Button(root,text='CREATE',command=create)
    bt.grid(column=0,row=0)
    bt1=tk.Button(root,text='DELETE',command=delete)
    bt1.grid(row=0,column=1)
    bt3=tk.Button(root,text='UPDATE',command=update)
    bt3.grid(row=0,column=3)
    bt4=tk.Button(root,text='back',command=frame.destroy)
    bt4.grid(row=0,column=5)

    


def update():    
    
    frame=tk.Frame(root)
    frame.place(relheight=2,relwidth=2) 
    def fun3():
        url = 'http://127.0.0.1:5000/getid'
        x = requests.get(url, params = {"id": id.get()})
        print(x.text)
        tmp = x.text.split(",")
        if id.get() == tmp[0]:
            status.config(text="Id Found")
            name.set(tmp[1])
            course.set(tmp[2])
            marks.set(tmp[3])

        else:
            id.set("")
            status.config(text="Id Not Found")

    def funupdate():
        if id.get()!="":
            url = 'http://127.0.0.1:5000/updatedata'
            x = requests.get(url, params = {"name": name.get() ,"id": id.get() ,"course": course.get() ,"marks": marks.get() })
            print(x.text)
            status.config(text=x.text)
            name.set("")
            id.set("")
            course.set("")
            marks.set("")

    text1 = Label(frame,width=50,height=5,text="**** Update ****",font="20")
    text1.grid(row = 1, column = 1)
    text = Label(frame,width=50,height=5,text="Students Management System",font="20")
    text.grid(row = 2, column = 1)

    id=StringVar()
    il = Label(frame,width=20,height=2,text="Id",font="15")
    il.grid(row = 3, column = 0)
    data2 = Entry(frame,width=50,textvariable=id)
    data2.grid(row = 3, column = 1)
    ok = Button(frame,height =1,width=6, text = "Find",bg="orange",command=fun3)
    ok.grid(row = 3, column = 2)

    name=StringVar()
    course=StringVar()
    marks=StringVar()
    nl = Label(frame,width=20,height=2,text="Name",font="15")
    nl.grid(row = 4, column = 0)
    cl = Label(frame,width=20,height=2,text="Course",font="15")
    cl.grid(row = 5, column = 0)
    ml = Label(frame,width=20,height=4,text="Marks",font="15")
    ml.grid(row = 6, column = 0)
    data1 = Entry(frame,width=50,textvariable=name)
    data1.grid(row = 4, column = 1)
    data3 = Entry(frame,width=50,textvariable=course)
    data3.grid(row = 5, column = 1)
    data4 = Entry(frame,width=50,textvariable=marks)
    data4.grid(row = 6, column = 1)

    status = Label(frame,width=50,height=10,text="Running",font="15")
    status.grid(row = 8, column = 1)
    update = Button(frame,height =1,width=6, text = "Update",bg="orange",command=funupdate)
    update.grid(row = 7, column = 1)
    
    bt=tk.Button(root,text='CREATE',command=create)
    bt.grid(column=0,row=0)
    bt1=tk.Button(root,text='DELETE',command=delete)
    bt1.grid(row=0,column=1)
    bt2=tk.Button(root,text='READ',command=read)
    bt2.grid(row=0,column=2)
    bt4=tk.Button(root,text='back',command=frame.destroy)
    bt4.grid(row=0,column=5)


    
    

    


bt=tk.Button(root,text='CREATE',command=create)
bt.grid(column=0,row=0)

bt1=tk.Button(root,text='DELETE',command=delete)
bt1.grid(row=0,column=1)

bt2=tk.Button(root,text='READ',command=read)
bt2.grid(row=0,column=2)

bt3=tk.Button(root,text='UPDATE',command=update)
bt3.grid(row=0,column=3)




root.grid()
root.mainloop()