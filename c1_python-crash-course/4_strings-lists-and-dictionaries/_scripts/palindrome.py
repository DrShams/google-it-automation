def is_palindrome(input_string):
# We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for word in input_string.strip().lower():
    # Add any non-blank letters to the
    # end of one string, and to the front
    # of the other string.
        #print(word)
        if word != " ":
            new_string = new_string + word
            #print(new_string)
            reverse_string = word + reverse_string
        # Compare the strings
    if new_string == reverse_string:

        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
