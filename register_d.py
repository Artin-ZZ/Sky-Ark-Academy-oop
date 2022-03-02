# Import dependenciess
from Info import Info
from Models import Models


# Instatntiate the required classes
db = Models()
info = Info()


# Page title
print("Enter Info In Order To Register Departments.")

# Prompt the user for require info
description = info.get_info('Department Description: ', 'str')
department_name = info.get_info("Enter Department Name: ", 'name')
department_story = info.get_info("How Many Stories This Building Has? ", 'int')
cls_number = info.get_info("How Many Class Rooms The Department Has? ", 'int')
dep_courses = info.get_info("Which Courses This Department Has? ", 'str')


# Register user
db.create_departments(department_name, department_story, cls_number, dep_courses, description)

# User registered
print("The Department was registered successfully!")