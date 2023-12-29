import tkinter as tk
from database import database

def change_options():
    # Clear existing options
    option_menu['menu'].delete(0, 'end')

    # Get the selected category
    selected_category = category_var.get()

    option_var.set('')
    # Add new options based on the selected category
    for x in database:
            if x.subjectName == selected_category:
                subject_selected = x

    for x in subject_selected.dates_cols:
        option_menu['menu'].add_command(label=x, command=tk._setit(option_var, x))
    
# Create the main window
root = tk.Tk()
root.title("Change OptionMenu Example")

# Define options
categories = [x.subjectName for x in database]


# Create a Label and an OptionMenu
category_label = tk.Label(root, text="Select a SUBJECT:")
category_label.pack(pady=10)

category_var = tk.StringVar(root)
category_menu = tk.OptionMenu(root, category_var, *categories, command=lambda event=None: change_options())
category_menu.pack()

# Create another Label and an OptionMenu for the specific options
option_label = tk.Label(root, text="Select an option:")
option_label.pack(pady=10)

option_var = tk.StringVar(root)
option_menu = tk.OptionMenu(root, option_var, '')
option_menu.pack()

# Start the main event loop
root.mainloop()