# Import dependencies
from Info import Info
from Models import Models
from helpers import random_id

# Instatntiate the required classes
db = Models()
info = Info()
professor_id = random_id()

# Page title
print("Enter Info In Order To Register Professors.")


# Prompt the user for require info
full_name = info.get_info('Professor Full Name: ', 'name')
identity_id = info.get_info('Professor Identity Number: ', 'int')
phone_number = info.get_info("Enter Phone Number: ", 'int')
professor_id = random_id()
age = info.get_info("Professor's Age: ", 'int')


# Register user
db.create_professors(full_name, professor_id, identity_id, phone_number, age)

# User registered
print("The Professor was registered successfully!")