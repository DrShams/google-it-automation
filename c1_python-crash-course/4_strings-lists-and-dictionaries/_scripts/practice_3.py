print("assignment #1\n")
def format_address(address_string):
  x = address_string.split()
  return "house number {} on street named {}".format(x[0],x[1]+" "+x[2])

print(format_address("123 Main Street"))
print(format_address("1001 1st Ave"))
print(format_address("55 North Center Drive"))




print("assignment #2\n")
def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))



print("assignment #3\n")
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  #list2.sorted()
  new_list = list2
  for i in reversed(range(len(list1))):
    new_list.append(list1[i])
  return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))




print("assignment #4 list comprehension\n")
def squares(start, end):
	return [ x ** 2 for x in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



print("assignment #5\n")
def car_listing(car_prices):
  result = ""
  for k in car_prices.keys():
    result += "{} costs {} dollars".format(k,car_prices[k]) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))



print("assignment #6\n")
def combine_guests(guests1, guests2):
    guests2.update(guests1)
    return guests2
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))



print("assignment #7\n")
def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():
        if letter.isalpha():
            if letter in result:
                result[letter] += 1
            # Add or increment the value in the dictionary
            else:
                result[letter] = 1
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
