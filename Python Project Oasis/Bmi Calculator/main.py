import json
from tkinter import *
from tkinter import messagebox
BGCOLOR = "#F6F5F2"
image_dict = {}


# THIS FUNCTION CALCULATES BODY MASS INDEX USING HEIGHT AND WEIGHT AS INPUT
def calculate_bmi(user_height, user_weight):
    user_height = int(user_height)
    user_weight = int(user_weight)
    user_bmi = user_weight / ((user_height/100) ** 2)
    return user_bmi


# THIS FUNCTION CLASSIFY YOUR WEIGHT STATUS USING BMI AS INPUT
def classify_bmi(user_bmi):
    if user_bmi < 18.5:
        return "Under weight", "#59C3AD", "under.png"
    elif user_bmi < 25:
        return "Healthy Weight", "green", "normal.png"
    elif user_bmi < 30:
        return "Over Weight", "orange", "over.png"
    else:
        return "Obesity", "red", "obes.png"


# MAIN FUNCTION
def run_main():
    height = height_input.get()
    weight = weight_input.get()
    name = name_input.get()
    age = age_input.get()
    gender = var.get()

    # THIS PART OF DATA, SETS VALIDATION INTO INPUT FIELDS FOR PROPER INPUT AND RESULT
    if (height == "") or (weight == "") or (name == "") or (age == "") or (gender == ""):
        messagebox.showinfo(title="EmptyFieldError", message="Please don't leave any fields empty!")
    elif not name.isalpha():
        messagebox.showinfo(title="InvalidNameError", message="Please enter a valid name, by only using alphabets !")
    elif not age.isdigit() or int(age) <= 2 or int(age) > 120:
        messagebox.showinfo(title="InvalidAgeError", message="Please enter a valid age 2 - 120 years !")
    elif not height.isdigit() or int(height) <= 50 or int(height) > 250:
        messagebox.showinfo(title="InvalidHeightError", message="Please enter a valid height 50 - 250cm !")
    elif not weight.isdigit() or int(weight) <= 8 or int(weight) > 500:
        messagebox.showinfo(title="InvalidWeightError", message="Please enter a valid weight 8 - 500kg !")
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        weight_status, color, image_filename = classify_bmi(bmi)
        weight_status_label.config(text=weight_status, fg=color)
        if image_filename not in image_dict:
            image_dict[image_filename] = PhotoImage(file=image_filename)
        new_body_img = image_dict[image_filename]
        canvas.itemconfig(body_img_item, image=new_body_img)
        main_label.config(text=f"Your Body Mass Index is {bmi} \nYour data is saved in the database")
        new_data = {
            name: {
                "Age": age,
                "Gender": gender,
                "BMI": bmi,
                "Weight Status": weight_status
            }
        }

        # THIS PART OF CODE IS RESPONSIBLE FOR SAVING DATA IN JSON FILE IN .json FORMAT
        try:
            with open("bmi.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("bmi.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("bmi.json", "w") as file:
                json.dump(data, file, indent=4)


# THIS FUNCTION IS USED TO RESET ALL THE INPUT FIELDS
def reset_fields():
    name_input.delete(0, END)
    age_input.delete(0, END)
    height_input.delete(0, END)
    weight_input.delete(0, END)
    var.set("")
    main_label.config(text="Welcome to Body Mass Index Calculator,\n Enter your details below")
# -------------------------------------------------  UI  -----------------------------------------------------


# THIS PART OF CODE IS THE GUI DEVELOPMENT USING TKINTER
window = Tk()
window.title("BMI Calculator")
window.config(padx=50, pady=50, bg=BGCOLOR)

# I HAVE ADDED CANVAS FOR IMAGE
canvas = Canvas(width=129, height=243, bg=BGCOLOR, highlightthickness=0)
body_img = PhotoImage(file="normal.png")
body_img_item = canvas.create_image(80, 131, image=body_img)
canvas.grid(column=2, row=1, rowspan=4)

var = StringVar()

# THIS IS WHERE ALL LABELS ARE CREATED
main_label = Label(text="Welcome to Body Mass Index Calculator,\n Enter your details below", font=("Arial", 12, "bold"), bg=BGCOLOR)
main_label.grid(column=0, row=0, columnspan=3)
name_label = Label(text="Name: ", font=("Arial", 12), bg=BGCOLOR)
name_label.grid(column=0, row=1, stick="w")
age_label = Label(text="Age: ", font=("Arial", 12), bg=BGCOLOR)
age_label.grid(column=0, row=2, stick="w")
gender_label = Label(text="Gender: ", font=("Arial", 12), bg=BGCOLOR)
gender_label.grid(column=0, row=3, stick="w")
height_label = Label(text="Height: ", font=("Arial", 12), bg=BGCOLOR)
height_label.grid(column=0, row=4, stick="w")
weight_label = Label(text="Weight: ", font=("Arial", 12), bg=BGCOLOR)
weight_label.grid(column=0, row=5, stick="w")
weight_status_label = Label(text="Healthy Weight", font=("Arial", 12, "bold"), fg="green", bg=BGCOLOR)
weight_status_label.grid(column=2, row=5, sticky="w", padx=(22, 0))

# THIS IS WHERE ALL THE INPUT TEXT BOXES ARE CREATED
name_input = Entry(width=20, font=("Arial", 10))
name_input.grid(column=1, row=1)
age_input = Entry(width=20, font=("Arial", 10))
age_input.grid(column=1, row=2)
radio_input = Radiobutton(window, text="Male", variable=var, value="Male", bg=BGCOLOR)
radio_input.grid(column=1, row=3, stick="w")
radio_input = Radiobutton(window, text="Female", variable=var, value="Female", bg=BGCOLOR)
radio_input.grid(column=1, row=3, stick="e")
height_input = Entry(width=20, font=("Arial", 10))
height_input.grid(column=1, row=4)
weight_input = Entry(width=20, font=("Arial", 10))
weight_input.grid(column=1, row=5)

# THIS IS WHERE ALL THE BUTTONS ARE CREATED
generate_button = Button(text="Calculate BMI", width=31, command=run_main, font=("Arial", 9, "bold"))
generate_button.grid(column=0, row=6, columnspan=2, pady=15)
reset_button = Button(text="Reset", width=18, command=reset_fields, font=("Arial", 9, "bold"))
reset_button.grid(column=2, row=6, pady=16)
window.mainloop()
