# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete A Professor.")

# Prompt for the student id
professor_id = info.get_info('Professor Id: ', 'str')

# Professor status
professor_status = db.professor_status(professor_id)


if not professor_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to delete this Professor? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.professor_delete(professor_id):
            message = "The Professor deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The Professor doesn't exist!"

# print result
print(message)