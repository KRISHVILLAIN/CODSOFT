import random
import string
import tkinter as tk


def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_and_display_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=5)
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Use Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Use Numbers", variable=numbers_var)
numbers_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Use Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root, width=40)
password_entry.pack()

root.mainloop()
