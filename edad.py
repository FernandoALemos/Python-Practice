from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.geometry("550x300")


def age():
	if my_entry.get():
		# Get the current year
		current_year = datetime.now().year
		# Calculate The Age
		your_age = current_year - int(my_entry.get())
		# Show age in message box
		messagebox.showinfo("Your Age", f"Your Age Is: {your_age}")

	else:
		# Show Error Message
		messagebox.showerror("Error", "You forgot to enter your age!")

my_label = Label(root, text="Ingrese el año de su nacimiento", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calcular edad", font=("Helvetica", 18), command=age)
my_button.pack(pady=20)



root.mainloop()