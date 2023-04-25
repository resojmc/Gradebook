import tkinter as tk
import random

root = tk.Tk()
root.geometry("300x400")
root.title("Gradebook")
root.resizable(False,False)

def randint():
    n = random.randrange(50,100,1)
    return n

def get_grade():
    grades = {"Chemistry": randint(), "English": randint(), "P.E": randint(), "Algebra": randint(), "History": randint()}
    grades_data_label.config(text=f"""
    Student: {name_entry.get()}

    Grades:

    Chemistry: {grades['Chemistry']}%

    English: {grades['English']}%

    P.E: {grades['P.E']}%

    Algebra: {grades['Algebra']}%

    History: {grades['History']}%

    """)

def update_grade():
    get_grade()

main_button = tk.Button(root, text="Get Grades", command=update_grade)
main_button.place(x=228, y=370)

main_label = tk.Label(root, text="Student Gradebook", font=("Ariel", 15))
main_label.place(x=60, y=0)

name_label = tk.Label(root, text="Enter student name: ", font=("Ariel", 13))
name_label.place(x=0, y=80)

name_entry = tk.Entry(root, width=23)
name_entry.place(x=153, y=84)

grades_data_label = tk.Label(root, text=f"", font=("Ariel"), anchor="e")
grades_data_label.place(x=75, y=115)


root.mainloop()