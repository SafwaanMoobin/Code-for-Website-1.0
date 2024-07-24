import tkinter as tk
from tkcalendar import Calendar
import re
import tkinter.messagebox as messagebox
from tkinter import * 
import csv


selected_dates = []


def store_date(date):
    selected_dates.append(date)
    print("Stored dates:", selected_dates)


def on_date_selected(event):
    selected_date = cal.selection_get()
    print("Selected date:", selected_date)
    store_date(selected_date.strftime('%Y-%m-%d'))

def validate_and_store_date():
    user_input = date_entry.get()
    # Check if the input matches the YYYY-MM-DD format
    if re.match(r"\d{4}-\d{2}-\d{2}", user_input):
        try:
            year, month, day = map(int, user_input.split('-'))
            # Check if the date is valid
            if 1 <= month <= 12 and 1 <= day <= 31:  # Basic validation, can be improved
                store_date(user_input)
            else:
                print("Invalid date")
        except ValueError:
            print("Invalid date")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")



# Initialize empty users dictionary
users = {}

# Function to validate username format
def validate_username(username):
    return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

# Function to validate email format
def validate_email(email):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

# Function to read existing users from users.csv
def load_users():
    try:
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                username, password, email = row
                users[username] = {'password': password, 'email': email}
    except FileNotFoundError:
        # Handle the case where users.csv doesn't exist yet
        pass

# Load existing users when the program starts
load_users()

# Function to handle sign-up button click
def sign_up_button_click(username_entry, password_entry, email_entry):
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

    # Check if username already exists
    if username in users:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return

    # Store user information in dictionary
    users[username] = {
        'password': password,
        'email': email
    }

    # Write user information to CSV file immediately
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([username, password, email])

    # Clear the entry fields after successful sign-up
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "User successfully registered!")

# Function to handle sign-up window creation
def sign_up():
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
    tk.Button(sign_up_window, text='Sign Up', command=lambda: sign_up_button_click(username_entry, password_entry, email_entry)).pack()

    sign_up_window.mainloop()


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


def create_calendar_page():
    global date_entry  # Ensure the global scope of date_entry

    # Set up the calendar window
    calendar_page = tk.Toplevel()
    calendar_page.geometry('621x397')
    calendar_page.configure(background='#7FFFD4')
    calendar_page.title("Calendar Picker")

    # Create a Calendar widget
    global cal
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20)
    cal.place(x=180, y=110)
    
    # Bind the date selection event
    cal.bind("<<CalendarSelected>>", on_date_selected)

    # Create a text input box for manual date entry
    date_entry = tk.Entry(calendar_page)
    date_entry.place(x=180, y=350)
    
    # Create a button to validate and store the manually entered date
    validate_button = tk.Button(calendar_page, text="Submit Date", command=validate_and_store_date)
    validate_button.place(x=320, y=345)

    def Back_to_main_page_btnClickFunction():
        calendar_page.destroy()

    # Create labels
    tk.Label(calendar_page, text='Select a date or enter a date in YYYY-MM-DD format', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=28, y=36)
    tk.Label(calendar_page, text='Manual Date Entry:', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=26, y=325)
    tk.Button(calendar_page, text='Back to main page', bg='#B0E0E6', font=('arial', 9, 'normal'), command=Back_to_main_page_btnClickFunction).place(x=474, y=61)

def Services_page():
    def btnClickFunction():
        print('clicked')

    def Custom_btnClickFunction():
        print('clicked')

    def Business_Leisures_btnClickFunction():
        create_calendar_page()

    def Back_to_main_page_btnClickFunction():
        services_packages.destroy()

    # Set up the services window
    services_packages = tk.Toplevel()
    services_packages.geometry('596x442')
    services_packages.configure(background='#8B8378')
    services_packages.title('Services')

    # Create labels and buttons
    tk.Label(services_packages, text='Choose packages that you prefer from our extensive line of event and hire options', bg='#8B8378', font=('arial', 12, 'normal')).place(x=12, y=23)
    tk.Label(services_packages, text='split line', bg='#8B8378', font=('arial', 12, 'normal')).place(x=268, y=65)
    tk.Button(services_packages, text='Weddings', bg='#000000', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=45, y=301)
    tk.Button(services_packages, text='Customize', bg='#0000FF', font=('arial', 12, 'normal'), command=Custom_btnClickFunction).place(x=231, y=303)
    tk.Button(services_packages, text='Business Leisures', bg='#0000FF', font=('arial', 12, 'normal'), command=Business_Leisures_btnClickFunction).place(x=403, y=309)
    tk.Button(services_packages, text='Back to main page', bg='#B0E0E6', font=('arial', 9, 'normal'), command=Back_to_main_page_btnClickFunction).place(x=474, y=61)

def For_Hire_Page():
    def onebtnClickFunction():
        print('1')

    def twobtnClickFunction():
        print('2')

    def threebtnClickFunction():
        print('3')

    def fourbtnClickFunction():
        print('4')

    def Back_to_Main_btnClickFunction():
        for_hire.destroy()

    # Set up the for hire window
    for_hire = tk.Toplevel()
    for_hire.geometry('510x400')
    for_hire.configure(background='#FFEBCD')
    for_hire.title('For Hire')

    # Create labels and buttons
    tk.Button(for_hire, text='Button text!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=onebtnClickFunction).place(x=119, y=165)
    tk.Button(for_hire, text='Button text1!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=twobtnClickFunction).place(x=313, y=164)
    tk.Button(for_hire, text='Button text2!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=threebtnClickFunction).place(x=106, y=353)
    tk.Button(for_hire, text='Button text3!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=fourbtnClickFunction).place(x=314, y=351)
    tk.Button(for_hire, text='Back to main page', bg='#B0E0E6', font=('arial', 9, 'normal'), command=Back_to_Main_btnClickFunction).place(x=350, y=61)
    tk.Label(for_hire, text='Welcome to the extensive amount of people to hire', bg='#FFEBCD', font=('arial', 15, 'normal')).place(x=12, y=91)

def Locations_Page():
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

    def Back_to_main_page_btnClickFunction():
        locations.destroy()

    # Set up the locations window
    locations = tk.Toplevel()
    locations.geometry('691x405')
    locations.configure(background='#8B7D6B')
    locations.title('Locations')

    # Create labels and buttons
    tk.Label(locations, text='All the Locations Available', bg='#8B7D6B', font=('arial', 15, 'normal')).place(x=14, y=35)
    tk.Button(locations, text='Location 1', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_One_btnClickFunction).place(x=76, y=202)
    tk.Button(locations, text='Location 2', bg='#F5F5DC', font=('arial', 5, 'normal'), command=btnClickFunction).place(x=307, y=204)
    tk.Button(locations, text='Location 3', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_three_btnClickFunction).place(x=514, y=209)
    tk.Button(locations, text='Location 4', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Four_btnClickFunction).place(x=76, y=360)
    tk.Button(locations, text='Location 5', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Five_btnClickFunction).place(x=306, y=359)
    tk.Button(locations, text='Location 6', bg='#F5F5DC', font=('arial', 5, 'normal'), command=Location_Six_btnClickFunction).place(x=515, y=354)
    tk.Button(locations, text='Back to main page', bg='#B0E0E6', font=('arial', 9, 'normal'), command=Back_to_main_page_btnClickFunction).place(x=474, y=61)
    tk.Label(locations, text='Exquisite locations for our valued customers ', bg='#8B7D6B', font=('arial', 8, 'normal')).place(x=408, y=14)

def About_Us_btnClickFunction():
    global about_page

    about_page = tk.Toplevel()
    about_page.geometry('400x300')
    about_page.title('About Us')

    tk.Label(about_page, text='About Us', bg='#B0E0E6', font=('arial', 12, 'normal')).pack(pady=10)

    about_text = """
    Welcome to Xtrive Services!

    We are dedicated to providing top-notch services to our customers.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum finibus ex, at blandit dolor sodales a.
    """

    tk.Label(about_page, text=about_text, justify='left', wraplength=380, font=('arial', 10, 'normal')).pack(padx=20, pady=10)
    tk.Button(about_page, text='Close', bg='#F5f5dc', font=('arial', 12, 'normal'), command=about_page.destroy).pack(pady=10)

def Main_Page():
    # Main Page
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

    tk.Label(Main_page, text='Welcome To The Future Of Event Orginising', bg='#B0E0E6', font=('arial', 13, 'normal')).place(x=200, y=20)
    tk.Button(Main_page, text='About us', bg='#B0E0E6', font=('arial', 12, 'normal'), command=About_Us_btnClickFunction).place(x=400, y=200)
    tk.Button(Main_page, text='Services', bg='#B0E0E6', font=('arial', 12, 'normal'), command=Services_page).place(x=225, y=200)
    tk.Label(Main_page, text='Xtrive', bg='#B0E0E6', font=('arial', 50, 'normal')).place(x=25, y=60)
    tk.Button(Main_page, text='Locations', bg='#F5f5dc', font=('arial', 12, 'normal'), command=Locations_Page).place(x=361, y=7)
    tk.Button(Main_page, text='For hire', bg='#F5f5dc', font=('arial', 12, 'normal'), command=For_Hire_Page).place(x=100, y=7)
    tk.Label(Main_page, text='Information about our website', bg='#B0E0E6', font=('arial', 10, 'normal')).place(x=253, y=103)

def Login_page():
    # Example usage in main window
    Login_page = tk.Tk()
    Login_page.geometry('637x401')
    Login_page.configure(background='#F0F8FF')
    Login_page.title('Hello, I\'m the main window')

    # Buttons to open sign-up and sign-in windows
    tk.Button(Login_page, text='Sign Up', bg='#F5f5dc', font=('arial', 12, 'normal'), command=sign_up).place(x=250, y=200)
    # tk.Button(Login_page, text='Sign In', bg='#F5f5dc', font=('arial', 12, 'normal'), command=sign_in).place(x=250, y=235)
    tk.Button(Login_page, text='login', bg='#F5f5dc', font=('arial', 12, 'normal'), command=Main_Page).place(x=400, y=235)
    tk.Button(Login_page, text='login', bg='#F5f5dc', font=('arial', 12, 'normal'), command=Login_page).place(x=120, y=235)
    Login_page.mainloop()


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
login_button = tk.Button(login_page, text='Login', bg='#B0E0E6', font=('arial', 12, 'normal'), command=lambda: handle_login(username_entry, password_entry))
login_button.place(x=400, y=235)

tk.Button(login_page, text='Sign up', bg='#B0E0E6', font=('arial', 9, 'normal'), command=sign_up).place(x=400, y=61)

login_page.mainloop()

