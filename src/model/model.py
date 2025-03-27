import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="school",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        
        self.cursor = self.connection.cursor()
        self.create_table()
        print("database connected")
        
    def create_table(self) :
        query = """
        CREATE TABLE IF NOT EXISTS student (
            id SERIAL PRIMARY KEY,
            roll_no VARCHAR(10) NOT NULL UNIQUE,
            student_name VARCHAR(100) NOT NULL,
            father_name VARCHAR(100) NOT NULL,
            gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other')),
            dob DATE NOT NULL CHECK (dob <= CURRENT_DATE), 
            class_name VARCHAR(50) NOT NULL,
            section VARCHAR(10), 
            address VARCHAR(500)
        );
        """
        
        self.cursor.execute(query)
        self.connection.commit()
        
    def insert_student(self,roll_no, name, father_name, gender, dob, class_name, section, address):
        query = """
        INSERT INTO student (roll_no, student_name, father_name, gender, dob, class_name, section, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        
        self.cursor.execute(query, (roll_no, name, father_name, gender, dob, class_name, section, address))
        self.connection.commit()
        return self.cursor.fetchone()[0]
    
    def fetch_students(self):
        self.cursor.execute("SELECT * FROM student")
        return self.cursor.fetchall()
    
