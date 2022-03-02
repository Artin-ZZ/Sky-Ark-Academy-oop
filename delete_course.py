# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete A Course.")

# Prompt for the Course name
cs_number = info.get_info('Course Number: ', 'str')

# Course status
course_status = db.course_status(cs_number)


if not course_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info(
        'Do you want to delete this Course? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.course_delete(cs_number):
            message = "The Course deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The Course doesn't exist!"

# print result
print(message)