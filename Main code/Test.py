import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import re

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
    # Check if the input matches the MM/DD/YY format
    if re.match(r"\d{2}/\d{2}/\d{2}", user_input):
        try:
            entered_date = datetime.strptime(user_input, '%m/%d/%y').date()
            if entered_date in selected_dates:
                messagebox.showerror("Date Already Chosen", "Date chosen already, please select another booking.")
            else:
                store_date(entered_date.strftime('%Y-%m-%d'))
                cal.calevent_create(entered_date, "Chosen", 'booked')
                date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YY.")
    else:
        messagebox.showerror("Invalid Date Format", "Please enter the date in the format MM/DD/YY.")

def create_calendar_page():
    global date_entry
    global cal

    def on_date_selected(event):
        selected_date_str = cal.get_date()
        try:
            selected_date = datetime.strptime(selected_date_str, '%m/%d/%y').date()
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
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20)
    cal.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
    cal.bind("<<CalendarSelected>>", on_date_selected)

    # Create a text input box for manual date entry
    date_entry = tk.Entry(calendar_page)
    date_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

    # Create a button to validate and store the manually entered date
    validate_button = tk.Button(calendar_page, text="Submit Date", command=validate_and_store_date)
    validate_button.grid(row=1, column=2, padx=10, pady=10)

    # Create labels
    tk.Label(calendar_page, text='Select a date or enter a date in MM/DD/YY format', bg='#7FFFD4', font=('arial', 12, 'normal')).grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

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

# Assuming there is a main Tkinter window setup
root = tk.Tk()
root.title("Main Page")
root.geometry('300x200')

# Button to open the calendar page
open_calendar_btn = tk.Button(root, text="Open Calendar", command=create_calendar_page)
open_calendar_btn.pack(pady=20)

root.mainloop()
