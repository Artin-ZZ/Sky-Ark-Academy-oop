# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Show All Tickets.")

# Check for existense
if not db.show_tickets():
    print("Ticket doesn't exist!")
    exit()

# Print the results
tickets = db.show_tickets()

result = """ Email | User Type | User ID | Tracking Code | Status | Subject | Description \n"""
for ticket in tickets:
    status = "Processed" if ticket['read_ticket'] == 1 else "In Process" 
    result += f""" {ticket['email']} | {ticket['user_type'].capitalize()} | {ticket['user_id']}  | {ticket['ticket_token']}  | {status} | {ticket['subject']} | {ticket['description']}  \n"""

print(result)