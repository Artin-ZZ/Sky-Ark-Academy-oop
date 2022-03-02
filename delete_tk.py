# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete Ticket.")

# Prompt for the Ticket tracking code
ticket_token = info.get_info('Ticket tracking code: ', 'str')

# ticket status
ticket_status = db.ticket_status(ticket_token)


if not ticket_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to delete the ticket? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.ticket_delete(ticket_token):
            message = "The ticket deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The tracking code doesn't exist!"

# print result
print(message)
