# Import dependencies
from Info import Info
from Models import Models
from helpers import random_id


# Instatntiate the required classes
db = Models()
info = Info()
student_id = random_id()



# Page title
print("Enter Info In Order To Register students.")

# Prompt the user for require info
full_name = info.get_info('Student Full Name: ', 'name')
student_id = random_id()
identity_id = info.get_info('Student Identity Number: ', 'int')
age = info.get_info("Student Age: ", 'int')
phone_number = info.get_info("Enter Phone Number: ", 'int')
last_grade = info.get_info("Student's Last Grade: ", 'float')
description = info.get_info('Student Description: ', 'str')



# Register user
db.create_students(full_name, student_id, identity_id, age, phone_number, last_grade, description)

# User registered
print("The Student was registered successfully!")
