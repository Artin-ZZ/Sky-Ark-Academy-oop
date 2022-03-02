# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Show all Courses.")

# Check for existense
if not db.fetch_courses():
    print("No Courses Found Or Course doesn't exist!")
    exit()

# Print the results
courses = db.fetch_courses()


result = """ course Name | Course  Id | Hwo Is Teaching This Course? \n"""
for course in courses:
    result += f""" {course['cs_name']} | {course['cs_number']} | {course['cs_prof']}\n"""
print(result)
