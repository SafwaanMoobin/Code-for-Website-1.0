import tkinter as tk
from tkcalendar import Calendar
import re
import tkinter.messagebox as messagebox
from tkinter import * 
import csv
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import os



# Initialize empty users dictionary
users = {}
current_user = None

# Function to validate username format
def validate_username(username):
    return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

# Function to validate email format
def validate_email(email):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

# Function to load users from CSV file
def load_users():
    if os.path.exists('users.csv'):
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 7:  # Expecting username, password, email, selected_package, selected_dates, selected_combo_item, selected_locations
                    username = row[0]
                    password = row[1]
                    email = row[2]
                    selected_package = row[3]
                    selected_dates = row[4:-2]  # Extract dates before combo item and locations
                    selected_combo_item = row[-2]
                    selected_locations = row[-1:]
                    
                    users[username] = {
                        'password': password,
                        'email': email,
                        'selected_package': selected_package,
                        'selected_dates': selected_dates,
                        'selected_combo_item': selected_combo_item,
                        'selected_locations': selected_locations
                    }
    else:
        print("users.csv file not found.")

def save_users():
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, user_data in users.items():
            row = [
                username,
                user_data['password'],
                user_data['email'],
                user_data['selected_package']
            ] + user_data['selected_dates'] + [
                user_data['selected_combo_item']
            ] + user_data['selected_locations']
            writer.writerow(row)

def sign_up_button_click(username_entry, password_entry, email_entry):
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    # Validate username and email
    if not validate_username(username):
        messagebox.showerror("Error", "Username must be 3-10 characters long and contain only letters and numbers.")
        return
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format.")
        return

    # Check if username already exists
    if username in users:
        messagebox.showerror("Error", "Username already exists.")
        return

    # Store new user information
    users[username] = {
        'password': password,
        'email': email,
        'selected_package': '',
        'selected_dates': [],  # Initialize an empty list for selected dates
        'selected_combo_item': '',  # Default empty combo item
        'selected_locations': []  # Initialize an empty list for selected locations
    }

    # Save users to CSV file
    save_users()

    # Clear the entry fields after successful sign-up
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "User successfully registered!")

def sign_up():
    sign_up_window = tk.Toplevel()
    sign_up_window.title("Sign Up")

    # Create labels and entry fields for username, password, and email
    tk.Label(sign_up_window, text="Username:").pack()
    username_entry = tk.Entry(sign_up_window)
    username_entry.pack()

    tk.Label(sign_up_window, text="Password:").pack()
    password_entry = tk.Entry(sign_up_window, show="*")
    password_entry.pack()

    tk.Label(sign_up_window, text="Email:").pack()
    email_entry = tk.Entry(sign_up_window)
    email_entry.pack()

    # Create the sign-up button and bind it to the sign_up_button_click function
    tk.Button(sign_up_window, text="Sign Up", command=lambda: sign_up_button_click(username_entry, password_entry, email_entry)).pack()

    sign_up_window.mainloop()

# Function to handle login button click
def handle_login(username_entry, password_entry):
    global current_user

    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]['password'] == password:
        current_user = username
        load_user_calendar()
        Main_Page()  # Assuming Main_Page is defined elsewhere in your code
    else:
        messagebox.showerror("Error", "Invalid username or password.")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Load existing users
load_users()

# Function to store selected date
def store_date(date, remove=False):
    if current_user:
        if remove:
            if date in users[current_user]['selected_dates']:
                users[current_user]['selected_dates'].remove(date)
        else:
            if date not in users[current_user]['selected_dates']:
                users[current_user]['selected_dates'].append(date)
        save_users()

def store_combo_item(selected_item):
    if current_user:
        users[current_user]['selected_combo_item'] = selected_item
        save_users()

def load_user_calendar():
    global selected_dates
    selected_dates = set(users.get(current_user, {}).get('selected_dates', []))

# Function to validate and store date from entry
def validate_and_store_date():
    user_input = date_entry.get()
    if re.match(r"\d{2}/\d{2}/\d{4}", user_input):
        try:
            entered_date = datetime.strptime(user_input, '%m/%d/%Y').date().strftime('%Y-%m-%d')
            if entered_date in selected_dates:
                messagebox.showerror("Date Already Chosen", "Date chosen already, please select another booking.")
            else:
                store_date(entered_date)
                cal.calevent_create(datetime.strptime(entered_date, '%Y-%m-%d'), "Chosen", 'booked')
                date_entry.delete(0, tk.END)
                save_users()  # Save users after storing the date
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YYYY.")
    else:
        messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YYYY.")

# Function to handle date selection
def on_date_selected(event):
    selected_date = cal.selection_get().strftime('%Y-%m-%d')
    if selected_date in selected_dates:
        messagebox.showerror("Date Already Chosen", "Date chosen already, please select another booking.")
    else:
        store_date(selected_date)
        cal.calevent_create(datetime.strptime(selected_date, '%Y-%m-%d'), "Chosen", 'booked')

# Function to handle right-click to remove or add date
def on_date_right_click(event):
    selected_date_str = cal.get_date()
    try:
        selected_date = datetime.strptime(selected_date_str, '%m/%d/%Y').date().strftime('%Y-%m-%d')
        if selected_date in selected_dates:
            cal.calevent_remove('booked')
            store_date(selected_date, remove=True)
        else:
            messagebox.showerror("Date Not Selected", "Date not selected for booking.")
    except ValueError:
        messagebox.showerror("Date Format Error", "Error parsing selected date.")

# Function to create calendar page
def create_calendar_page():
    global date_entry
    global cal

    def submit_and_close():
        save_users()  # Save users before closing the page
        calendar_page.destroy()  # Close the calendar page

    # Set up the calendar window
    calendar_page = tk.Toplevel()
    calendar_page.geometry('620x400')
    calendar_page.configure(background='#7FFFD4')
    calendar_page.title("Calendar Picker")

    # Create a Calendar widget
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20, date_pattern='mm/dd/yyyy')
    cal.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    cal.bind("<<CalendarSelected>>", on_date_selected)
    cal.bind("<Button-3>", on_date_right_click)  # Right-click to remove or add date

    # Create a text input box for manual date entry
    date_entry = tk.Entry(calendar_page)
    date_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

    # Create a button to validate and store the manually entered date
    validate_button = tk.Button(calendar_page, text="Submit Date", command=validate_and_store_date)
    validate_button.grid(row=1, column=2, padx=10, pady=10)

    # Create a button to submit the selected dates and close the page
    submit_button = tk.Button(calendar_page, text="Submit and Close", command=submit_and_close)
    submit_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Create labels
    tk.Label(calendar_page, text='Select a date or enter a date in MM/DD/YYYY format', bg='#7FFFD4', font=('arial', 12, 'normal')).grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    tk.Label(calendar_page, text='Manual Date Entry:', bg='#7FFFD4', font=('arial', 12, 'normal')).grid(row=4, column=0, padx=10, pady=10, sticky='w')

    # Highlight previously selected dates
    for date in selected_dates:
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            cal.calevent_create(date_obj, "Chosen", 'booked')
        except ValueError:
            continue

    calendar_page.mainloop()

def Services_page():
    # Function to handle package selection
    def btnClickFunction():
        if current_user:
            selected_package = COmbo.get()
            users[current_user]['selected_package'] = selected_package
            save_users()
            print('Selected package saved:', selected_package)
        else:
            print('No user logged in.')

    # Initialize the main window
    Pacakges = tk.Tk()
    Pacakges.geometry('596x451')
    Pacakges.configure(background='#F0F8FF')
    Pacakges.title('Hello, I\'m the main window')

    # Create labels
    tk.Label(Pacakges, text='Packages', bg='#F0F8FF', font=('arial', 17, 'normal')).place(x=28, y=41)
    tk.Label(Pacakges, text='Art/Auction', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=95, y=126)
    tk.Label(Pacakges, text='Business', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=264, y=304)
    tk.Label(Pacakges, text='Ceremony/Wedding', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=395, y=121)
    tk.Label(Pacakges, text='Custom', bg='#F0F8FF', font=('arial', 13, 'normal')).place(x=51, y=382)

    # Create buttons
    tk.Button(Pacakges, text='For Hire', bg='#F0F8FF', font=('arial', 13, 'normal'), command=btnClickFunction).place(x=162, y=372)
    tk.Button(Pacakges, text='Submit', bg='#F0F8FF', font=('arial', 8, 'normal'), command=btnClickFunction).place(x=425, y=414)
    tk.Button(Pacakges, text='Back to main menu', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=436, y=34)

    # Create Combobox
    COmbo = ttk.Combobox(Pacakges, values=['Art/Auction', 'Business', 'Ceremony/Wedding', 'Custom'], font=('arial', 12, 'normal'), width=15)
    COmbo.place(x=360, y=377)
    COmbo.current(0)  # Set default value

    Pacakges.mainloop()


def For_Hire_Page():
    def btnClickFunction():
        # Store the selected combo item
        selected_item = comboOneTwoPunch.get()
        store_combo_item(selected_item)
        messagebox.showinfo("Info", f"Selected item '{selected_item}' has been saved.")
    
    For_hire = tk.Tk()

    # This is the section of code which creates the main window
    For_hire.geometry('585x452')
    For_hire.configure(background='#F0F8FF')
    For_hire.title('For Hire Page')

    # This is the section of code which creates a label
    tk.Label(For_hire, text='For Hire', bg='#F0F8FF', font=('arial', 17, 'normal')).place(x=31, y=37)

    # This is the section of code which creates a button
    tk.Button(For_hire, text='Back to menu', bg='#F0F8FF', font=('arial', 10, 'normal'), command=For_hire.destroy).place(x=347, y=14)

    # This is the section of code which creates the a label
    tk.Label(For_hire, text='Team 1', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=55, y=239)

    # This is the section of code which creates the a label
    tk.Label(For_hire, text='Text ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=228, y=154)
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
    tk.Label(For_hire, text='Team 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=335, y=239)

    # This is the section of code which creates the a label
    tk.Label(For_hire, text='Text 2', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=500, y=132)

    # This is the section of code which creates a combo box
    comboOneTwoPunch = ttk.Combobox(For_hire, values=['Thing 1', 'Thing 2'], font=('arial', 12, 'normal'), width=10)
    comboOneTwoPunch.place(x=124, y=377)
    comboOneTwoPunch.current(1)

    # This is the section of code which creates a button
    tk.Button(For_hire, text='Submit', bg='#F0F8FF', font=('arial', 10, 'normal'), command=btnClickFunction).place(x=293, y=402)

    # This is the section of code which creates the a label
    tk.Label(For_hire, text='Help', bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=75, y=381)

    For_hire.mainloop()

# Example function to simulate user login and page access

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
