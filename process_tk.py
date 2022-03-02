# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Process Ticket.")

# Prompt for the Ticket tracking code
ticket_token = info.get_info('Ticket tracking code: ', 'str')

# ticket status
ticket_status = db.ticket_status(ticket_token)

if ticket_status == 0:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to mark the ticket as processed? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Update database (set status to 1)
        if db.ticket_process(ticket_token):
            message = "The ticket marked as processed!"
        else:
            message = "Oops, an error occoured!!"

    # Update database (set status to 1)
    else:
        message = "The process has been cancelled!"

elif ticket_status == 1:
    # Alert admin that already processed
    message = "The ticket is already processed!"

elif ticket_status == -1:
    message = "The tracking code doesn't exist!"

# print result
print(message)