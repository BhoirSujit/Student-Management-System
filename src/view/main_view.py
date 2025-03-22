from tkinter import *


class StudentManagementSystem:
    def __init__(self, root: Tk):
        root.title("Student Management System")

        root.size = (100, 100)

        #sections
        frameTitle = Frame(root, border=10)
        frameTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        frameEntry = LabelFrame(root, text="Enter Details")
        frameEntry.grid(row=1, column=0, columnspan=1, sticky='w', padx=10, pady=10)

        frameData = Frame(root)
        frameData.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        
        #title section
        labelTitle = Label(frameTitle, text="Student Management System")
        labelTitle.pack()

        #entry data section
        labelrollno = Label(frameEntry, text="Roll No")
        textRollno = Text(frameEntry, height=1)
        labelrollno.grid(row=0, column=0)
        textRollno.grid(row=0, column=1)

        labelName = Label(frameEntry, text="Name")
        textName = Text(frameEntry, height=1)
        labelName.grid(row=1, column=0)
        textName.grid(row=1, column=1) 
        
        labelFatherName = Label(frameEntry, text="Father Name")
        textFatherName = Text(frameEntry, height=1)
        labelFatherName.grid(row=2, column=0)
        textFatherName.grid(row=2, column=1)

        labelGender = Label(frameEntry, text="Gender")
        textGender = Text(frameEntry, height=1)
        labelGender.grid(row=3, column=0)
        textGender.grid(row=3, column=1)

        labelDOB = Label(frameEntry, text="D.O.B")
        textDOB = Text(frameEntry, height=1)
        labelDOB.grid(row=4, column=0)
        textDOB.grid(row=4, column=1)

        labelClass = Label(frameEntry, text="Class")
        textClass = Text(frameEntry, height=1)
        labelClass.grid(row=5, column=0)
        textClass.grid(row=5, column=1)

        labelSection = Label(frameEntry, text="Section")
        textSection = Text(frameEntry, height=1)
        labelSection.grid(row=6, column=0)
        textSection.grid(row=6, column=1)

        labelAddress = Label(frameEntry, text="Address")
        textAddress = Text(frameEntry, height=1)
        labelAddress.grid(row=7, column=0)
        textAddress.grid(row=7, column=1)

        #table data section



        table = Listbox(frameData);
        table.pack(fill='both')