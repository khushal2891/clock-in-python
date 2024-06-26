from tkinter import *
import time

def update_time():
    current_time = time.strftime('%H:%M:%S %p') # Get the current time
    label.config(text=current_time) # Update the label text with the current time
    label.after(1000, update_time) # Call update_time function again after 1000ms (1 second)

# Create the Tkinter window
root = Tk()
root.title("Tkinter Clock")

# Create a label to display the time
label = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call update_time function to update time initially and then recursively update it
update_time()

# Start the main event loop
root.mainloop()