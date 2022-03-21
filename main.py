import tkinter as tk
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from PIL import Image, ImageTk
from student import *
from school import *

# field names for students records csv file
fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address','phone_number', 'date_of_enrollment'
    , 'year', 'major','status', 'passcode']


students_list = []  # a list of all students records
program_outlines = []  # a list of all the degree programs outlines
programs_list = []  # a list of all degree programs offered in a school


root = tk.Tk()
root.title("Student Information System")
root.geometry("600x600")

# A frame to hold all the changing widgets on a screen from page to page
frame = tk.Frame(root)
frame.pack(side="top", expand=True, fill="both")

#logo picture
logo = Image.open("dummy-logo.png")
resized_image= logo.resize((100,100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
logo_label = tk.Label(image = new_image)
logo_label.image = new_image
logo_label.place(x=50, y=30)

# header
title = tk.Label(root,text="Student Information System",font=("Calibri bold", 15))
title.place(x=200, y=65)

# login page
email_prompt = tk.Label(frame,text="Enter your email",font="Raleway")
email_prompt.place(x=100, y=150)
email = tk.Entry(frame)
email.place(x=270, y=150)

passcode_prompt = tk.Label(frame,text="Enter your passcode",font="Raleway")
passcode_prompt.place(x=100, y=190)
passcode = tk.Entry(frame)
passcode.place(x=270, y=190)


# Function for creating a student instance
def create_student(student_email, student_name, gender, date_of_birth, address, phone_number, date_of_enrollment, year,
                   major):

    if student_email == '' or student_name == '' or gender == '' or date_of_birth == '' or address == '' or \
            phone_number == '' or date_of_enrollment == '' or year == '' or major == '':

        messagebox.showwarning("Warning", "Input every field of the form!!!")

    else:
        Student(student_email, student_name, gender, date_of_birth, address, phone_number, date_of_enrollment, year, major)


# Function for capturing student information from the user before adding them to the records
def record_student_info():
    for widgets in frame.winfo_children():
        widgets.destroy()

    menu_title = tk.Label(frame, text="Enter student's information", font=("Calibri bold", 15))
    menu_title.place(x=150, y=70)
    name_prompt = tk.Label(frame, text="Student's name", font="Raleway")
    name_prompt.place(x=100, y=150)
    name = tk.Entry(frame)
    name.place(x=300, y=150)

    email_prompt = tk.Label(frame, text="Student's email", font="Raleway")
    email_prompt.place(x=100, y=190)
    email = tk.Entry(frame)
    email.place(x=300, y=190)

    gender_prompt = tk.Label(frame, text="Student's gender", font="Raleway")
    gender_prompt.place(x=100, y=230)
    gender = tk.Entry(frame)
    gender.place(x=300, y=230)

    dob_prompt = tk.Label(frame, text="Student's date of birth", font="Raleway")
    dob_prompt.place(x=100, y=270)
    dob = tk.Entry(frame)
    dob.place(x=300, y=270)

    address_prompt = tk.Label(frame, text="Student's address", font="Raleway")
    address_prompt.place(x=100, y=310)
    address = tk.Entry(frame)
    address.place(x=300, y=310)

    phone_prompt = tk.Label(frame, text="Student's phone number", font="Raleway")
    phone_prompt.place(x=100, y=350)
    phone = tk.Entry(frame)
    phone.place(x=300, y=350)

    major_prompt = tk.Label(frame, text="Student's major", font="Raleway")
    major_prompt.place(x=100, y=390)
    major = tk.Entry(frame)
    major.place(x=300, y=390)

    enrollment_prompt = tk.Label(frame, text="Date of enrollment", font="Raleway")
    enrollment_prompt.place(x=100, y=430)
    enrollment = tk.Entry(frame)
    enrollment.place(x=300, y=430)

    year_prompt = tk.Label(frame, text="What year is the student in", font="Raleway")
    year_prompt.place(x=100, y=470)
    year = tk.Entry(frame)
    year.place(x=300, y=470)

    register = tk.Button(frame, text="Register", command=lambda:create_student(email.get(), name.get(), gender.get(),
            dob.get(), address.get(), phone.get(),enrollment.get(), year.get(), major.get()), font="Calibri",
            bg="#000000", fg="white", height=1, width=15)

    register.place(x=200, y=530)


# Function to capture student email the user would like to view information for or update
def get_student_email(action):
    for widgets in frame.winfo_children():
        widgets.destroy()

        email_prompt = tk.Label(frame, text="Enter the Student's email", font="Raleway")
        email_prompt.place(x=100, y=150)
        email = tk.Entry(frame)
        email.place(x=310, y=150)

    if action == "view":
        send = tk.Button(frame, text="send",command=lambda:view_student(email.get()), font="Calibri", bg="#000000", fg="white", height=1, width=15)
        send.place(x=200, y=220)

    elif action == "update":
        send = tk.Button(frame, text="send", command=lambda: update_student(email.get()), font="Calibri", bg="#000000",
                         fg="white", height=1, width=15)
        send.place(x=200, y=220)


# function to save updated student's information into the school records
def save_new_student_info(students_list,updated_student):
    students_list.append(updated_student)
    try:
        with open("student_records.csv", 'w', newline="") as new_student_records:
            write_student = csv.DictWriter(new_student_records, fieldnames=fieldnames)
            for student in students_list:
                write_student.writerow(
                    {"student_email": student[0], "student_name": student[1], "gender": student[2],
                     "date_of_birth": student[3], "address": student[4], "phone_number": student[5],
                     "date_of_enrollment": student[6], "year": student[7], "major": student[8],
                     'status': student[9], "passcode": student[10]})

            messagebox.showinfo("Message", "Student updated successfully!!!")

    except OSError as e:
        messagebox.showwarning("Warning", "Could not save changes!!!")


# Function to capture student's updated information
def update_student(email):
    for widgets in frame.winfo_children():
        widgets.destroy()

    students_list.clear()
    try:
        with open("student_records.csv", 'r') as student_records:
            read_student = csv.reader(student_records)
            for student in read_student:
                if email == student[0]:
                    email_prompt = tk.Label(frame, text="Student's email", font="Raleway")
                    email_prompt.place(x=100, y=190)
                    email = tk.Entry(frame)
                    email.insert(tk.END, student[0])
                    email.place(x=300, y=190)

                    name_prompt = tk.Label(frame, text="Student's name", font="Raleway")
                    name_prompt.place(x=100, y=150)
                    name = tk.Entry(frame)
                    name.insert(tk.END, student[1])
                    name.place(x=300, y=150)

                    gender_prompt = tk.Label(frame, text="Student's gender", font="Raleway")
                    gender_prompt.place(x=100, y=230)
                    gender = tk.Entry(frame)
                    gender.insert(tk.END, student[2])
                    gender.place(x=300, y=230)

                    dob_prompt = tk.Label(frame, text="Student's date of birth", font="Raleway")
                    dob_prompt.place(x=100, y=270)
                    dob = tk.Entry(frame)
                    dob.insert(tk.END, student[3])
                    dob.place(x=300, y=270)

                    address_prompt = tk.Label(frame, text="Student's address", font="Raleway")
                    address_prompt.place(x=100, y=310)
                    address = tk.Entry(frame)
                    address.insert(tk.END, student[4])
                    address.place(x=300, y=310)

                    phone_prompt = tk.Label(frame, text="Student's phone number", font="Raleway")
                    phone_prompt.place(x=100, y=350)
                    phone = tk.Entry(frame)
                    phone.insert(tk.END, student[5])
                    phone.place(x=300, y=350)

                    major_prompt = tk.Label(frame, text="Date of enrollment", font="Raleway")
                    major_prompt.place(x=100, y=390)
                    major = tk.Entry(frame)
                    major.insert(tk.END, student[6])
                    major.place(x=300, y=390)

                    enrollment_prompt = tk.Label(frame, text="What year is the student in", font="Raleway")
                    enrollment_prompt.place(x=100, y=430)
                    enrollment = tk.Entry(frame)
                    enrollment.insert(tk.END, student[7])
                    enrollment.place(x=300, y=430)

                    year_prompt = tk.Label(frame, text="Student's major", font="Raleway")
                    year_prompt.place(x=100, y=470)
                    year = tk.Entry(frame)
                    year.insert(tk.END, student[8])
                    year.place(x=300, y=470)

                    status_prompt = tk.Label(frame, text="Student's status", font="Raleway")
                    status_prompt.place(x=100, y=510)
                    status = tk.Entry(frame)
                    status.insert(tk.END, student[9])
                    status.place(x=300, y=510)

                    password = student[10]

                else:
                    students_list.append(student)

            save = tk.Button(frame, text="Save", command=lambda: save_new_student_info(students_list,[email.get(), name.get(), gender.get(),
            dob.get(), address.get(), phone.get(),enrollment.get(), year.get(), major.get(),status.get(),password]),
                             font="Calibri", bg="#000000", fg="white", height=1, width=25)
            save.place(x=200, y=550)

    except OSError as e:
        messagebox.showwarning("Warning", "Could not retrieve student information!!!")


# Function to display student's information to the user
def view_student(email,user="admin"):
    for widgets in frame.winfo_children():
        widgets.destroy()
    try:
        with open("student_records.csv", 'r') as student_records:
            read_student = csv.reader(student_records)
            next(read_student)
            for student in read_student:
                if email == student[0]:
                    field_name_location = 100
                    value_location = 250
                    y_axis_position = 150
                    for i in range(len(fieldnames) - 1):
                        tk.Label(frame, text=fieldnames[i] + ":", font="Raleway").place(x=field_name_location, y=y_axis_position)
                        tk.Label(frame, text=student[i], font="Raleway").place(x=value_location, y=y_axis_position)
                        y_axis_position += 30
                    break

            else:
                messagebox.showwarning("Warning", "Could not retrieve student information!!!")
    except OSError as e:
        messagebox.showwarning("Warning", "Could not retrieve student information!!!")

    if user == "student":
        update_btn = tk.Button(frame, text="update", command=lambda: update_student(email),
                         font="Calibri",
                         bg="#000000", fg="white", height=1, width=17)
        update_btn.place(x=200, y=530)


# Function to create a school instance from the information passed to it
def create_school(link,index,school_name,programs):
    program_outlines.append(link)
    index += 1
    if index == len(programs):
        School(school_name, programs, program_outlines)
    else:
        upload_outlines(school_name,index,programs)


# function to allow user to upload a degree program outline for each program offered by the user
def upload_outlines(school_name,index,programs):
    for widgets in frame.winfo_children():
        widgets.destroy()

    title = tk.Label(frame, text="Enter a link to the degree program outline", font=("Calibri bold", 15))
    title.place(x=100, y=150)

    lab = tk.Label(frame, text=programs[index], font="Raleway")
    lab.place(x=100, y=200)
    value = tk.Entry(frame, width=35)
    value.place(x=250, y=200)

    next = tk.Button(frame, text="Next", command=lambda: create_school(value.get(), index,school_name,programs), font="Calibri",
                     bg="#000000", fg="white", height=1, width=17)
    next.place(x=200, y=250)


# Function to capture all the required information about the school from the user
def set_up_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()

    menu_title = tk.Label(frame, text="Enter school information", font=("Calibri bold", 15))
    menu_title.place(x=150, y=70)

    name_prompt = tk.Label(frame, text="School name", font="Raleway")
    name_prompt.place(x=100, y=150)
    name = tk.Entry(frame, width=35)
    name.place(x=300, y=150)

    programs_prompt = tk.Label(frame, text="Degree programs", font="Raleway")
    programs_prompt.place(x=100, y=190)
    programs = tk.Entry(frame, width=35)
    programs.place(x=300, y=190)
    programs_prompt = tk.Label(frame,
                               text="*List degree programs\nseparated by a comma\navoid spaces before or\nafter the comma*",
                               font=("Raleway italic", 9), fg="gray", justify=tk.LEFT)
    programs_prompt.place(x=100, y=220)
    index = 0

    next = tk.Button(frame, text="next", command=lambda: upload_outlines(name.get(),index,programs.get().split(",")), font="Calibri", bg="#000000", fg="white",
                     height=1, width=17)
    next.place(x=200, y=310)


# Function to open a link to a degree program outline in the user's default browser
def open_url(url):
    webbrowser.open_new_tab(url)


# Function to allow user to view a degree program outline
def view_outline():
    for widgets in frame.winfo_children():
      widgets.destroy()

    title = tk.Label(frame, text="The outline document will be opened in the browser once you click on a program",
                     font=("Calibri bold", 15))
    title.place(x=50, y=150)

    warning = tk.Label(frame, text="If you can not see anything, it means that no outline was added.", font=("Calibri", 12))
    warning.place(x=50, y=180)

    try:
        with open("degree_programs.csv", 'r') as programs_records:
            read_program = csv.reader(programs_records)

            field_name_location = 200
            y_axis_position = 240

            for program in read_program:
                program_name =tk.Label(frame, text=program[0], font="Raleway")
                program_name.pack(pady=15)
                program_name.place(x=field_name_location, y=y_axis_position)

                # Define the URL to open
                url = program[2]

                # Bind the label with the URL to open in a new tab
                program_name.bind("<Button-1>", lambda e: open_url(url))
                y_axis_position += 30

    except OSError as e:
        messagebox.showwarning("Warning", "Could not retrieve degree programs outlines!!!")


# Function to allow a user to visualize proportions of students in each degree program
def visualize():
    labels_dict = {}
    try:
        with open("degree_programs.csv", 'r') as programs_records:
            read_program = csv.reader(programs_records)

            for program in read_program:
                labels_dict[program[0]]=0

        with open("student_records.csv", 'r') as students_records:
            read_students = csv.reader(students_records)
            next(read_students)
            for student in read_students:
                labels_dict[student[8]] += 1
    except OSError as e:
        messagebox.showwarning("Warning", "Could not retrieve data for visualization!!!")

    data_labels = []
    data_points = []
    for key in labels_dict:
        data_labels.append(key)
        data_points.append(labels_dict[key])
    y = np.array(data_points)
    plt.pie(y, labels=data_labels)
    plt.show()


# Function to display of different operations a user can do with different access level i.e:student & administration
# member
def display_menu(user_type,student_email=""):
    for widgets in frame.winfo_children():
        widgets.destroy()

    menu_title = tk.Label(frame, text="Choose from the menu what you would like to do.", font=("Calibri bold", 15))
    menu_title.place(x=100, y=150)

    if user_type == "admin":
        set_up = tk.Button(frame, text="Set up",command=lambda: set_up_menu(), font="Calibri",bg="#000000", fg="white", height=1, width=25)
        set_up.place(x=200, y=200)

        register = tk.Button(frame, text="Register a student", command=lambda: record_student_info(),font="Calibri", bg="#000000", fg="white",
                             height=1, width=25)
        register.place(x=200, y=250)
        view = tk.Button(frame, text="View student", command=lambda: get_student_email("view"), font="Calibri", bg="#000000", fg="white",
                         height=1, width=25)
        view.place(x=200, y=300)
        update = tk.Button(frame, text="update student", command=lambda: get_student_email("update"), font="Calibri", bg="#000000", fg="white",
                           height=1, width=25)
        update.place(x=200, y=350)
        view_program = tk.Button(frame, text="view degree program outline", command=lambda: view_outline(), font="Calibri", bg="#000000", fg="white",
                                 height=1, width=25)
        view_program.place(x=200, y=400)
        visualize_btn = tk.Button(frame, text="visualize", command=lambda: visualize(), font = "Calibri", bg="#000000",
                                  fg="white",height=1, width=25)
        visualize_btn.place(x=200, y=450)

    elif user_type == "student":
        view = tk.Button(frame, text="View student", command=lambda: view_student(student_email,"student"), font="Calibri",
                         bg="#000000", fg="white",height=1, width=25)
        view.place(x=200, y=200)
        view_program = tk.Button(frame, text="view degree program outline", command=lambda: view_outline(),
                                 font="Calibri", bg="#000000", fg="white", height=1, width=25)
        view_program.place(x=200, y=250)


# Function to capture student's password once they register
def update_passcode(updated_student):
    try:
        with open("student_records.csv", 'r') as student_records:
            read_student = csv.reader(student_records)
            for student in read_student:
                if student[0] == updated_student[0]:
                    students_list.append(updated_student)
                else:
                    students_list.append(student)

        with open("student_records.csv", 'w', newline="") as new_student_records:
            write_student = csv.DictWriter(new_student_records, fieldnames=fieldnames)
            for student in students_list:
                write_student.writerow(
                    {"student_email": student[0], "student_name": student[1], "gender": student[2],
                     "date_of_birth": student[3], "address": student[4], "phone_number": student[5],
                     "date_of_enrollment": student[6], "year": student[7], "major": student[8],
                     'status': student[9], "passcode": student[10]})

            messagebox.showinfo("Message", "Registration successful!!!")
            display_menu("student")

    except OSError as e:
        messagebox.showwarning("Warning", "Registration unsuccessful!!!")


# Function to authenticate the user before they are logged in
def authenticate(action):
    user_email = email.get()
    user_passcode = passcode.get()

    # The administration will have a single email and password
    if user_email == "a" and user_passcode == "a":
        for widgets in frame.winfo_children():
            widgets.destroy()
        display_menu("admin")

    else:
        try:
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                next(read_student)
                for student in read_student:
                    if user_email == student[0]:
                        if not student[10]:
                            student[10]=user_passcode
                            update_passcode(student)
                        elif student[10] and action == "register":
                            messagebox.showwarning("Warning", "You can not register twice with the same email!!")
                        elif user_passcode == student[10]:
                            display_menu("student",user_email)
                        elif user_passcode != student[10]:
                            messagebox.showwarning("Warning", "Password incorrect")
                        break
                else:
                    messagebox.showwarning("Warning", "You are not recognized as a student of this school or admin hence you are not allowed to register!!!")
        except OSError as e:
            messagebox.showwarning("Warning", "Failed to authenticate :(")


# Function to capture student's credentials when they are registering
def register():
    submit_btn.destroy()
    register_label.destroy()

    register_btn = tk.Button(frame, text="Register", command=lambda: authenticate("register"), font="Raleway", bg="#000000",
                           fg="white", height=1, width=15)
    register_btn.place(x=200, y=260)


# submit button on the login page
submit_btn = tk.Button(frame, text = "Log In", command=lambda:authenticate("login"), font="Raleway",bg = "#000000",
                       fg="white",height=1, width=15)
submit_btn.place(x=200, y=260)

register_label =tk.Label(frame, text="Register", font=("Raleway bold", 15), fg= "blue" )
register_label.pack(pady=0)
register_label.place(x=400, y=270)

# Bind the register label with the function to capture registration information
register_label.bind("<Button-1>", lambda e: register())

root.mainloop()