# Import dependencies
from Info import Info
from Models import Models


# Instatntiate the required classes
db = Models()
info = Info()


# Page title
print("Enter Info In Order To Register Courses.")

# Prompt the user for require info
cs_name = info.get_info("Course Name: ", 'name')
cs_number = info.get_info("Enter Course's Code: ", 'int')
cs_prof = info.get_info("Which Professor Is Representing This Course?: ", 'str')



# Register user
db.create_courses(cs_name, cs_number, cs_prof)


# User registered
print("The Course was registered successfully!")