import tkinter as tk


root = tk.Tk()
root.title("Radio Buttons Example")

# Variable to store the selected option
gender = tk.StringVar()

# Create radio buttons
radio = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
radio.pack()
radio = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
radio.pack()
print(gender.get())
root.mainloop()

