# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete A Student.")

# Prompt for the student id
student_id = info.get_info('Student Id: ', 'str')

# Student status
student_status = db.student_status(student_id)

if not student_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to delete this Student? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.student_delete(student_id):
            message = "The Student deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The Student doesn't exist!"

# print result
print(message)
