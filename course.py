# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Search Course by Name.")

# Prompt for the Course Name
cs_number = info.get_info('Course Name: ', 'str')

# Check for existense
if not db.fetch_course(cs_number):
    print("Course doesn't exist!")
    exit()

# Print the results
course = db.fetch_course(cs_number)

result = """ course Name | Course  Id | Hwo Is Teaching This Course? \n"""
result += f""" {course['cs_name']} | {course['cs_number']} | {course['cs_prof']}\n"""


print(result)
