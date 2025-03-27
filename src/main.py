from view.main_view import StudentManagementSystem
from controller.controller import Controller
import tkinter

if __name__ == "__main__":
    root = tkinter.Tk()
    app = StudentManagementSystem(root)
    controller = Controller(app)
    root.mainloop()