import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox



users = {}

def sign_up():
    global users

    # Function to validate username format
    def validate_username(username):
        return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

    # Function to validate email format
    def validate_email(email):
        return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

    # Function to handle sign-up button click
    def sign_up_button_click():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        # Validate username format
        if not validate_username(username):
            messagebox.showerror("Error", "Username must be 3-10 characters long and contain only letters and numbers.")
            return

        # Validate email format
        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format. Please enter in the format 'EmailExample@Organisation.com'.")
            return

        # Store user information in dictionary
        users[username] = {
            'password': password,
            'email': email
        }

        # Clear the entry fields after successful sign-up
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "User successfully registered!")

    # Create the sign-up window
    sign_up_window = tk.Toplevel()
    sign_up_window.geometry('400x300')
    sign_up_window.title('Sign Up')

    # Username label and entry
    tk.Label(sign_up_window, text='Username:').pack()
    username_entry = tk.Entry(sign_up_window, width=30)
    username_entry.pack()

    # Password label and entry
    tk.Label(sign_up_window, text='Password:').pack()
    password_entry = tk.Entry(sign_up_window, show='*', width=30)
    password_entry.pack()


    

    # Email label and entry
    tk.Label(sign_up_window, text='Email:').pack()
    email_entry = tk.Entry(sign_up_window, width=30)
    email_entry.pack()

    # Sign up button
    tk.Button(sign_up_window, text='Sign Up', command=sign_up_button_click).pack()

    sign_up_window.mainloop()

def For_Hire_Page():
    global for_hire

    # Function definitions for "For hire" page buttons
    def onebtnClickFunction():
        print('1')

    def twobtnClickFunction():
        print('2')

    def threebtnClickFunction():
        print('3')

    def fourbtnClickFunction():
        print('4')

    def Back_to_Main_btnClickFunction():
        close_for_hire_page()

    # Create "For hire" page
    for_hire = tk.Tk()
    for_hire.geometry('510x400')
    for_hire.configure(background='#FFEBCD')
    for_hire.title('For Hire')

    # Buttons and labels for "For hire" page
    tk.Button(for_hire, text='Button text!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=onebtnClickFunction).place(x=119, y=165)
    tk.Button(for_hire, text='Button text1!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=twobtnClickFunction).place(x=313, y=164)
    tk.Button(for_hire, text='Button text2!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=threebtnClickFunction).place(x=106, y=353)
    tk.Button(for_hire, text='Button text3!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=fourbtnClickFunction).place(x=314, y=351)
    tk.Button(for_hire, text='Back to main page', bg='#FFEBCD', font=('arial', 15, 'normal'), command=Back_to_Main_btnClickFunction).place(x=299, y=13)
    tk.Label(for_hire, text='Welcome to the extensive amount of people to hire', bg='#FFEBCD', font=('arial', 15, 'normal')).place(x=12, y=91)

    for_hire.mainloop()
Locations = None
def Locations_Page():
    global Locations

    # Function definitions for "Locations" page buttons
    def Location_One_btnClickFunction():
        print('clicked')

    def btnClickFunction():
        print('clicked')

    def Location_three_btnClickFunction():
        print('clicked')

    def Location_Four_btnClickFunction():
        print('clicked')

    def Location_Five_btnClickFunction():
        print('clicked')

    def Location_Six_btnClickFunction():
        print('clicked')
# This is the section of code which creates a combo box
    location_options = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5', 'Location 6']
    location_combobox = ttk.Combobox(Locations, values=location_options, font=('arial', 12, 'normal'), width=20)
    location_combobox.place(x=50, y=100)
    location_combobox.current(0)  # Set the default selection



    # Buttons and labels for "Locations" page
    tk.Label(Locations, text='All the Locations Available', bg='#8B7D6B', font=('arial', 15, 'normal')).place(x=14, y=35)
    tk.Button(Locations, text='Location 1', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_One_btnClickFunction).place(x=76, y=202)
    tk.Button(Locations, text='Location 2', bg='#F5F5DC', font=('arial', 5, 'normal'), command=btnClickFunction).place(x=307, y=204)
    tk.Button(Locations, text='Location 3', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_three_btnClickFunction).place(x=514, y=209)
    tk.Button(Locations, text='Location 4', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Four_btnClickFunction).place(x=76, y=360)
    tk.Button(Locations, text='Location 5', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Five_btnClickFunction).place(x=306, y=359)
    tk.Button(Locations, text='Location 6', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Six_btnClickFunction).place(x=515, y=354)
    tk.Label(Locations, text='Exquisite locations for our valued customers', bg='#8B7D6B', font=('arial', 8, 'normal')).place(x=408, y=14)
    
    Locations.mainloop()

def close_about_page():
    Main_page.destroy()

def close_for_hire_page():
    for_hire.destroy()

def Services_btnClickFunction():
    close_about_page()

def Locations_btnClickFunction():
    global locations_page
    locations_page = tk.Toplevel()
    locations_page.geometry('400x300')
    locations_page.title('Locations')

def About_Us_btnClickFunction():
    global about_page
    about_page = tk.Toplevel(Main_page)
    about_page.geometry('400x300')
    about_page.title('About Us')

    tk.Label(about_page, text='About Us', bg='#B0E0E6', font=('arial', 12, 'normal')).pack(pady=10)

    about_text = """
    Welcome to Xtrive Services!
    
    We are dedicated to providing top-notch services to our customers.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum finibus ex, at blandit dolor sodales a.
    """

    tk.Label(about_page, text=about_text, justify='left', wraplength=380, font=('arial', 10, 'normal')).pack(padx=20, pady=10)

    tk.Button(about_page, text='Close', bg='#FFFFFF', font=('arial', 12, 'normal'), command=close_about_page).pack(pady=10)
    tk.Button(about_page, text='Back to Main', bg='#FFFFFF', font=('arial', 12, 'normal'), command=show_main_window).pack(pady=10)

    about_page.transient(Main_page)  # Set about_page as transient to Main_page
    about_page.grab_set()       # Grab focus to about_page
    Main_page.wait_window(about_page)  # Wait for about_page to be closed

def show_main_window():
    global Main_page
    about_page.destroy()  # Destroy the about_page window
    Main_page.deiconify()      # Show the main window

Main_page = tk.Tk()
Main_page.geometry('512x393')
Main_page.configure(background='#F5f5dc')
Main_page.title('Hello, I\'m the main window')

# Function to create a white frame with specified dimensions
def create_white_frame(x, y, width, height):
    frame = tk.Frame(Main_page, bg='#FFFFFF', width=width, height=height)
    frame.place(x=x, y=y)
    return frame

# Create white frames as backgrounds for the buttons and labels
create_white_frame(0, 100, 512, 50)  # Horizontal line under the labels
create_white_frame(250, 0, 50, 343)  # Vertical line between 'About us' and 'Services'
create_white_frame(390, 50, 50, 600)  # Vertical line between 'Services' and 'Locations'
create_white_frame(250, 100, 263, 50)  # Horizontal line under the buttons

# Labels and buttons on the main page
tk.Label(Main_page, text='Welcome to Xtrive Services', bg='#B0E0E6', font=('arial', 12, 'normal')).place(x=17, y=27)
tk.Button(Main_page, text='About us', bg='#7F675B', font=('arial', 12, 'normal'), command=About_Us_btnClickFunction).place(x=252, y=59)
tk.Button(Main_page, text='Services', bg='#7F675B', font=('arial', 12, 'normal'), command=Services_btnClickFunction).place(x=366, y=58)
tk.Button(Main_page, text='Locations', bg='#7F675B', font=('arial', 12, 'normal'), command=Locations_Page).place(x=361, y=7)
tk.Button(Main_page, text='For hire', bg='#7F675B', font=('arial', 12, 'normal'), command=For_Hire_Page).place(x=259, y=7)
tk.Label(Main_page, text='Information about our website', bg='#B0E0E6', font=('arial', 10, 'normal')).place(x=253, y=103)
tk.Label(Main_page, text='Xtrive', bg='#B0E0E6', font=('arial', 25, 'normal')).place(x=69, y=71)

# Sign up button on the main page
tk.Button(Main_page, text='Sign Up', bg='#7F675B', font=('arial', 12, 'normal'), command=sign_up).place(x=466, y=7)



Main_page.mainloop()




