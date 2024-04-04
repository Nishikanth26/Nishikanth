import tkinter as tk

root =tk.Tk()
root.title("nishi")
root.geometry('400x400')

#creating table
L1=tk.Label(root, text='BMI Calculator', font='Times 14 bold',bg='sky blue',width=37)
L1.place(x=0, y=0)

L2=tk.Label(root, text='height meteres',font='Times 12 bold')
L2.place(x=80, y=80)

L3=tk.Label(root, text='weight kg',font='Times 12 bold')
L3.place(x=80, y=120)

#creating entry box
e1=tk.Entry(root)
e1.place(x=200, y=84)

e2=tk.Entry(root)
e2.place(x=200, y=124)

#creating function for button
def bmi():
    h=e1.get()
    w=e2.get()
    bmi=round((float(w)/float(h)**2),2)

    L1=tk.Label(root, text=('your BMI is:()'.format(bmi)), font='Times 12')
    L1.place(x=135, y=215)

    if(bmi <=18.5):
        l2=tk.Label(root, text="yor are underweight!",font='time 12',bg='light blue', width=30)
        l2.place(x=62, y=250)

    if(18.5<bmi<=24.9):
        l2=tk.Label(root, text="yor are weight is normal!",font='time 12',bg='light green', width=30)
        l2.place(x=62, y=250)

    if(25<bmi <=29.29):
        l2=tk.Label(root, text="yor are overweight!",font='time 12',bg='red', width=30)
        l2.place(x=62, y=250)

    else:
        l2=tk.Label(root, text="yor are is obese!",font='time 12',bg='orange', width=30)
        l2.place(x=62, y=250)

#creating buttons
button=tk.Button(root,text='BMI ', font='Times 12 bold',bg='orange',width=30,command=bmi)
button.place(x=60, y=250)


root.mainloop()




















    
