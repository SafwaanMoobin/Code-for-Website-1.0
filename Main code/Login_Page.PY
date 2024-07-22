import tkinter as tk
from tkinter import ttk
from tkinter import * 

root = Tk()

# This is the section of code which creates the main window
root.geometry('638x459')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a text input box
Password=Entry(root)
Password.place(x=159, y=215)
# This is the section of code which creates a text input box
Username=Entry(root)
Username.place(x=100, y=215)

# This is the section of code which creates a button
Button(root, text='Login', bg='#00FFFF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=159, y=266)



# This is the section of code which creates the a label
Label(root, text='User login', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=162, y=97)


root.mainloop()



# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Password.get()
	return userInput



# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')

