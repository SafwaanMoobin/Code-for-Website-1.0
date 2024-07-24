import tkinter as tk
from tkinter import messagebox
import csv

# Dictionary to store user information
users = {}

# Function to load users from CSV file
def load_users():
    try:
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password, email = row
                users[username] = {'password': password, 'email': email}
    except FileNotFoundError:
        pass

# Load users from CSV file at the start
load_users()

# Function to validate the username
def validate_username(username):
    return 3 <= len(username) <= 10 and username.isalnum()

# Dummy function to check sign-in status
def check_sign_in(username, password):
    return username in users and users[username]['password'] == password

# Function to handle login button click
def handle_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if check_sign_in(username, password):
        Main_Page()
    else:
        messagebox.showerror("Error", "Invalid username or password. Please try again.")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to represent main page transition
def Main_Page():
    main_page = tk.Tk()
    main_page.geometry('512x393')
    main_page.configure(background='#F5f5dc')
    main_page.title('Hello, I\'m the main window')

    # Function to create a white frame with specified dimensions
    def create_white_frame(x, y, width, height):
        frame = tk.Frame(main_page, bg='#FFFFFF', width=width, height=height)
        frame.place(x=x, y=y)
        return frame

    # Create white frames as backgrounds for the buttons and labels
    create_white_frame(0, 100, 512, 50)  # Horizontal line under the labels
    create_white_frame(250, 0, 50, 343)  # Vertical line between 'About us' and 'Services'
    create_white_frame(390, 50, 50, 600)  # Vertical line between 'Services' and 'Locations'
    create_white_frame(250, 100, 263, 50)  # Horizontal line under the buttons

    tk.Label(main_page, text='Welcome to Xtrive Services', bg='#B0E0E6', font=('arial', 12, 'normal')).place(x=17, y=27)
    tk.Button(main_page, text='About us', bg='#7F675B', font=('arial', 12, 'normal')).place(x=252, y=59)
    tk.Button(main_page, text='Services', bg='#7F675B', font=('arial', 12, 'normal')).place(x=366, y=58)
    tk.Button(main_page, text='Locations', bg='#7F675B', font=('arial', 12, 'normal')).place(x=361, y=7)
    tk.Button(main_page, text='For hire', bg='#7F675B', font=('arial', 12, 'normal')).place(x=259, y=7)
    tk.Label(main_page, text='Information about our website', bg='#B0E0E6', font=('arial', 10, 'normal')).place(x=253, y=103)
    tk.Label(main_page, text='Xtrive', bg='#B0E0E6', font=('arial', 25, 'normal')).place(x=69, y=71)

    main_page.mainloop()

# Create the login page
login_page = tk.Tk()
login_page.title("Login")
login_page.geometry('512x393')
login_page.configure(background='#F5f5dc')

# Username label and entry
tk.Label(login_page, text='Username:', bg='#F5f5dc', font=('arial', 12, 'normal')).place(x=150, y=150)
username_entry = tk.Entry(login_page, width=30)
username_entry.place(x=250, y=150)

# Password label and entry
tk.Label(login_page, text='Password:', bg='#F5f5dc', font=('arial', 12, 'normal')).place(x=150, y=200)
password_entry = tk.Entry(login_page, show='*', width=30)
password_entry.place(x=250, y=200)

# Login button
login_button = tk.Button(login_page, text='Login', bg='#7F675B', font=('arial', 12, 'normal'), command=lambda: handle_login(username_entry, password_entry))
login_button.place(x=400, y=235)

login_page.mainloop()
