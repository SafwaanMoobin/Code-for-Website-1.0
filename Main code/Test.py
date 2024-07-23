import tkinter as tk
from tkcalendar import Calendar
import re
import tkinter.messagebox as messagebox

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
    if re.match(r"\d{4}-\d{2}-\d{2}", user_input):
        try:
            year, month, day = map(int, user_input.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                store_date(user_input)
            else:
                print("Invalid date")
        except ValueError:
            print("Invalid date")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")

users = {}

def sign_up():
    global users

    def validate_username(username):
        return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

    def validate_email(email):
        return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

    def sign_up_button_click():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        if not validate_username(username):
            messagebox.showerror("Error", "Username must be 3-10 characters long and contain only letters and numbers.")
            return

        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format. Please enter in the format 'EmailExample@Organisation.com'.")
            return

        users[username] = {
            'password': password,
            'email': email
        }

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "User successfully registered!")

    sign_up_window = tk.Toplevel()
    sign_up_window.geometry('400x300')
    sign_up_window.title('Sign Up')

    tk.Label(sign_up_window, text='Username:').pack()
    username_entry = tk.Entry(sign_up_window, width=30)
    username_entry.pack()

    tk.Label(sign_up_window, text='Password:').pack()
    password_entry = tk.Entry(sign_up_window, show='*', width=30)
    password_entry.pack()

    tk.Label(sign_up_window, text='Email:').pack()
    email_entry = tk.Entry(sign_up_window, width=30)
    email_entry.pack()

    tk.Button(sign_up_window, text='Sign Up', command=sign_up_button_click).pack()

    sign_up_window.mainloop()

def sign_in(): 
    global users

    def validate_username(username):
        return re.match(r'^[a-zA-Z0-9]{3,10}$', username)

    def sign_in_button_click():
        username = username_entry.get()
        password = password_entry.get()

        if not validate_username(username):
            messagebox.showerror("Error", "Username must be 3-10 characters long and contain only letters and numbers.")
            return

        if username in users and users[username]['password'] == password:
            messagebox.showinfo("Success", "User successfully signed in!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    sign_in_window = tk.Toplevel()
    sign_in_window.geometry('400x200')
    sign_in_window.title('Sign In')

    tk.Label(sign_in_window, text='Username:').pack()
    username_entry = tk.Entry(sign_in_window, width=30)
    username_entry.pack()

    tk.Label(sign_in_window, text='Password:').pack()
    password_entry = tk.Entry(sign_in_window, show='*', width=30)
    password_entry.pack()

    tk.Button(sign_in_window, text='Sign In', command=sign_in_button_click).pack()

    sign_in_window.mainloop()

def create_calendar_page():
    global date_entry

    calendar_page = tk.Toplevel()
    calendar_page.geometry('621x397')
    calendar_page.configure(background='#7FFFD4')
    calendar_page.title("Calendar Picker")

    global cal
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20)
    cal.place(x=180, y=110)
    
    cal.bind("<<CalendarSelected>>", on_date_selected)

    date_entry = tk.Entry(calendar_page)
    date_entry.place(x=180, y=350)
    
    validate_button = tk.Button(calendar_page, text="Submit Date", command=validate_and_store_date)
    validate_button.place(x=320, y=345)

    def Back_to_main_page_btnClickFunction():
        calendar_page.destroy()

    tk.Label(calendar_page, text='Select a date or enter a date in YYYY-MM-DD format', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=28, y=36)
    tk.Label(calendar_page, text='Manual Date Entry:', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=26, y=325)
    tk.Button(calendar_page, text='Back to main page', bg='#FFD39B', font=('arial', 9, 'normal'), command=Back_to_main_page_btnClickFunction).place(x=474, y=61)

def Services_page():
    def btnClickFunction():
        print('clicked')

    def Custom_btnClickFunction():
        print('clicked')

    def Business_Leisures_btnClickFunction():
        create_calendar_page()

    def Back_to_main_page_btnClickFunction():
        services_packages.destroy()

    services_packages = tk.Toplevel()
    services_packages.geometry('596x442')
    services_packages.configure(background='#8B8378')
    services_packages.title('Services')

    tk.Label(services_packages, text='Choose packages that you prefer from our extensive line of event and hire options', bg='#8B8378', font=('arial', 12, 'normal')).place(x=12, y=23)
    tk.Label(services_packages, text='split line', bg='#8B8378', font=('arial', 12, 'normal')).place(x=268, y=65)
    tk.Button(services_packages, text='Weddings', bg='#000000', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=45, y=301)
    tk.Button(services_packages, text='Customize', bg='#0000FF', font=('arial', 12, 'normal'), command=Custom_btnClickFunction).place(x=231, y=303)
    tk.Button(services_packages, text='Business Leisures', bg='#0000FF', font=('arial', 12, 'normal'), command=Business_Leisures_btnClickFunction).place(x=403, y=309)
    tk.Button(services_packages, text='Back to main page', bg='#FFD39B', font=('arial', 9, 'normal'), command=Back_to_main_page_btnClickFunction).place(x=474, y=61)

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

    for_hire = tk.Toplevel()
    for_hire.geometry('510x400')
    for_hire.configure(background='#FFEBCD')
    for_hire.title('For Hire')

    tk.Button(for_hire, text='Button text!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=onebtnClickFunction).place(x=119, y=165)
    tk.Button(for_hire, text='Button text1!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=twobtnClickFunction).place(x=313, y=164)
    tk.Button(for_hire, text='Button text2!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=threebtnClickFunction).place(x=127, y=236)
    tk.Button(for_hire, text='Button text3!', bg='#FFEBCD', font=('arial', 15, 'normal'), command=fourbtnClickFunction).place(x=307, y=240)
    tk.Button(for_hire, text='Back to main page', bg='#FFD39B', font=('arial', 9, 'normal'), command=Back_to_Main_btnClickFunction).place(x=447, y=66)

def Locations_Page():
    def BtnClickFunction():
        print('clicked')

    def Main_Page():
        locations_page.destroy()

    locations_page = tk.Toplevel()
    locations_page.geometry('600x300')
    locations_page.configure(background='#BDB76B')
    locations_page.title('Locations')

    tk.Label(locations_page, text='Lorem ipsum', bg='#BDB76B', font=('arial', 12, 'normal')).place(x=22, y=53)
    tk.Button(locations_page, text='Click!', bg='#D3D3D3', font=('arial', 12, 'normal'), command=BtnClickFunction).place(x=232, y=99)
    tk.Label(locations_page, text='Lorem ipsum', bg='#BDB76B', font=('arial', 12, 'normal')).place(x=22, y=129)
    tk.Button(locations_page, text='Back to main page', bg='#FFD39B', font=('arial', 9, 'normal'), command=Main_Page).place(x=466, y=57)

def About_Us_btnClickFunction():
    about_us = tk.Toplevel()
    about_us.geometry('600x450')
    about_us.configure(background='#FFE4B5')
    about_us.title('About us')

    tk.Label(about_us, text='Who we are', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=26, y=37)
    tk.Label(about_us, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=12, y=67)
    tk.Label(about_us, text='Company values', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=25, y=144)
    tk.Label(about_us, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=21, y=177)
    tk.Label(about_us, text='Contact Information', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=21, y=273)
    tk.Label(about_us, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', bg='#FFE4B5', font=('arial', 12, 'normal')).place(x=21, y=304)
    tk.Button(about_us, text='Back to main page', bg='#FFD39B', font=('arial', 9, 'normal'), command=about_us.destroy).place(x=474, y=61)

def main():
    main_page = tk.Tk()
    main_page.geometry('722x497')
    main_page.configure(background='#F5DEB3')
    main_page.title('Main Page')

    tk.Label(main_page, text='Welcome to Events Management System', bg='#F5DEB3', font=('arial', 12, 'normal')).place(x=170, y=55)
    tk.Button(main_page, text='About us', bg='#FFE4B5', font=('arial', 12, 'normal'), command=About_Us_btnClickFunction).place(x=32, y=145)
    tk.Button(main_page, text='Services', bg='#FFE4B5', font=('arial', 12, 'normal'), command=Services_page).place(x=31, y=215)
    tk.Button(main_page, text='Locations', bg='#FFE4B5', font=('arial', 12, 'normal'), command=Locations_Page).place(x=31, y=275)
    tk.Button(main_page, text='For hire', bg='#FFE4B5', font=('arial', 12, 'normal'), command=For_Hire_Page).place(x=31, y=332)
    tk.Button(main_page, text='Sign Up', bg='#FFE4B5', font=('arial', 12, 'normal'), command=sign_up).place(x=31, y=390)

    main_page.mainloop()

main()
