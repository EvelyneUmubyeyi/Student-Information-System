import csv
from tkinter import messagebox

fieldnames = ["program","outline"]
class School:
    def __init__(self,name,degree_programs,program_outlines):
        self.name = name
        self.degreePrograms = degree_programs
        self.program_outlines = program_outlines
        try:
            for index in range(len(self.degreePrograms)):
               with open("degree_programs.csv", 'a', newline='') as add_record:
                   record_program = csv.DictWriter(add_record,fieldnames=fieldnames)
                   record_program.writerow({"program":self.degreePrograms[index],"outline":self.program_outlines[index]})

            messagebox.showinfo("Message","School " + self.name + " was set up successfully!!!")
        except OSError as e:
            messagebox.showwarning("Warning", "Could not successfully register the student!!!")




