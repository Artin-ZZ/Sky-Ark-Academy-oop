# Import dependencies
import re
from helpers import valid_email


#
# @desc Input user information and validate
#
# @param text: str -- The text to show the user
# @param datatype: str -- The datatype of user input to validate
#
# @var data: object -- A variable to hold the user input
#
# @return any -- Depending on datatype
#


class Info:
    # Constructor method
    def __init__(self) -> None:
        pass

    def get_info(self, text: str, datatype: str, lst:list=[]):
        # Python trick for do while
        while True:
            # Input the user data
            data = input(text)

            result = ""

            # Check the type
            try:
                if datatype == 'int':
                    result = int(data)
                    break
                
                elif datatype == 'float':
                    result = float(data)
                    break

                elif datatype == 'name':
                    if self.check_name(data):
                        result = str(data)
                        break

                elif datatype == 'str':
                    result = str(data)
                    break

                elif datatype == 'email':
                    if valid_email(data):
                        result = str(data)
                        break
                    else:
                        print("Invalid email.")
                        continue

                elif datatype == 'list':
                    result = str(data)

                    if result in lst: 
                        break
                    else:
                        print(f"Please select from {lst}.")
                        continue

                else:
                    if self.check_name(data):
                        result = str(data)
                        break

            # Handle the errors
            except:
                print(f"{result} must be of type {datatype}.")

        # Return the data
        return result

    # Check user name for correct characters
    # only accepts the English alphabetical characters
    def check_name(self, text: str):
        # Check required model name
        if not text:
            print("The name is required!")
            return False

        elif len(text) < 2:
            print("The name must be al least 2 characters!")
            return False

        # Regular expression
        regex = '^[A-Za-z ]+$'

        # Valid name
        if not re.match(regex, text):
            print("Invalid characters!")
            return False

        # Invalid name
        else:
            return True
