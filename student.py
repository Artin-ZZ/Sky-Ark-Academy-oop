# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# For Test
# user_grades = db.query("SELECT * FROM grades WHERE student_id = 1 ORDER BY id DESC").fetchone()
# print(user_grades)

# Page title
print("Search student by ID.")

# Prompt for the student id
student_id = info.get_info('Student Id: ', 'str')


# Check for existense
if not db.fetch_student(student_id):
    print("Student doesn't exist!")
    exit()

# Print the student info
student = db.fetch_student(student_id)

result = """ Full Name | Age | Student ID | Identity ID | Phone Number | Last Grade | Description \n"""
result += f"""Name: {student['full_name']} | {student['age']} | {student['student_id']}  | {student['identity_id']}  | {student['phone_number']} | {student['last_grade']} | {student['description']}  \n"""

# Print the student last 10 grades
student_grades = db.query(
    f"""SELECT * FROM grades WHERE student_id = {student['id']} ORDER BY id DESC""").fetchmany(5)

new_result = " Grade | Lesson \n"
for student_grade in student_grades:
    new_result += f""" {student_grade['grade']} | {student_grade['lesson']} \n"""

print(result)
print(new_result)
