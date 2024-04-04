# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd

dataset = pd.read_csv("C:/Users/whynew/OneDrive/Desktop/New folder/Salary_Data.csv")
dataset.isnull().sum()


X = dataset.iloc[:,0:1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.30,random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()


regressor.fit(X_train, y_train)


'''
y_pred = regressor.predict(X_test)

regressor.score(X_train, y_train)

regressor.score(X_test, y_test)


from sklearn.metrics import r2_score
r2_score(y_test,y_pred)
'''
#deployment

import tkinter as tk
root = tk.Tk()
root.title('Linear regression')
root.geometry('300x250')

#creating Labels
L_simple = tk.Label(root,text='simple Linear Regression\n(salary prediction)',font='Times 11 bold',
                    bg='Light blue',width=35)
L_simple.place(x=30,y=30)

Label = tk.Label(root,text='year of experience')
Label.place(x=50,y=90)

Label1=tk.Entry(root)
Label1.place(x=160,y=90)

def predict1():
    experience=float(Label1.get())
    
    y_pred = regressor.predict([[experience]])
    y=np.round((y_pred),2)
    y_pred = "".join([str(i) for i in y])

    pred1=tk.Label(root,text=('The predicted salary is{}'.format(y_pred)),width=35)    
    pred1.place(x=30,y=130)
    
predict1 = tk.Button(root,text='Predict salary',bg='orange',command=predict1,width=20)
predict1.place(x=80,y=160)

root.mainloop()    
    
    



















