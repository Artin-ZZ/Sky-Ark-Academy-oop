# Dependencies
from Models import Models
from Info import Info

# Instatntiate the required classes
db = Models()
info = Info()

# Page title
print("Delete Department.")

# Prompt for the Department Name
department_name = info.get_info('Department name: ', 'name')

# Department status
department_status = db.department_status(department_name)


if not department_status == -1:
    # Prompt admin to confirm the process
    confirm = info.get_info('Do you want to delete the Department? (y/n) ', 'list', ['y', 'n'])

    if confirm == 'y':
        # Delete from database
        if db.department_delete(department_name):
            message = "The Department deleted successfully!"
        else:
            message = "Oops, an error occoured!!"

    # Rejected
    else:
        message = "The process has been cancelled!"

else:
    message = "The Department doesn't exist!"

# print result
print(message)
