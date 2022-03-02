# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Show all registered students.")

# Check for existense
if not db.fetch_students():
    print("No Students Found Or Student doesn't exist!")
    exit()

# Print the results
students = db.fetch_students()

result = """ Full Name | Age | Student ID | Identity ID | Phone Number | Last Grade | Description \n"""
for student in students:
    result += f""" {student['full_name']} | {student['age']} | {student['student_id']}  | {student['identity_id']}  | {student['phone_number']} | {student['last_grade']} | {student['description']}  \n"""
print(result)