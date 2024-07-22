import tkinter as tk
from tkinter import ttk

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Main Tkinter window
root = tk.Tk()
root.title("Xtrive Services")
root.geometry("600x400")

# Create a container to hold all frames
container = ttk.Frame(root)
container.pack(fill=tk.BOTH, expand=True)

# Define custom styles
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' theme for simplicity

# Define frames with custom colors
main_frame = ttk.Frame(container, style='Beige.TFrame')
about_frame = ttk.Frame(container, style='White.TFrame')
services_frame = ttk.Frame(container, style='White.TFrame')
hire_frame = ttk.Frame(container, style='White.TFrame')
locations_frame = ttk.Frame(container, style='White.TFrame')

# Pack all frames into the container
main_frame.pack(fill=tk.BOTH, expand=True)
about_frame.pack(fill=tk.BOTH, expand=True)
services_frame.pack(fill=tk.BOTH, expand=True)
hire_frame.pack(fill=tk.BOTH, expand=True)
locations_frame.pack(fill=tk.BOTH, expand=True)

# Content for each frame
content = {
    "main": ("Welcome to Xtrive Services", "Here you can find information about our offerings."),
    "about": ("About Us", "We are dedicated to providing high-quality services."),
    "services": ("Our Services", "We offer a variety of services to meet your needs."),
    "hire": ("For Hire", "Join our team of dedicated professionals."),
    "locations": ("Our Locations", "Find us in various locations.")
}

# Create content labels in each frame
for key, (title, text) in content.items():
    label_title = ttk.Label(eval(f"{key}_frame"), text=title, font=('Helvetica', 16, 'bold'), background='white')
    label_title.pack(pady=10)

    label_content = ttk.Label(eval(f"{key}_frame"), text=text, wraplength=500, background='white')
    label_content.pack(padx=20, pady=10)

# Navigation buttons
button_frame = ttk.Frame(main_frame, style='White.TFrame')
button_frame.pack(side=tk.TOP, fill=tk.X)

btn_about = ttk.Button(button_frame, text="About Us", command=lambda: show_frame(about_frame))
btn_about.pack(side=tk.LEFT, padx=10, pady=5)

btn_services = ttk.Button(button_frame, text="Services", command=lambda: show_frame(services_frame))
btn_services.pack(side=tk.LEFT, padx=10, pady=5)

btn_hire = ttk.Button(button_frame, text="For Hire", command=lambda: show_frame(hire_frame))
btn_hire.pack(side=tk.LEFT, padx=10, pady=5)

btn_locations = ttk.Button(button_frame, text="Locations", command=lambda: show_frame(locations_frame))
btn_locations.pack(side=tk.LEFT, padx=10, pady=5)

# Title in the middle of the main page
label_title_main = ttk.Label(main_frame, text="Xtrive", font=('Helvetica', 24, 'bold'), foreground='black', background='White')
label_title_main.pack(pady=20)

# Show the main frame initially
show_frame(main_frame)

# Start the main loop
root.mainloop()
