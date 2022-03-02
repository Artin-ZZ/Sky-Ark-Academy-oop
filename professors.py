# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Show all registered Professors.")

# Check for existense
if not db.fetch_professors():
    print("No Professors Found Or Professor doesn't exist!")
    exit()

# Print the results
professors = db.fetch_professors()


result = """ Full Name | Professor ID | Identity ID | Phone Number | Age \n"""
for professor in professors:
    result += f""" {professor['full_name']} | {professor['professor_id']}  | {professor['identity_id']}  | {professor['phone_number']} | {professor['age']} \n"""
print(result)