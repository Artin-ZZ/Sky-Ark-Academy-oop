# Dependencies
from Models import Models
from Info import Info


# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Search Professor by ID.")

# Prompt for the Professor Id
professor_id = info.get_info('Professor Id: ', 'str')

# Check for existense
if not db.fetch_professor(professor_id):
    print("Professor doesn't exist!")
    exit()

# Print the results
professor = db.fetch_professor(professor_id)


result = """ Full Name | Professor ID | Identity ID | Phone Number | Age \n"""
result += f""" {professor['full_name']} | {professor['professor_id']}  | {professor['identity_id']}  | {professor['phone_number']} | {professor['age']} \n"""


print(result)