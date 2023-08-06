import logging
import re

def split_recursive(b_string):
    unit=16
    c_string= b_string[:unit]
    if len(b_string)>unit:
        a=0
        while a< len(b_string) :
            c_string += b_string[unit :] + "\\n"
            a+=unit
    return c_string


def format_name_string(a_string, action=None):
    """

    :param a_string:
    :param action:
    :return: sring --terragrunt-json-out
    """
    if action == 'split':
        if len(a_string) > 17:
            #a_string = a_string[:16] + "\\n" + a_string[16:]
            a_string= split_recursive(a_string)

    elif action == 'format':

        a_string = re.sub('[-!?@.+]', '', a_string)
        a_string = a_string.replace(" ", '')
    return a_string


st= "151377982441-aws-dev-bank4us-product-sophos"

print(format_name_string(st, "split"))