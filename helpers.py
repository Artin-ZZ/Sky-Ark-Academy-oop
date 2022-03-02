# Import dependencies
import re
import time
import string
import random

##
# @desc Convert tuple list into dictionary list, for SQLite Database
#
# @param cur: object - database connection cursor
# @param row: object - database rows
#
# @var d: dict
#
# @retun dict
##
def dict_factory(cur: object, row: object):
    d = {}

    for i, col in enumerate(cur.description):
        d[col[0]] = row[i]

    return d


##
# @desc Generates random string
# 
# @param [size]: int -- The size of output (characters)
# @param [chars]: str -- The type of characters
# 
# @return str




# Random Unique Token Generator
def random_string(chars:str=string.ascii_uppercase + string.digits):
    result = f'{round(time.time() * 1000)}#'
    result += ''.join(random.choice(chars) for _ in range(16))
    return result

# Email Validator
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

# Random Unique Id Generator
def random_id(chars: str = string.ascii_uppercase + string.digits):
    result = 'SAA'
    result  = f'{round(time.time() * 1000)}'
    return result