from tkinter import *
import random
import string
import pyperclip
from tkinter import *

FONT = "Verdana"


def generate_password(event=None):
    length = int(length_slider.get())
    length_value_label.config(text=length)
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    exclude_chars = exclude_entry.get()

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        password_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    strength = ""
    color = "black"
    if length >= 12 or (use_lowercase and use_uppercase and use_numbers and use_symbols):
        strength = "Strong"
        color = "red"
    elif length > 8 or ((use_lowercase or use_uppercase) and (use_numbers or use_symbols)):
        strength = "Moderate"
        color = "#c65102"
    else:
        strength = "Weak"
        color = "green"

    # Check if all selected character types are used and password length is more than 12
    contains_lowercase = any(c in string.ascii_lowercase for c in password)
    contains_uppercase = any(c in string.ascii_uppercase for c in password)
    contains_numbers = any(c in string.digits for c in password)
    contains_symbols = any(c in string.punctuation for c in password)

    password_label.config(text=password)
    strength_label.config(text=strength, fg=color)
    pyperclip.copy(password)  # Copy generated password to clipboard


def refresh_password():
    generate_password()


# Create main window
window = Tk()
window.title("Password Generator")
window.config(padx=30, pady=20)

# Create widgets
length_slider = Scale(window, from_=6, to=20, orient="horizontal", length=195, command=generate_password)
length_value_label = Label(window, text=int(length_slider.get()), font=(FONT, 12))  # Convert to integer

lowercase_var = BooleanVar(value=True)
lowercase_check = Checkbutton(window, text="Include lowercase letters", variable=lowercase_var,
                                  command=generate_password)

uppercase_var = BooleanVar(value=True)
uppercase_check = Checkbutton(window, text="Include uppercase letters", variable=uppercase_var,
                                  command=generate_password)

numbers_var = BooleanVar(value=True)
numbers_check = Checkbutton(window, text="Include numbers", variable=numbers_var, command=generate_password)

symbols_var = BooleanVar(value=True)
symbols_check = Checkbutton(window, text="Include symbols", variable=symbols_var, command=generate_password)

exclude_label = Label(window, text="Exclude Characters:", font=(FONT, 11))
exclude_entry = Entry(window, width=41)
exclude_entry.bind("<KeyRelease>", generate_password)  # Bind KeyRelease event to password generation function

refresh_button = Button(window, text="Refresh", command=refresh_password, width=10)

copy_button = Button(window, text="Copy", command=lambda: pyperclip.copy(password_label.cget("text")), width=10)
password_label = Label(window, text="Password", font=(FONT, 11))
strength_label = Label(window, text="Strength", font=(FONT, 8), fg="black")
# Grid layout
password_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=(4, 0), pady=(0, 22))
strength_label.grid(row=0, column=0, padx=(4, 0), pady=(18, 0), sticky="w")
copy_button.grid(row=3, column=1, sticky="e")
refresh_button.grid(row=4, column=1, sticky="e")

length_slider.grid(row=0, column=1, sticky="w", padx=(60, 0), pady=(0, 13))

exclude_label.grid(row=1, column=0, sticky="w", padx=(4, 0), pady=(0, 5))
exclude_entry.grid(row=1, column=1, padx=(6, 0), pady=(0, 5), sticky="w")

lowercase_check.grid(row=3, column=0, sticky="w", padx=5, pady=5)
uppercase_check.grid(row=4, column=0, sticky="w", padx=5, pady=5)
numbers_check.grid(row=3, column=1, sticky="w", padx=5, pady=5)
symbols_check.grid(row=4, column=1, sticky="w", padx=5, pady=5)

# Run the main event loop
window.mainloop()
