import tkinter as tk
from tkcalendar import Calendar
import re
import tkinter.messagebox as messagebox
from tkinter import * 
import csv
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox



selected_dates = []
# Initialize empty users dictionary
users = {}

# Function to validate username format
def validate_username(username):
    return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

# Function to validate email format
def validate_email(email):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

# # Function to read existing users from users.csv
# def load_users():
#     try:
#         with open('users.csv', mode='r') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip header row
#             for row in reader:
#                 username, password, email = row
#                 users[username] = {'password': password, 'email': email}
#     except FileNotFoundError:
#         # Handle the case where users.csv doesn't exist yet
#         pass

# # Load existing users when the program starts
# load_users()

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


users = {}  # Initialize an empty dictionary to store user data

def load_users():
    try:
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    if len(row) >= 3:
                        username, password, email = row[:3]  # Take only the first three elements
                        users[username] = {'password': password, 'email': email, 'bookings': {}}
                        # You can process additional fields here if needed
                    else:
                        print(f"Ignoring invalid data row: {row}")
                except ValueError as e:
                    print(f"Error processing row: {row}. Error: {e}")
    except FileNotFoundError:
        print("users.csv file not found.")

# Example usage:
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


#This code snippet manages the selection and storage of dates in a list 
# called selected_dates. It includes functions for storing a date, handling a date selection event, and validating and storing a user-input dateimport re
selected_dates = set()

def store_date(date):
    selected_dates.add(date)
    print("Stored dates:", selected_dates)

def on_date_selected(event):
    selected_date = cal.selection_get()
    print("Selected date:", selected_date)
    store_date(selected_date.strftime('%Y-%m-%d'))

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_and_store_date():
    user_input = date_entry.get()
    # Check if the input matches the MM/DD/YYYY format
    if re.match(r"\d{2}/\d{2}/\d{4}", user_input):
        try:
            entered_date = datetime.strptime(user_input, '%m/%d/%Y').date()
            if entered_date in selected_dates:
                messagebox.showerror("Date Already Chosen", "Date chosen already, please select another booking.")
            else:
                store_date(entered_date.strftime('%Y-%m-%d'))
                cal.calevent_create(entered_date, "Chosen", 'booked')
                date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YYYY.")
    else:
        messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YYYY.")

def create_calendar_page():
    global date_entry
    global cal

    def on_date_selected(event):
        selected_date_str = cal.get_date()
        try:
            selected_date = datetime.strptime(selected_date_str, '%m/%d/%Y').date()
            if selected_date in selected_dates:
                messagebox.showerror("Date Already Chosen", "Date chosen already, please select another booking.")
            else:
                store_date(selected_date.strftime('%Y-%m-%d'))
                cal.calevent_create(selected_date, "Chosen", 'booked')
                date_entry.delete(0, tk.END)
                date_entry.insert(0, selected_date_str)
        except ValueError:
            messagebox.showerror("Date Format Error", "Error parsing selected date.")

    def back_to_main_page_btn_click_function():
        calendar_page.destroy()

    # Set up the calendar window
    calendar_page = tk.Toplevel()
    calendar_page.geometry('620x400')
    calendar_page.configure(background='#7FFFD4')
    calendar_page.title("Calendar Picker")

    # Create a Calendar widget
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20, date_pattern='mm/dd/yyyy')
    cal.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    cal.bind("<<CalendarSelected>>", on_date_selected)

    # Create a text input box for manual date entry
    date_entry = tk.Entry(calendar_page)
    date_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

    # Create a button to validate and store the manually entered date
    validate_button = tk.Button(calendar_page, text="Submit Date", command=validate_and_store_date)
    validate_button.grid(row=1, column=2, padx=10, pady=10)

    # Create labels
    tk.Label(calendar_page, text='Select a date or enter a date in MM/DD/YYYY format', bg='#7FFFD4', font=('arial', 12, 'normal')).grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    tk.Label(calendar_page, text='Manual Date Entry:', bg='#7FFFD4', font=('arial', 12, 'normal')).grid(row=3, column=0, padx=10, pady=10, sticky='w')

    # Create a button to go back to the main page
    back_button = tk.Button(calendar_page, text='Back to main page', bg='#B0E0E6', font=('arial', 9, 'normal'), command=back_to_main_page_btn_click_function)
    back_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='e')

    # Adjust column and row weights for better resizing behavior
    calendar_page.grid_columnconfigure(0, weight=1)
    calendar_page.grid_columnconfigure(1, weight=1)
    calendar_page.grid_columnconfigure(2, weight=1)
    calendar_page.grid_rowconfigure(0, weight=1)
    calendar_page.grid_rowconfigure(1, weight=1)
    calendar_page.grid_rowconfigure(2, weight=1)
    calendar_page.grid_rowconfigure(3, weight=1)
    calendar_page.grid_rowconfigure(4, weight=1)

    calendar_page.mainloop()


def Services_page():
    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')


    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')


    # this is a function which returns the selected combo box item
    def getSelectedComboItem():
        return COmbo.get()


    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')



    Pacakges = Tk()
    # Pacakges = ttk()


    # This is the section of code which creates the main window
    Pacakges.geometry('596x451')
    Pacakges.configure(background='#F0F8FF')
    Pacakges.title('Hello, I\'m the main window')


    # This is the section of code which creates a button
    Button(Pacakges, text='Back to main menu', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=436, y=34)


    # This is the section of code which creates the a label
    Label(Pacakges, text='Packages', bg='#F0F8FF', font=('arial', 17, 'normal')).place(x=28, y=41)


    # This is the section of code which creates the a label
    Label(Pacakges, text='Art/Auction', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=95, y=126)


    # This is the section of code which creates the a label
    Label(Pacakges, text='Business ', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=264, y=304)


    # This is the section of code which creates the a label
    Label(Pacakges, text='Ceromony/wedding', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=395, y=121)


    # This is the section of code which creates the a label
    Label(Pacakges, text='Custom', bg='#F0F8FF', font=('arial', 13, 'normal')).place(x=51, y=382)


    # This is the section of code which creates a button
    Button(Pacakges, text='For Hire', bg='#F0F8FF', font=('arial', 13, 'normal'), command=btnClickFunction).place(x=162, y=372)

    # This is the section of code which creates a button
    Button(Pacakges, text='Submit', bg='#F0F8FF', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=425, y=414)


    # This is the section of code which creates a combo box
    COmbo= ttk.Combobox(Pacakges, values=['Art/Auction', 'Buisness', 'Ceromony/Wedding'], font=('arial', 12, 'normal'), width=10)
    COmbo.place(x=360, y=377)
    COmbo.current(3)


        

def For_Hire_Page():

    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')


    # this is a function which returns the selected combo box item
    def getSelectedComboItem():
        return comboOneTwoPunch.get()


    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')



    For_hire = Tk()

    # This is the section of code which creates the main window
    For_hire.geometry('585x452')
    For_hire.configure(background='#F0F8FF')
    For_hire.title('Hello, I\'m the main window')


    # This is the section of code which creates the a label
    Label(For_hire, text='For Hire', bg='#F0F8FF', font=('arial', 17, 'normal')).place(x=31, y=37)


    # This is the section of code which creates a button
    Button(For_hire, text='Back to menu', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=347, y=14)


    # This is the section of code which creates the a label
    Label(For_hire, text='Team 1', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=55, y=239)


    # This is the section of code which creates the a label
    Label(For_hire, text='Text ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=228, y=154)
    Team_1_text = """
    Welcome to Xtrive Services!

    We are dedicated to providing top-notch services to our customers.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum finibus ex, at blandit dolor sodales a.
    """
    tk.Label(For_hire, text=Team_1_text, justify='left', wraplength=380, font=('arial', 10, 'normal')).pack(padx=20, pady=10)

    Team_2_text = """
    Welcome to Xtrive Services!

    We are dedicated to providing top-notch services to our customers.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum finibus ex, at blandit dolor sodales a.
    """
    tk.Label(For_hire, text=Team_2_text, justify='left', wraplength=380, font=('arial', 10, 'normal')).pack(padx=20, pady=10)



    # This is the section of code which creates the a label
    Label(For_hire, text='Team 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=335, y=239)


    # This is the section of code which creates the a label
    Label(For_hire, text='Text 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=500, y=132)


    # This is the section of code which creates a combo box
    comboOneTwoPunch= ttk.Combobox(For_hire, values=['Thing 1', 'Thing 2'], font=('arial', 12, 'normal'), width=10)
    comboOneTwoPunch.place(x=124, y=377)
    comboOneTwoPunch.current(1)


    # This is the section of code which creates a button
    Button(For_hire, text='Submit', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=293, y=402)


    # This is the section of code which creates the a label
    Label(For_hire, text='Help', bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=75, y=381)


    For_hire.mainloop()



def Locations_Page():
    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')


    # this is a function which returns the selected combo box item
    def getSelectedComboItem():
        return comboOneTwoPunch.get()


   
    Locations = Tk()

    # This is the section of code which creates the main window
    Locations.geometry('612x373')
    Locations.configure(background='#F0F8FF')
    Locations.title('Hello, I\'m the main window')


    # This is the section of code which creates the a label
    Label(Locations, text='Location', bg='#F0F8FF', font=('arial', 17, 'normal')).place(x=19, y=25)


    # This is the section of code which creates the a label
    Label(Locations, text='Location 1', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=80, y=182)


    # This is the section of code which creates the a label
    Label(Locations, text='Location 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=255, y=178)


    # This is the section of code which creates the a label
    Label(Locations, text='Location 3', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=79, y=341)


    # This is the section of code which creates the a label
    Label(Locations, text='Location 4', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=256, y=340)


    # This is the section of code which creates a button
    Button(Locations, text='Back to menu', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=279, y=21)

    # This is the section of code which creates a button
    Button(Locations, text='Submit', bg='#F0F8FF', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=505, y=250)


    # This is the section of code which creates a combo box
    comboOneTwoPunch= ttk.Combobox(Locations, values=['Location 1', 'Location 2', 'Location 3', 'Location 4'], font=('arial', 10, 'normal'), width=10)
    comboOneTwoPunch.place(x=452, y=122)
    comboOneTwoPunch.current(1)

    # This is the section of code which creates a combo box
    comboOneTwoPunch= ttk.Combobox(Locations, values=['Location 1', 'Location 2', 'Location 3', 'Location 4'], font=('arial', 10, 'normal'), width=10)
    comboOneTwoPunch.place(x=452, y=200)
    comboOneTwoPunch.current(1)





    # This is the section of code which creates the a label
    Label(Locations, text='Manual choice', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=439, y=58)

    #  # this is a function which returns the selected combo box item
    # def getSelectedComboItem():
    #     return Lcaotion.get()


    # # this is a function which returns the selected combo box item
    # def getSelectedComboItem():
    #     return Lcaotiass.get()

    Locations.mainloop()

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
    tk.Button(Main_page, text='calendar', bg='#B0E0E6', font=('arial', 9, 'normal'), command=create_calendar_page).place(x=253, y=61)


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