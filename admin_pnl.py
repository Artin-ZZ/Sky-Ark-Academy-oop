# Import dependencies
from Info import Info

# Instantiate the Info class
info = Info()


# Main admin pannel function
def admin():

    # App title
    print("**************************************\n")
    print('Hi !, Welcome To Sky Ark Academy App. \n')

    # Navigate to models of the app
    text = "----------------------------------\n"
    text += "***| Please Select An Option |***\n"
    text += "*********************************\n"
    text += "***|--------Students---------|***\n"
    text += "***| 1.Register A Student    |***\n"
    text += "***| 2.Search Students By Id |***\n"
    text += "***| 3.Show All Students     |***\n"
    text += "***| 4.Delete Or Expel       |***\n"
    text += "*********************************\n"
    text += "***|-------Professors--------|***\n"
    text += "***| 5.Register A Professor  |***\n"
    text += "***| 6.Search Professors     |***\n"
    text += "***| 7.Show All Professors   |***\n"
    text += "***| 8.Delete Or Expel       |***\n"
    text += "*********************************\n"
    text += "***|-------Departments-------|***\n"
    text += "***| 9.Add Departments       |***\n"
    text += "***| 10.Search Departments   |***\n"
    text += "***| 11.Show All Departments |***\n"
    text += "***| 12.Delete Or remove     |***\n"
    text += "*********************************\n"
    text += "***|--------Courses----------|***\n"
    text += "***| 13.Course Registration  |***\n"
    text += "***| 14.Search Cources       |***\n"
    text += "***| 15.See All Courses      |***\n"
    text += "***| 16.Delete A Course      |***\n"
    text += "*********************************\n"
    text += "***|--------Contact-Us-------|***\n"
    text += "***| 17.Our Contact Info     |***\n"
    text += "***| 18.Help And tickets     |***\n"
    text += "***| 19.Search Tickets       |***\n"
    text += "***| 20.Show All Tickets     |***\n"
    text += "***| 21.Update Status        |***\n"
    text += "***| 22.Delete Ticket        |***\n"
    text += "*********************************\n"
    text += "Type In Your Selected Navigation: "


    navigation = info.get_info(text, 'int')
    #------Students----#
    # Register Student
    if navigation == 1:
        import register_s
        

    # Search user selected
    elif navigation == 2:
        import student
    

    # Show user selected
    elif navigation == 3:
        import students
        
        
    # Delete
    elif navigation == 4:
        import delete_student
    
        
    #----Professors-----#
    # Register Professor
    elif navigation == 5:
        import register_p
        
        
    #Search By Id
    elif navigation == 6:
        import professor
    
    # Show All
    elif navigation == 7:
        import professors

        
    #Delete
    elif navigation == 8:
        import delete_professor
        
        
        
    #----Departments----#
    # Register
    elif navigation == 9:
        import register_d
        
        
    #Search By Name
    elif navigation == 10:
        import department
        
        
    # Show All
    elif navigation == 11:
        import departments
        
        
    # Delete
    elif navigation == 12:
        import delete_department
        
        
    #-----Courses-------#
    # Register
    elif navigation == 13:
        import register_c
        
    
    #Search By Name
    elif navigation == 14:
        import course
        
        
    # Show All
    elif navigation == 15:
        import courses
        
        
    # Delete
    elif navigation == 16:
        import delete_course
        
        
    #-----Contact-us----#    
    # Constant Contact info
    elif navigation == 17:
       import help_ticket
       
       
    # help and tickets Submit
    elif navigation == 18:
        import register_tk
        
        
    # Search Tickets
    elif navigation == 19:
        import track_tk
        
        
    # Show All Tickets
    elif navigation == 20:
        import show_tickets
        
        
    # Edit Tickets
    elif navigation == 21:
        import process_tk
        
    
    elif navigation == 22:
        import delete_tk

        
        
    # Invalid navigation
    else:
        print("Please select a valid navigation.")
        navigation = info.get_info(text, 'int')


# Run the application
if __name__ == '__main__':
    admin()
