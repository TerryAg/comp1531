import random
import copy

"""
This function returns a new list that is created by shuffling the elements of the
provided list
:param li: The list to be shuffled
:return shuffled_list: The shuffled list
"""

user_list = input("Put a few comma separated characters\n").split(',')


def shuffle(li):
    new_L = li[:]
    random.shuffle(new_L)
    return ','.join(new_L)

print(shuffle(user_list))

