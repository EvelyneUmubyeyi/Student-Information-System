import csv
from tkinter import messagebox

fieldnames = ['student_email', 'student_name', 'gender', 'date_of_birth', 'address',
                                      'phone_number', 'date_of_enrollment', 'year', 'major','status', 'passcode']

class Student:
    def __init__(self,student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year, major, status="current"):
        self.student_email = student_email
        self.student_name = student_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.major = major
        self.date_of_enrollment = date_of_enrollment
        self.year = year
        self.passcode = None
        self.status = status
        try:
            with open("student_records.csv", 'r') as student_records:
                read_student = csv.reader(student_records)
                for student in read_student:
                    if self.student_email in student:
                        break
                else:
                    with open("student_records.csv", 'a', newline='') as add_record:
                        record_student = csv.DictWriter(add_record, fieldnames=fieldnames)
                        record_student.writerow(
                            {"student_email": self.student_email, "student_name": self.student_name,
                             "gender": self.gender,
                             "date_of_birth": self.date_of_birth, "address": self.address,
                             "phone_number": self.phone_number, "date_of_enrollment": self.date_of_enrollment,
                             "year": self.year, "major": self.major, 'status': self.status, "passcode": self.passcode})

                messagebox.showinfo("Message","Student registered successfully!!!")
        except OSError as e:
            messagebox.showwarning("Warning", "Could not successfully register the student!!!")

