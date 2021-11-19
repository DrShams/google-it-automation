def skip_elements(elements):
	# Initialize variables
	new_list = []

	# Iterate through the list
	for i, elem in enumerate(elements):
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(elem)

	return new_list

def skip_elements(elements):
# code goes here
    element = [e for i, e in enumerate(elements) if i % 2 == 0]
    element.insert(3,'NewMe') # add value witn (index, 'value')
    #element.pop(0) #   removes value with (index)
    for x in element:
        if 'NewMe' in element:
            element.remove('NewMe')

    return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
