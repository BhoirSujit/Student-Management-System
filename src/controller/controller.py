from model.model import Database

class Controller:
    def __init__(self, view):
        self.db = Database()
        self.view = view
        self.view.set_controller(self)
        self.view.load_students()
        
    def add_student(self,roll_no, name, father_name, gender, dob, class_name, section, address):
        self.db.insert_student(roll_no, name, father_name, gender, dob, class_name, section, address)
        self.view.load_students()
        
    def fetch_add_students(self):
        return self.db.fetch_students()