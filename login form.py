
from tkinter import*
root = Tk()
root.title("login form")
root.geometry('300x300')

l1=Label(root,text='Login Form',fg='white',bg='orange',relief="solid",font=("arial",14,"bold"))
l1.pack(fill=BOTH)

l2=Label(root,text='username')
l2.place(x=50,y=50)

l3=Label(root,text='password')
l3.place(x=50,y=80)

E1=Entry(root)
E1.place(x=120,y=54)

E2=Entry(root)
E2.place(x=120,y=84)

def login():
   a=E1.get()
   b=E2.get()
   if  a=="nishi" and b=="nsk@1234":
      l4=Label(root, text="login success", bg='sky blue',width=20)
      l4.place(x=80,y=170)
   else:
      l4=Label(root, text="login failed", bg='sky blue',width=20)
      l4.place(x=80,y=170)
   db.commit()
   

   

b=Button(root,text='login',bg='dark red',fg='white',width=20,command=login)
b.place(x=80, y=200)


root.mainloop()
