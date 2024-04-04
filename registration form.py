from tkinter import ttk
from tkinter import*
window=Tk()
window.geometry('300x450')

L1=Label(window,text="Registration Form",relief="solid",font=('times new roman',16,'bold'))
L1.place(x=50,y=0)

L2=Label(window,text='Enter your name')
L2.place(x=0,y=60)

L3=Label(window,text='Enter your surname')
L3.place(x=0,y=90)

L4=Label(window,text='Enter your email ')
L4.place(x=0,y=120)

L5=Label(window,text='Select your gender ')
L5.place(x=0,y=150)

#create entry box
name=StringVar()
E1=Entry(window,textvariable=name)
E1.place(x=150,y=60)

surname=StringVar()
E2=Entry(window,textvariable=surname)
E2.place(x=150,y=90)

email=StringVar()
E3=Entry(window,textvariable=email)
E3.place(x=150,y=120)

#create combo box
male_female=StringVar()
combo1=ttk.Combobox(window,state='readonly',textvariable=male_female)
combo1['values']=("male","female","other")
combo1.current(0)#by default it will select automatically
combo1.place(x=150,y=150)

#create radio box
usertype=StringVar()
r1=ttk.Radiobutton(window,text='student',value='student',variable=usertype)
r1.place(x=20,y=180)

r2=ttk.Radiobutton(window,text='teacher',value='teacher',variable=usertype)
r2.place(x=120,y=180)


#check box

checkbox=IntVar()
check1=ttk.Checkbutton(window,text="check for latest update",variable=checkbox)
check1.place(x=0,y=220)


#button

def button():
    names=name.get()
    surnames=surname.get()
    emails=email.get()
    Mf=male_female.get()
    abc=usertype.get()
    if checkbox.get()==0:
        checked="checke the check box button"
    else:
        checked="you have successfully checked check box button"
    
    #print(f"your name {names}\n your surname {surnames}\n your email {emails}")
    #print(f" yor are {abc}\n your gender {Mf}")
    #print(checked)

    all_details=(f"your name is {names} \nyour surname is {surnames} \nyour email is {emails} \nyor are {abc} \nyour gender is {Mf} \n{checked}")
    details=Label(window,text=all_details)
    details.place(x=0,y=290)


b1=Button(window,text="submit",command=button)
b1.place(x=190,y=260)

window.mainloop()
