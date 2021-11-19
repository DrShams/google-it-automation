#!/usr/bin/python3

def validate_user(name, minlen):
    assert type(name) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(name) < minlen:
        return False
    if not name .isalnum():
        return False
    return True

#LAB
#1
my_list = [27, 5, 9, 6, 8]
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print("1",RemoveValue(27))
#print("2",RemoveValue(27))




#2
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

my_new_list = [6, 3, 8, "12", 42]
#print(OrganizeList(my_new_list))
#without assert
#TypeError: '<' not supported between instances of 'str' and 'int'



#3
import random

participants = ['Jack','Jill','NotLarry','Tom']

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        return None

print(Guess(participants))
