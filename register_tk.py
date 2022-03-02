# Import dependencies
from Info import Info
from Models import Models
from helpers import random_string


# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Send Ticket.")

# Prompt the user for require info
email = info.get_info('User Email: ', 'email')
subject = info.get_info("Ticket Subject: ", 'str')
description = info.get_info('Ticket Description: ', 'str')
user_type = info.get_info("User Type: (student/professor) ", datatype="list", lst=["student", "professor"])
user_id = info.get_info("User Id: ", 'int')
ticket_token = random_string()


# Create ticket
ticket_token = db.create_ticket(email, subject, description, user_type, user_id, ticket_token)

# Success
message = f"Your Ticket Has Been Submitted Successfully!\n"
message += f"Your tracking code is: {ticket_token}"
print(message)