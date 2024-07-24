import tkinter as tk

            # Main Page
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