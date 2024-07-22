import tkinter as tk
from tkcalendar import Calendar

def on_date_selected(event):
    selected_date = cal.selection_get()
    print("Selected date:", selected_date)

def create_calendar_page():
    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = selector.get()
        print("User input:", userInput)

    # Set up the main application window
    calendar_page = tk.Tk()
    calendar_page.geometry('621x397')
    calendar_page.configure(background='#7FFFD4')
    calendar_page.title("Calendar Picker")

    # Create a Calendar widget
    global cal
    cal = Calendar(calendar_page, selectmode='day', year=2024, month=7, day=20)
    cal.place(x=180, y=110)
    
    # Bind the date selection event
    cal.bind("<<CalendarSelected>>", on_date_selected)

    # Create a text input box
    selector = tk.Entry(calendar_page)
    selector.place(x=240, y=325)

    # Create labels
    tk.Label(calendar_page, text='Select a date that best suits your needs', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=28, y=36)
    tk.Label(calendar_page, text='Selector for packages unite', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=26, y=75)

    # Run the application
    calendar_page.mainloop()

# Call the function to create the calendar page
create_calendar_page()
