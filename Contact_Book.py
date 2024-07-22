import tkinter as tk
from tkinter import messagebox

import mysql.connector

# Initialize Tkinter
root = tk.Tk()
root.title("Contact Book")

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Krish5671@",
    database="codsoft"
)
mycursor = mydb.cursor()


# Function to add a new contact
def add_contact():
    # Example: Get values from entry fields
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()  # Get address from Text widget

    # Insert into database
    sql = "INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)"
    val = (name, phone, email, address)
    mycursor.execute(sql, val)
    mydb.commit()

    # Clear entry fields after adding
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

    messagebox.showinfo("Success", "Contact added successfully.")


# Function to view all contacts
def view_contacts():
    # Clear previous listbox content
    contacts_listbox.delete(0, tk.END)

    # Fetch all contacts from database
    mycursor.execute("SELECT name, phone FROM contacts")
    contacts = mycursor.fetchall()

    # Display contacts in listbox
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")


# Function to search contacts
def search_contacts():
    # Example: Get search term
    search_term = search_entry.get()

    # Clear previous listbox content
    contacts_listbox.delete(0, tk.END)

    # Search contacts from database
    sql = "SELECT name, phone FROM contacts WHERE name LIKE %s OR phone LIKE %s"
    val = (f"%{search_term}%", f"%{search_term}%")
    mycursor.execute(sql, val)
    contacts = mycursor.fetchall()

    # Display search results in listbox
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")


# Function to update a contact
def update_contact():
    # Example: Get selected contact from listbox
    selected_contact = contacts_listbox.curselection()
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to update.")
        return

    # Get new values from entry fields
    new_phone = new_phone_entry.get()
    new_email = new_email_entry.get()
    new_address = new_address_entry.get("1.0", tk.END).strip()

    # Update contact in database
    selected_index = selected_contact[0]
    contact_info = contacts_listbox.get(selected_index)
    contact_name = contact_info.split(" - ")[0]

    sql = "UPDATE contacts SET phone = %s, email = %s, address = %s WHERE name = %s"
    val = (new_phone, new_email, new_address, contact_name)
    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Contact updated successfully.")

    # Clear entry fields after updating
    new_phone_entry.delete(0, tk.END)
    new_email_entry.delete(0, tk.END)
    new_address_entry.delete("1.0", tk.END)


# Function to delete a contact
def delete_contact():
    # Example: Get selected contact from listbox
    selected_contact = contacts_listbox.curselection()
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    # Get contact details from listbox
    selected_index = selected_contact[0]
    contact_info = contacts_listbox.get(selected_index)
    contact_name = contact_info.split(" - ")[0]

    # Delete contact from database
    sql = "DELETE FROM contacts WHERE name = %s"
    val = (contact_name,)
    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Contact deleted successfully.")
    # Refresh contact list after deletion
    view_contacts()


# GUI Layout
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Text(root, height=4, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# Listbox to display contacts
contacts_listbox = tk.Listbox(root, height=10, width=50)
contacts_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# Search entry and button
tk.Label(root, text="Search:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)
search_button = tk.Button(root, text="Search", command=search_contacts)
search_button.grid(row=7, column=1, padx=10, pady=5, sticky=tk.E)

# Update contact section
tk.Label(root, text="New Phone").grid(row=8, column=0, padx=10, pady=5)
new_phone_entry = tk.Entry(root)
new_phone_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="New Email").grid(row=9, column=0, padx=10, pady=5)
new_email_entry = tk.Entry(root)
new_email_entry.grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="New Address").grid(row=10, column=0, padx=10, pady=5)
new_address_entry = tk.Text(root, height=4, width=30)
new_address_entry.grid(row=10, column=1, padx=10, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# Delete contact button
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# Start the main loop
root.mainloop()

# Close database connection
mydb.close()
