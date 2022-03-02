# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Track Ticket.")

# Prompt for the student id
ticket_token = info.get_info('Your tracking code: ', 'str')

# ticket status
ticket_token = db.ticket_status(ticket_token)

if ticket_token == 0:
    message = "Your ticket is in process."

elif ticket_token == 1:
    message = "Your ticket has been processed, and the result will be sent to your email."

elif ticket_token == -1:
    message = "The tracking code doesn't exist!"

# print result
print(message)
