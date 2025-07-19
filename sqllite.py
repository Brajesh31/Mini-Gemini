# This is an Sample database You can use Your own database
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("StudentInfo.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Define the SQL query to create the table
table_info = """
CREATE TABLE STUDENT_INFO (
    Firstname VARCHAR(25),
    Lastname VARCHAR(25),
    Date_of_Birth DATE,
    Degree VARCHAR(50),
    CGPA FLOAT,
    Department VARCHAR(50),
    College VARCHAR(100),
    Country VARCHAR(50)
);
"""

# Execute the SQL query to create the table
cursor.execute(table_info)

# Define sample data to be inserted into the table
sample_data = [
    ('John', 'Doe', '1998-05-15', 'Computer Science', 3.8, 'Engineering', 'ABC University', 'USA'),
    ('Jane', 'Smith', '1997-09-20', 'Electrical Engineering', 3.5, 'Engineering', 'XYZ College', 'Canada'),
    ('Michael', 'Johnson', '1999-02-10', 'Mathematics', 3.9, 'Science', 'PQR Institute', 'UK'),
    ('Emily', 'Brown', '1998-07-01', 'Business Administration', 3.6, 'Business', 'LMN College', 'Australia'),
    ('David', 'Lee', '1997-12-25', 'Physics', 3.7, 'Science', 'EFG University', 'Germany'),
    ('Sarah', 'Taylor', '1999-04-18', 'Medicine', 3.95, 'Medical', 'JKL Medical College', 'USA'),
    ('Aiden', 'Wilson', '1998-11-30', 'Psychology', 3.85, 'Social Sciences', 'QRS College', 'Canada'),
    ('Olivia', 'Martinez', '1997-03-05', 'Chemical Engineering', 3.75, 'Engineering', 'TUV Institute', 'Australia'),
    ('Ethan', 'Garcia', '1999-08-12', 'English Literature', 3.8, 'Humanities', 'WXY University', 'UK'),
    ('Sophia', 'Lopez', '1998-06-28', 'History', 3.65, 'Humanities', 'IJK College', 'Germany')
]

# Insert the sample data into the table
cursor.executemany("INSERT INTO STUDENT_INFO VALUES (?, ?, ?, ?, ?, ?, ?, ?)", sample_data)

# Display all the records in the table
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT_INFO")
for row in data:
    print(row)

# Commit changes to the database
connection.commit()

# Close the connection to the database
connection.close()