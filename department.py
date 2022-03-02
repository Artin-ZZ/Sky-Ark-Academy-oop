# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Search Department by ID.")

# Prompt for the Department Name
department_name = info.get_info('Department Name: ', 'str')

# Check for existense
if not db.fetch_department(department_name):
    print("Department doesn't exist!")
    exit()

# Print the results
department = db.fetch_department(department_name)


result = """ Department Name | How Many Stories? | How Many Class Rooms? | What Courses this Department Has | Description \n"""
result += f""" {department['department_name']} | {department['department_story']} | {department['cls_number']} | {department['dep_courses']} | {department['description']}\n"""


print(result)