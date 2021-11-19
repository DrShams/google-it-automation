print('assignment #1\n')
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
#newfilenames =[x for x in filenames if 'hpp' in x x.replace("hpp", "h",inreplace=True)]
newfilenames = [line.replace('.hpp','.h') for line in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


print('\nassignment #2\n')
def pig_latin(text):
  words = text.split()
  say = []

  for word in words:
    word = word[1:] + word[0] + 'ay'
    say.append(word)

  return ' '.join(say)

print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

print('\nassignment #3:permissions\n')
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += '-'
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

print('\nassignment #5\n')
def group_list(group, users):
  members = ', '.join(users)
  return "{}: {}".format(group,members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

print('\nassignment #6\n')
def guest_list(guests):
	for data in guests:
		name, years, job = data
		print("{} is {} years old and works as {}".format(name, years, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
