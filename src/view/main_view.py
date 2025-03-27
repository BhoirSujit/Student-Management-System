from tkinter import *
from tkinter import ttk


class StudentManagementSystem:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Student Management System")
        self.controller = None
       

        #section
        self.frameTitle = Frame(root, border=1, relief="groove", padx=10, pady=10)
        self.frameTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.frameEntry = LabelFrame(root, text=" Enter Details ", border=1, padx=10, pady=10)
        self.frameEntry.grid(row=1, column=0, columnspan=1, sticky='nsew', padx=10, pady=10)

        self.frameData = LabelFrame(root, text=" Data ", border=1,  relief="groove", padx=10, pady=10)
        self.frameData.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Title Section
        self.labelTitle = Label(self.frameTitle, text="Student Management System", font=("Arial", 16, "bold"))
        self.labelTitle.pack()

        # Entry Data Section
        Label(self.frameEntry, text="Roll No").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.textRollno = Entry(self.frameEntry)
        self.textRollno.grid(row=0, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Name").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.textName = Entry(self.frameEntry)
        self.textName.grid(row=1, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Father Name").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.textFatherName = Entry(self.frameEntry)
        self.textFatherName.grid(row=2, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Gender").grid(row=3, column=0, sticky="nw", padx=5, pady=2)
        
        Label(self.frameEntry, text="Gender").grid(row=3, column=0, sticky="nw", padx=5, pady=2)

        # Frame for gender selection
        self.frameGender = Frame(self.frameEntry)
        self.frameGender.grid(row=3, column=1, padx=5, pady=2, sticky='w')

        # StringVar to hold selected gender
        self.genderVar = StringVar(self.frameEntry, value="male")  # Default value

        # Radio Buttons
        Radiobutton(self.frameGender, text="Male", value="Male", variable=self.genderVar).grid(row=0, column=0, sticky="w")
        Radiobutton(self.frameGender, text="Female", value="Female", variable=self.genderVar).grid(row=1, column=0, sticky="w")
        Radiobutton(self.frameGender, text="Other", value="Other", variable=self.genderVar).grid(row=2, column=0, sticky="w")
        
        Label(self.frameEntry, text="D.O.B").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        self.textDOB = Entry(self.frameEntry)
        self.textDOB.grid(row=4, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Class").grid(row=5, column=0, sticky="w", padx=5, pady=2)
        self.textClass = Entry(self.frameEntry)
        self.textClass.grid(row=5, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Section").grid(row=6, column=0, sticky="w", padx=5, pady=2)
        self.textSection = Entry(self.frameEntry)
        self.textSection.grid(row=6, column=1, padx=5, pady=2)

        Label(self.frameEntry, text="Address").grid(row=7, column=0, sticky="w", padx=5, pady=2)
        self.textAddress = Entry(self.frameEntry)
        self.textAddress.grid(row=7, column=1, padx=5, pady=2)
        
        self.operationFrame = Frame(self.frameEntry, border=1, relief='groove')
        self.operationFrame.grid(row=8, column=0,   columnspan=2, padx=5, pady=2, sticky='nsew')
        
        # Configure row & column weights to expand buttons
        self.operationFrame.columnconfigure((0, 1), weight=1)
        self.operationFrame.rowconfigure((0, 1), weight=1)
        
        self.buttonAdd = Button(self.operationFrame, text="Add", command=self.add_students)
        self.buttonAdd.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.buttonUpdate = Button(self.operationFrame, text="Update")
        self.buttonUpdate.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.buttonDelete = Button(self.operationFrame, text="Delete")
        self.buttonDelete.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.buttonClear = Button(self.operationFrame, text="Clear")
        self.buttonClear.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        # Table Data Section
        self.searchFrame = Frame(self.frameData, border=1, relief='groove')
        self.searchFrame.grid(column=0, row=0, columnspan=5, sticky="ew", padx=5, pady=5)
        
        # Configure row & column weights to expand buttons
        self.searchFrame.columnconfigure((0,1,2,3,4), weight=1)
        
        Label(self.searchFrame, text="Search").grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.textSearch = Entry(self.searchFrame)
        self.textSearch.grid(row=0, column=1, columnspan=2, sticky='ew', padx=5, pady=5)

        self.buttonSearch = Button(self.searchFrame, text="Search")
        self.buttonSearch.grid(row=0, column=3, sticky='ew', padx=5, pady=5)

        self.buttonShowAll = Button(self.searchFrame, text="Show All")
        self.buttonShowAll.grid(row=0, column=4, sticky='nsew', padx=5, pady=5)

    
        # Data Table
        columns = ("ID","Roll No", "Name", "Father Name", "Gender", "D.O.B", "Class", "Section", "Address")
        self.table = ttk.Treeview(self.frameData, columns=columns, show="headings", selectmode="browse")

        # Add headings and set column widths
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100)

        # Add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.frameData, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Grid the table and scrollbar
        self.table.grid(row=1, column=0, padx=5, pady=5, columnspan=5, rowspan=11, sticky="nsew")
        self.scrollbar.grid(row=1, column=5, sticky="ns")

        # Make frameData expand within parent
        self.frameData.columnconfigure(0, weight=1)
        self.frameData.rowconfigure(1, weight=1)

        # Bind the table selection event
        self.table.bind("<<TreeviewSelect>>", self.on_table_select)
        
        
        
    def set_controller(self, controller):
        self.controller = controller
        
    def load_students(self):
        for row in self.table.get_children():
            self.table.delete(row)
            
        students = self.controller.fetch_add_students()
        for student in students:
            self.table.insert("", "end", values=student)
    
    def add_students(self):
        self.controller.add_student(
            self.textRollno.get(),
            self.textName.get(),
            self.textFatherName.get(),
            self.genderVar.get(),
            self.textDOB.get(),
            self.textClass.get(),
            self.textSection.get(),
            self.textAddress.get()
        )
        
    
    def on_table_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item, "values")

            self.textRollno.delete(0, END)
            self.textRollno.insert(0, values[1]) 

            self.textName.delete(0, END)
            self.textName.insert(0, values[2])  

            self.textFatherName.delete(0, END)
            self.textFatherName.insert(0, values[3]) 

            self.genderVar.set(values[4])

            self.textDOB.delete(0, END)
            self.textDOB.insert(0, values[5]) 

            self.textClass.delete(0, END)
            self.textClass.insert(0, values[6]) 

            self.textSection.delete(0, END)
            self.textSection.insert(0, values[7]) 

            self.textAddress.delete(0, END)
            self.textAddress.insert(0, values[8]) 

        
    