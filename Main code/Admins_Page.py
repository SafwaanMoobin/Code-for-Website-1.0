import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunction():
	print("x")


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('580x495')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a button
Button(root, text='Orginisation', bg='#EE7621', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=402, y=281)


# This is the section of code which creates a button
Button(root, text='Admin', bg='#CD5B45', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=232, y=284)


# This is the section of code which creates a button
Button(root, text='User', bg='#CD5B45', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=60, y=284)


# This is the section of code which creates the a label
Label(root, text='Sign UP', bg='#F0F8FF', font=('arial', 34, 'normal')).place(x=186, y=85)


root.mainloop()



import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Password.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = UserName.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('638x459')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a text input box
Password=Entry(root)
Password.place(x=159, y=215)


# This is the section of code which creates a button
Button(root, text='Login', bg='#00FFFF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=159, y=266)


# This is the section of code which creates a text input box
UserName=Entry(root)
UserName.place(x=158, y=154)


# This is the section of code which creates the a label
Label(root, text='OrGinisation', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=156, y=85)


root.mainloop()









import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Password.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction(x):
	
	print('Hello')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = UserName.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('638x459')
root.configure(background='#F0F8FF')
root.title('Admins Login Page')


# This is the section of code which creates a text input box
Password=Entry(root)
Password.place(x=159, y=215)


# This is the section of code which creates a button
Button(root, text='Login', bg='#00FFFF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=159, y=266)


# This is the section of code which creates a text input box
UserName=Entry(root)
UserName.place(x=158, y=154)


# This is the section of code which creates the a label
Label(root, text='Admins User', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=159, y=95)


root.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Password.get()
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = UserName.get()
	return userInput



root = Tk()

# This is the section of code which creates the main window
root.geometry('638x459')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates a text input box
Password=Entry(root)
Password.place(x=159, y=215)


# This is the section of code which creates a button
Button(root, text='Login', bg='#00FFFF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=159, y=266)


# This is the section of code which creates a text input box
UserName=Entry(root)
UserName.place(x=158, y=154)


# This is the section of code which creates the a label
Label(root, text='User login', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=162, y=97)


root.mainloop()
