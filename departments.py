# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Show all registered Departments.")

# Check for existense
if not db.fetch_departments():
    print("No Departments Found Or Department doesn't exist!")
    exit()

# Print the results
departments = db.fetch_departments()

result = """ Department Name | How Many Stories? | How Many Class Rooms? | What Courses this Department Has | Description \n"""
for department in departments:
    result += f""" {department['department_name']} | {department['department_story']} | {department['cls_number']} | {department['dep_courses']} | {department['description']}\n"""
print(result)