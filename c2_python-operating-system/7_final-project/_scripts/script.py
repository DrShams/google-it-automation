#EXERCISE 1
import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
x = re.search(r"ticky: INFO: ([\w ]*) ", line)
print(x)

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
x= re.search(r"ticky: ERROR: ([\w ]*) ", line)
print(x[1])



#EXERCISE 2
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
#option #1
x = sorted(fruit.items())
#print(x)
import operator
x = sorted(fruit.items(), key=operator.itemgetter(0))
print(x)

#option #2
x = sorted(fruit.items(), key=operator.itemgetter(1))
print(x)
x = sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
print(x)



#EXERCISE 3
