import tkinter as tk
from tkinter import Entry, Button, Label

# Function to switch to the sign-up screen
def switch_to_signup():
    root.withdraw()  # Hide the login window
    signup_window.deiconify()  # Show the signup window

# Function to perform login
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Check username and password validity here
    print("Logged in as:", username)

# Function to perform signup
def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    email = email_entry.get()
    # Store user details or perform signup process here
    print("Signed up with:", username, password, email)

# Create the main window
root = tk.Tk()
root.title('Login')

# Create login widgets
Label(root, text='Username:').pack()
username_entry = Entry(root)
username_entry.pack()

Label(root, text='Password:').pack()
password_entry = Entry(root, show="*")
password_entry.pack()

Button(root, text='Login', command=login).pack()
Button(root, text='Switch to Sign Up', command=switch_to_signup).pack()

# Create the signup window
signup_window = tk.Toplevel(root)
signup_window.title('Sign Up')
signup_window.withdraw()  # Hide the signup window initially

# Create signup widgets
Label(signup_window, text='Username:').pack()
signup_username_entry = Entry(signup_window)
signup_username_entry.pack()

Label(signup_window, text='Password:').pack()
signup_password_entry = Entry(signup_window, show="*")
signup_password_entry.pack()

Label(signup_window, text='Email:').pack()
email_entry = Entry(signup_window)
email_entry.pack()

Button(signup_window, text='Sign Up', command=signup).pack()

root.mainloop()