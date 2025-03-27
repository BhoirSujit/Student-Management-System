CREATE DATABASE school;

CREATE TABLE student (
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
