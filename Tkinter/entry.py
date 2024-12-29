import tkinter as tk
from tkinter import ttk, messagebox
import csv

# Function to save data
def save_data():
    fname = fname_entry.get().strip()
    lname = lname_entry.get().strip()
    gender = gender_combobox.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()
    number = number_entry.get().strip()
    address = address_text.get("1.0", tk.END).strip()

    if not fname or not lname:
        messagebox.showerror("Error", "First Name and Last Name are required!")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a valid number!")
        return

    if not number.isdigit():
        messagebox.showerror("Error", "Contact number must be a valid number!")
        return

    info = [fname, lname, gender, int(age), email, int(number), address]
    with open('info.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(info)

    messagebox.showinfo("Success", "Data Saved Successfully!")

    # Clear input fields
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    gender_combobox.set("")
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)

# Function to search data
def search_data():
    search_text = search_entry.get().strip()
    if not search_text:
        messagebox.showerror("Error", "Please enter a first name to search!")
        return

    found = False
    try:
        with open('info.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].lower() == search_text.lower():
                    search_output.config(state="normal")
                    search_output.delete("1.0", tk.END)
                    search_output.insert(
                        "1.0", \
                        f"First Name: {row[0]}\nLast Name: {row[1]}\nGender: {row[2]}\nAge: {row[3]}\n"
                        f"Email: {row[4]}\nNumber: {row[5]}\nAddress: {row[6]}"
                    )
                    search_output.config(state="disabled")
                    found = True
                    break
        if not found:
            search_output.config(state="normal")
            search_output.delete("1.0", tk.END)
            search_output.insert("1.0", "No match found.")
            search_output.config(state="disabled")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found!")

# Function to clear search
def clear_search():
    search_entry.delete(0, tk.END)
    search_output.config(state="normal")
    search_output.delete("1.0", tk.END)
    search_output.config(state="disabled")

# Function to view all names
def view_all_names():
    try:
        with open('info.csv', 'r') as file:
            reader = csv.reader(file)
            names = [f"{row[0]} {row[1]}" for row in reader if row]
            all_names_output.config(state="normal")
            all_names_output.delete("1.0", tk.END)
            all_names_output.insert("1.0", "\n".join(names))
            all_names_output.config(state="disabled")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found!")

# Main window
root = tk.Tk()
root.title("Contact Entry")
root.configure(bg="gray14")
root.maxsize(800, 500)
root.minsize(400, 250)

# Input section
input_frame = tk.Frame(root, bg="gray14")
input_frame.pack(padx=10, pady=10, fill="x")

tk.Label(input_frame, text="Enter First Name:", bg="gray14", fg="DeepSkyBlue2").grid(row=0, column=0, sticky="w")
fname_entry = tk.Entry(input_frame)
fname_entry.grid(row=0, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Last Name:", bg="gray14", fg="DeepSkyBlue2").grid(row=1, column=0, sticky="w")
lname_entry = tk.Entry(input_frame)
lname_entry.grid(row=1, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Gender:", bg="gray14", fg="DeepSkyBlue2").grid(row=2, column=0, sticky="w")
gender_combobox = ttk.Combobox(input_frame, values=["Male", "Female", "Other"])
gender_combobox.grid(row=2, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Age:", bg="gray14", fg="DeepSkyBlue2").grid(row=3, column=0, sticky="w")
age_entry = tk.Entry(input_frame)
age_entry.grid(row=3, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Email:", bg="gray14", fg="DeepSkyBlue2").grid(row=4, column=0, sticky="w")
email_entry = tk.Entry(input_frame)
email_entry.grid(row=4, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Number:", bg="gray14", fg="DeepSkyBlue2").grid(row=5, column=0, sticky="w")
number_entry = tk.Entry(input_frame)
number_entry.grid(row=5, column=1, sticky="ew")

tk.Label(input_frame, text="Enter Address:", bg="gray14", fg="DeepSkyBlue2").grid(row=6, column=0, sticky="nw")
address_text = tk.Text(input_frame, height=4, width=30)
address_text.grid(row=6, column=1, sticky="ew")

save_button = tk.Button(input_frame, text="Save", bg="MediumPurple2", fg="white", command=save_data)
save_button.grid(row=7, column=0, pady=10)

cancel_button = tk.Button(input_frame, text="Cancel", bg="Firebrick", fg="white", command=root.quit)
cancel_button.grid(row=7, column=1, pady=10)

# Separator
ttk.Separator(root, orient="horizontal").pack(fill="x", pady=10)

# Search section
search_frame = tk.Frame(root, bg="gray14")
search_frame.pack(padx=10, pady=10, fill="x")

tk.Label(search_frame, text="Search by First Name:", bg="gray14", fg="DeepSkyBlue2").grid(row=0, column=0, sticky="w")
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, sticky="ew")

search_button = tk.Button(search_frame, text="Search", bg="MediumPurple2", fg="white", command=search_data)
search_button.grid(row=1, column=0, pady=10)

clear_button = tk.Button(search_frame, text="Clear", bg="Firebrick", fg="white", command=clear_search)
clear_button.grid(row=1, column=1, pady=10)

search_output = tk.Text(search_frame, height=4, width=40, state="disabled", bg="white", fg="DeepSkyBlue2")
search_output.grid(row=2, column=0, columnspan=2, sticky="ew")

# View all names section
view_all_frame = tk.Frame(root, bg="gray14")
view_all_frame.pack(padx=10, pady=10, fill="x")

view_all_button = tk.Button(view_all_frame, text="View All Names", bg="DeepSkyBlue2", fg="white", command=view_all_names)
view_all_button.grid(row=0, column=0, pady=10)

all_names_output = tk.Text(view_all_frame, height=10, width=40, state="disabled", bg="white", fg="DeepSkyBlue2")
all_names_output.grid(row=1, column=0, columnspan=2, sticky="ew")

# Start the application
root.mainloop()