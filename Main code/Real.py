import tkinter as tk
from tkinter import ttk
from tkinter import * 



#second screen

def screen2():
	# this is a function to get the user input from the text input box
	def getInputBoxValue():
		userInput = Username.get()
		return userInput


	# this is a function to get the user input from the text input box
	def getInputBoxValue():
		userInput = Password.get()
		return userInput


	# this is a function to get the user input from the text input box
	def getInputBoxValue():
		userInput = Email.get()
		return userInput


	# this is the function called when the button is clicked
	def btnClickFunction():
		Screen2.withdraw()



	Screen2 = Tk()

	# This is the section of code which creates the main window
	Screen2.geometry('878x581')
	Screen2.configure(background='#F5F5DC')
	Screen2.title('Login window')


	# This is the section of code which creates a text input box
	Username=Entry(Screen2)
	Username.place(x=181, y=187)


	# This is the section of code which creates a text input box
	Password=Entry(Screen2)
	Password.place(x=180, y=257)


	# This is the section of code which creates a text input box
	Email=Entry(Screen2)
	Email.place(x=180, y=330)


	# This is the section of code which creates the a label
	Label(Screen2, text='Sign up', bg='#F5F5DC', font=('arial', 20, 'normal')).place(x=207, y=91)


	# This is the section of code which creates the a label
	Label(Screen2, text='Find The best results with our companies', bg='#F5F5DC', font=('arial', 20, 'normal')).place(x=32, y=505)


	# This is the section of code which creates a button
	Button(Screen2, text='Sign up ', bg='#A9A9A9', font=('arial', 20, 'normal'), command=btnClickFunction).place(x=177, y=381)






# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Username.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = Password.get()
	return userInput


# this is the function called when the button is clicked
def btnLoginFunction():
	Screen1.destroy()
	
	
def btnSwitchToSignUp():
	Screen1.destroy()
	screen2()


Screen1 = Tk()

# This is the section of code which creates the main window
Screen1.geometry('878x581')
Screen1.configure(background='#F5F5DC')
Screen1.title('Login window')


# This is the section of code which creates a text input box
Username=Entry(Screen1)
Username.place(x=181, y=187)


# This is the section of code which creates a text input box
Password=Entry(Screen1)
Password.place(x=180, y=257)


# This is the section of code which creates a button
Button(Screen1, text='Login', bg='#F5F5DC', font=('arial', 12, 'normal'), command=btnLoginFunction).place(x=181, y=354)
Button(Screen1, text='Switch to sign up page', bg='#F3F5DC', font=('arial', 12, 'normal'), command=btnSwitchToSignUp).place(x=181, y=304)
Button(Screen1, text='Our Team', bg='#F3F5DC', font=('arial', 10, 'normal'), command=btnSwitchToSignUp).place(x=620, y=187)
Button(Screen1, text='Locations', bg='#F3F5DC', font=('arial', 10, 'normal'), command=btnSwitchToSignUp).place(x=620, y=257)





# This is the section of code which creates the a label
Label(Screen1, text='Sign in', bg='#F5F5DC', font=('arial', 20, 'normal')).place(x=204, y=102)


# This is the section of code which creates the a label
Label(Screen1, text='About me', bg='#F5F5DC', font=('arial', 20, 'normal')).place(x=600, y=86)


Screen1.mainloop()

Screen1.mainloop()



def screen3():
# this is the function called when the button is clicked
	def btnClickFunction():
		print('clicked')


# this is the function called when the button is clicked
	def btnClickFunction():
		print('clicked')


# this is the function called when the button is clicked
	def btnClickFunction():
		print('clicked')


# this is the function called when the button is clicked
	def btnClickFunction():
		print('clicked')


# this is the function called when the button is clicked
	def btnClickFunction():
		print('clicked')



	Screen3 = Tk()

# This is the section of code which creates the main window
	Screen3.geometry('623x394')
	Screen3.configure(background='#838B8B')
	Screen3.title('Hello, I\'m the main window')


# This is the section of code which creates the a label
	Label(Screen3, text='Event orginiser', bg='#838B8B', font=('arial', 30, 'normal')).place(x=22, y=39)


# This is the section of code which creates a button
	Button(Screen3, text='Sign in ', bg='#EED5B7', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=370, y=10)


# This is the section of code which creates a button
	Button(Screen3, text='Sign up', bg='#EED5B7', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=466, y=10)


# This is the section of code which creates a button
	Button(Screen3, text='Packages', bg='#EED5B7', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=550, y=10)


# First, we create a canvas to put the picture on
	Ty= Canvas(Screen3, height=100, width=100)
# Then, we actually create the image file to use (it has to be a *.gif)
	picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
	Ty.create_image(100, 0, anchor=NE, image=picture_file)
	Ty.place(x=106, y=117)


# First, we create a canvas to put the picture on
	Image= Canvas(Screen3, height=100, width=100)
# Then, we actually create the image file to use (it has to be a *.gif)
	picture_file = PhotoImage(file = '')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
	Image.create_image(100, 0, anchor=NE, image=picture_file)
	Image.place(x=425, y=117)


# This is the section of code which creates a button
	Button(Screen3, text='Admin ', bg='#EED5B7', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=130, y=239)


# This is the section of code which creates a button
	Button(Screen3, text='About us', bg='#EED5B7', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=443, y=238)


	Screen3.mainloop()

	