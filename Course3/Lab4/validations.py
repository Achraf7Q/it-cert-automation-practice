#!/usr/bin/env python3

import re

def validate_user(username, minlen):

    if minlen < 3:

        return False

    if not username[0].isalpha():  # Check if the first character is a letter

        return False

    if len(username) < minlen:

        return False

    return True


print(validate_user("blue.kale", 3)) # True

print(validate_user(".blue.kale", 3)) # Currently True, should be False

print(validate_user("red_quinoa", 4)) # True

print(validate_user("_red_quinoa", 4)) # Currently True, should be False
